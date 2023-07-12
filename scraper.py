import requests
import lxml.html as html

HOME = 'https://dolarhoy.com/cotizaciondolarblue'

XPATH_LINKS = '//div[@class="tile cotizaciones_more"]//a/@href'


def parse_exchange():
    try:
        response = requests.get(HOME)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINKS)
            monedas = []

            for link in links:
                moneda = {}
                moneda['name'] = parsed.xpath(
                    f'//div[@class="tile cotizaciones_more"]//a[@href="{link}"]/div[1]/text()')[0]
                moneda['compra'] = parsed.xpath(
                    f'//div[@class="tile cotizaciones_more"]//a[@href="{link}"]/div[2]/text()')[0]
                moneda['venta'] = parsed.xpath(
                    f'//div[@class="tile cotizaciones_more"]//a[@href="{link}"]/div[3]/text()')[0]
                monedas.append(moneda)

            for moneda in monedas:
                print(f'{moneda["name"]}.')
                print(f'Compra: {moneda["compra"]}.')
                print(f'Venta: {moneda["venta"]}.\n')
        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as status:
        print(status)


def run():
    parse_exchange()


if __name__ == "__main__":
    run()
