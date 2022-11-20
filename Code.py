import requests

# def get_michigan_date(week):
#     headers = {
#             'accept': 'application/json',
#             'Authorization': 'Bearer jZGKLT++7nEywEb8ej0sEtM/+rMHPO59/KxVx/8BWlTfYpV4Hsj8+lzLpLZiwuGh',
#     }
#     params = {
#             'year': '2021',
#             'week': week,
#             'seasonType': 'regular',
#             'team': 'Michigan',
#             'division': 'fbs',
#     }
#     response = requests.get('https://api.collegefootballdata.com/games', params=params, headers=headers)
#     data_as_json = response.json()
#     start_date = (data_as_json[0]["start_date"])
#     date = start_date[:10]
#     return date

# def get_michigan_score(week):
#     headers = {
#             'accept': 'application/json',
#             'Authorization': 'Bearer jZGKLT++7nEywEb8ej0sEtM/+rMHPO59/KxVx/8BWlTfYpV4Hsj8+lzLpLZiwuGh',
#     }
#     params = {
#             'year': '2021',
#             'week': week,
#             'seasonType': 'regular',
#             'team': 'Michigan',
#             'division': 'fbs',
#     }
#     response = requests.get('https://api.collegefootballdata.com/games', params=params, headers=headers)
#     data_as_json = response.json()
#     score_total = data_as_json[0]["home_points"] + data_as_json[0]["away_points"]
#     print(score_total)
#     return score_total

# def get_michigan_temp(x):
#     string = "https://api.weatherstack.com/historical?access_key=89cc8c429b8e9d7635ec1dcc34bace1a&query=Ann%20Arbor&units=f&historical_date=" + str(get_michigan_date(x))
#     response = requests.get(string)
#     data_as_json = response.json()
#     print(data_as_json['historical'][str(get_michigan_date(x))]['avgtemp'])
#     return data_as_json['historical'][str(get_michigan_date(x))]['avgtemp']

# 14 is the max weeks that michigan played. keep range at 14. Michigan had bye week 7 so no data. If we use 10 we have positve correlation, if 14, no relationship.
# for b in range(10):
#     b += 1
#     if b == 7:
#         continue
#     else:
#         print("week ", b)
#         print('temp: '), get_michigan_temp(str(b))
#         print('score: '), get_michigan_score(str(b))

def bitcoin_price(date):
    string = f'https://api.polygon.io/v1/open-close/crypto/BTC/USD/{date}?adjusted=true&apiKey=CpYzUvAB_9CnlJ8pTQvLSqfZfN6h9dTv'
    response = requests.get(string)
    data_as_json = response.json()
    print(data_as_json["close"])
bitcoin_price("2021-08-01")


for x in range(1,29):
    if x < 10:
        x = "0" + str(x)
        print(x)
    else:
        print(x)