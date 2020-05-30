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

''' Menu Function '''
def welcome_message():
    print('------------------------------------------')
    print('----------- Welcome To Coverter ----------')
    print('----------- ------------------- ----------')
    print('------- Please Select Menu Number --------')
    print('------------------------------------------')

def first_menu():
    print('1. Currency converter')
    print('2. Currency rate compare with all nowsdays')
    print('3. History currency rate converter')
    print('4. Bitcoin price nowsdays')
    print('5. Values to bitcoin nowsdays')
    print('------------------------------------------')

def input_first_menu():
    loop_set = 0
    welcome_message()
    first_menu()
    while loop_set == 0:
        user_input = int(input('Menu Number >> '))
        if user_input == 1:
            print('Select Menu 1. Currency converter')
            loop_set = 1
            return 1

        elif user_input == 2:
            print('Select Menu 2. Currency rate compare with all nowsdays')
            loop_set = 1
            return 2
        elif user_input == 3:
            print('Select Menu 3. History currency rate converter')
            loop_set = 1
            return 3
        elif user_input == 4:
            print('Select Menu 4. Bitcoin price nowsdays')
            loop_set = 1
            return 4
        elif user_input == 5:
            print('Select Menu 5. Currency to bitcoin nowsdays')
            loop_set = 1
            return 5
        else:
            print('Invalid Menu Number, please select again')

def currency_list():
    print('Please Select Currency in List')
    print('''---------
THB  USD  EUR  JPY
HKD  INR  CHF  MXN
input 0 back to main menu
---------''')

def currency_converter():
    while_loop = 1
    while while_loop == 1:
        currency_list()
        user_currency = input('Your currency >>').upper()
        if user_currency == '0':
            while_loop = 0
            print('Back to main menu')
            input_first_menu()
        else:
            user_value = float(input('Input value (0 or more) >>'))
            convert_to_currency = input('Need to convert to >>').upper()
            print('{} {} = {} {}'.format(user_value, user_currency, c.convert(user_currency, convert_to_currency, user_value), convert_to_currency))
            print('------------------------------------------')





''' Test Part '''
'''
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

currency_converter()
'''



'''Menu Part'''
welcome_message()
first_menu()
user_input = int(input('Menu Number >>'))
if user_input == 1:
    print('--- Menu 1 Currency converter ---')
    currency_converter()
elif user_input ==2:
    print('Going to Menu 2')
elif user_input ==3:
    print('Going to Menu 3')
elif user_input ==4:
    print('Going to Menu 4')
elif user_input ==5:
    print('Going to Menu 5')
