import requests

url = 'http://apis.data.go.kr/6290000/gjcitsdata/getTrafficStatistic'
params ={'serviceKey' : '98dVxoqIjT9M6MkINChiw8Cj6/MA2nyJ0yO5hSoqmqv4ExXZePKPKuCSlE2R7mr3JN1ClyMhb0+gYkvyI0iplQ==', 'offerDate' : '2021100615' }

response = requests.get(url, params=params)
print(response.content)