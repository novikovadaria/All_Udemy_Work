# ........................PIP...........................
import requests
from datetime import datetime
import pytz
response = requests.get('http://google.com')
print(response)
# local = datetime.now()
# print('local:', local.strftime('%m/%d/%Y'))
tz_0 = pytz.timezone('Europe/Moscow')
datetime_0 = datetime.now(tz_0)
# print('А в Токио сейчас', datetime_0.strftime('%m/%d/%Y, %H:%M:%S'))

tz_1 = pytz.timezone('Asia/Yerevan')
datetime_1 = datetime.now(tz_1)
# print('У котика сейчас', datetime_1.strftime('%m/%d/%Y, %H:%M:%S'))

tz_2 = pytz.timezone('Asia/Tokyo')
datetime_2 = datetime.now(tz_2)
# print('А в Токио сейчас', datetime_2.strftime('%m/%d/%Y, %H:%M:%S'))
print('У кисы сейчас', datetime_0.strftime('%H:%M:%S,'), 'но вот у котика время идёт чуть быстрее, у него сейчас', datetime_1.strftime('%H:%M:%S'),
      '\nНо когда коты будут вместе, у них у обоих будет', datetime_2.strftime('%H:%M:%S'), '\nИменно столько времени сейчас в Токио.')

# ........................Yelp..............
# Standart HTTP request
# GET
# POST
# PUT
# DELETE
