from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey = '98dVxoqIjT9M6MkINChiw8Cj6%2FMA2nyJ0yO5hSoqmqv4ExXZePKPKuCSlE2R7mr3JN1ClyMhb0%2BgYkvyI0iplQ%3D%3D'
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def check_air():
    station = []
    pm10 = []
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    returnType="xml"
    numOfRows="100"
    pageNo="1"
    sidoName="경남"
    ver="1.0"

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('sidoName') : sidoName, quote_plus('ver') : ver })
    res = requests.get(url + queryParams)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('stationname'):
        station.append(tag.text)
    for tag in soup.find_all('pm10value'):
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    return res
