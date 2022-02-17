from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey = '98dVxoqIjT9M6MkINChiw8Cj6%2FMA2nyJ0yO5hSoqmqv4ExXZePKPKuCSlE2R7mr3JN1ClyMhb0%2BgYkvyI0iplQ%3D%3D'
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def bike():
    station = []
    pm10 = []
    url = "http://http://api.data.go.kr/openapi/tn_pubr_public_bcycl_lend_api"
    pageNo="0"
    numOfRows="100"
    type="xml"

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('type') : type, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo })
    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('bcyclLendNm'):
        station.append(tag.text)
    for tag in soup.find_all('bcyclLendSe'):
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    return res