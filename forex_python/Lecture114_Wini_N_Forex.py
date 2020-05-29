from converter import CurrencyRates
from bitcoin import BtcConverter
import datetime,decimal

b = BtcConverter()
c = CurrencyRates()

def current_rate():
    c.get_rates('USD')
    print(c.get_rates('USD'))

def convert_rate():     #in use
    c.convert('USD', 'INR', 10)
    print(c.convert('USD', 'INR', 10))

def currency_on_date():
    date_obj = datetime.datetime(2014, 5, 23)
    print(c.get_rates('USD', date_obj))

def currency_compare_date():
    date_obj = datetime.datetime(2014, 5, 23)
    #c.get_rate('USD', 'INR', date_obj)
    print(c.get_rate('USD', 'INR', date_obj))

def convert_amout():    #in use
    print(c.convert('USD', 'INR', 10))

def convert_amout_date():  #in use
    date_obj = datetime.datetime(2014, 5, 23)
    c.convert('USD', 'INR', 10, date_obj)

'''
Bitcoin Part
'''

def one_bitcoin_price():    #in use
    b.get_latest_price('EUR')
    print(b.get_latest_price('EUR'))


def money_convert_bitcoin():    #in use
    b.convert_to_btc(5000, 'USD')
    print(b.convert_to_btc(5000, 'USD'))

print("-" * 50)
print('current_rate(USD)')
print(current_rate())

print("-" * 50)
print('convert_rate(INR - USD)')
print(convert_rate())

print("-" * 50)
print('USD vs All on 2014 5 23')
print(currency_on_date())

print("-" * 50)
print('USD vs INR on 2014 5 23')
print(currency_compare_date())

print("-" * 50)
print('convert amout USD - INR 10')
print(convert_amout())

print("-" * 50)
print('bitcoin_price(EUR)')
print(one_bitcoin_price())

print("-" * 50)
print('money_convert_bitcoin(THB)')
print(money_convert_bitcoin())


#Menu Part
print('')