import requests
import lxml.html as html

HOME = 'https://www.ambito.com/contenidos/dolar.html'

XPATH_NAMES_EXCHANGE = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Compra")]/ancestor::node()/div/h2[@class="variation-max-min__title"]/a/span/text()'
XPATH_PRICES_BUY = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Compra")]/../span[1]/text()'
XPATH_PRICES_SELL = '//span[@class="variation-max-min__value data-valor data-venta"]/text()'

XPATH_NAMES_REFERENCE = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Referencia")]/ancestor::node()/div/h2[@class="variation-max-min__title"]/a/span/text()'
XPATH_PRICES_REFERENCE = '//span[@class="variation-max-min__description data-valor-descripcion" and contains(., "Referencia")]/../span[1]/text()'

def run():
    pass

if __name__ == "__main__":
    run()