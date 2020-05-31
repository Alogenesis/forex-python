from converter import CurrencyRates
from bitcoin import BtcConverter
import datetime,decimal

b = BtcConverter()
c = CurrencyRates()


'''test part'''
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

'''end test part'''

''' Menu Function '''
def main_menu():
    print('------------------------------------------')
    print('----------- Welcome To Coverter ----------')
    print('----------- ------------------- ----------')
    print('------- Please Select Menu Number --------')
    print('------------------------------------------')
    print('1. Currency converter')
    print('2. Currency rate compare with all nowsdays')
    print('3. History currency rate converter')
    print('4. Bitcoin price nowsdays')
    print('5. Money to bitcoin nowsdays')
    print('------------------------------------------')

def input_menu():
    loop_set = 0
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
            print('Select Menu 5. Money to bitcoin nowsdays')
            loop_set = 1
            return 5
        else:
            print('Invalid Menu Number, please select again')

#Currency List
def currency_list():
    print('Please Select Currency in List')
    print('''---------
THB  USD  EUR  JPY
HKD  INR  CHF  MXN
input 0 back to main menu
---------''')

#Menu 1
def currency_converter():
    while_loop = 1
    while while_loop == 1:
        currency_list()
        user_currency = input('Your currency >>').upper()
        if user_currency == '0':
            while_loop = 0
            print('Back to main menu')
            #break
        else:
            user_value = float(input('Input value (0 or more) >>'))
            convert_to_currency = input('Need to convert to >>').upper()
            print('------------------------------------------')
            print('------------------------------------------')
            print('{} {} = {} {}'.format(user_value, user_currency, c.convert(user_currency, convert_to_currency, user_value), convert_to_currency))
            print('------------------------------------------')
            print('------------------------------------------')

#Menu 2
def currency_compare_all():
    while_loop = 1
    while while_loop == 1:
        currency_list()
        print('Please input Main currency')
        user_currency = input('Main currency >>').upper()
        if user_currency == '0':
            while_loop = 0
            print('Back to main menu')
            # break
        else:
            print('------------------------------------------')
            print('------------------------------------------')
            print('1 {} are (unit)'.format(user_currency))
            print(c.get_rates(user_currency))
            print('------------------------------------------')
            print('------------------------------------------')

#Menu 3
def history_converter():
    while_loop = 1
    while while_loop == 1:
        currency_list()
        print('Format : Your currency , value , another currency , date')
        print('Example : 10 USD to EUR on 23/06/2014')
        print('Please input follow guide')
        user_currency = input('Your currency >>').upper()
        if user_currency == '0':
            while_loop = 0
            print('Back to main menu')
            # break
        else:
            yyyy = 2014
            mm = 10
            dd = 10
            date_obj = datetime.datetime(yyyy, mm, dd)
            user_value = float(input('Input value (0 or more) >>'))
            convert_to_currency = input('Need to convert to >>').upper()
            dd = int(input('Date (2 decimal ex. 01 to 31) >>'))
            mm = int(input('Month (2 decimal ex. 01 to 12) >>'))
            yyyy = int(input('Year (4 decimal ex. 1991 to 2019) >>'))
            print('------------------------------------------')
            print('------------------------------------------')
            print('{} {} = {} {} on {}/{}/{}'.format(user_value, user_currency,
                                         c.convert(user_currency, convert_to_currency, user_value, date_obj),
                                         convert_to_currency, dd,mm,yyyy))
            print('------------------------------------------')
            print('------------------------------------------')

#Menu 4
def bitcoin_price_now():
    while_loop = 1
    while while_loop == 1:
        currency_list()
        user_currency = input('Your currency >>').upper()
        if user_currency == '0':
            while_loop = 0
            print('Back to main menu')
            # break
        else:
            print('------------------------------------------')
            print('------------------------------------------')
            print('1 bitcoin are  = {} {}'.format(b.get_latest_price(user_currency), user_currency))
            print('------------------------------------------')
            print('------------------------------------------')

#Menu 5
def money_to_bitcoin():
    while_loop = 1
    while while_loop == 1:
        currency_list()
        user_currency = input('Your currency >>').upper()
        if user_currency == '0':
            while_loop = 0
            print('Back to main menu')
            # break
        else:
            user_value = float(input('Input value (0 or more) >>'))
            print('------------------------------------------')
            print('------------------------------------------')
            print('{} {} are {} bitcoins'.format(user_value, user_currency, b.convert_to_btc(user_value, user_currency)))
            print('------------------------------------------')
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
'''end test part'''


'''Menu Part'''
while True:
    main_menu()
    user_input = input_menu()
    if user_input == 1:
        currency_converter()

    elif user_input == 2:
        currency_compare_all()

    elif user_input == 3:
        history_converter()

    elif user_input == 4:
        bitcoin_price_now()

    elif user_input == 5:
        money_to_bitcoin()

    elif user_input == 0:
        pass
        # go main menu
    else:
        pass
        # go loop

