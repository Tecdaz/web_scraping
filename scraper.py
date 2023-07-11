import requests
import lxml.html as html

HOME = 'https://www.ambito.com/contenidos/dolar.html'

XPATH_NAMES_EXCHANGE = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Compra")]/ancestor::node()/div/h2[@class="variation-max-min__title"]/a/span/text()'
XPATH_PRICES_BUY = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Compra")]/../span[1]/text()'
XPATH_PRICES_SELL = '//span[@class="variation-max-min__value data-valor data-venta"]/text()'

XPATH_NAMES_REFERENCE = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Referencia")]/ancestor::node()/div/h2[@class="variation-max-min__title"]/a/span/text()'
XPATH_PRICES_REFERENCE = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Referencia")]/../span[1]/text()'

def parse_exchange():
    try:
        response = requests.get(HOME)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            exchange_names = parsed.xpath(XPATH_NAMES_EXCHANGE)
            print(exchange_names)
        else:
            raise ValueError(f'Error: {response.status_code}')
        
    except ValueError as status:
        print(status)

def parse_reference():
    pass


def run():
    parse_exchange()

if __name__ == "__main__":
    run()