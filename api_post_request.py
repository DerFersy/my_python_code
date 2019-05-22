import random
import string
import requests

from bs4 import BeautifulSoup


def gen_str(len):
    return "".join([random.choice(string.letters[:26]) for i in xrange(len)])


url = "http://example_site.ru/"


payload = {
    "token": "put:any_token",
    "tax_id": gen_str(10**3),
    "company": gen_str(10**3),
    "firstname": gen_str(10**3),
    "lastname": gen_str(10**3),
    "address1": gen_str(10**3),
    "address2": gen_str(10**3),
    "postcode": gen_str(10**3),
    "city": "Moscow",
    "country_code": "RU",
    "zone_code": None,
    "email": gen_str(1000),
    "phone": "put: phone number",
    "newsletter": 1,
    "password": "put:password",
    "confirmed_password": "put:password",
    "create_account": "Create Account",
    "undefined": None
}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "put:Postman-Token"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
for notice in soup.find_all('div', {"class": "notice"}):
    print(notice.text)

