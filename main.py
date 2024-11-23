import requests
from xml.etree import ElementTree

# URL ЦБ РФ
url = 'https://www.cbr.ru/scripts/XML_daily.asp'

# Запрос
response = requests.get(url)
tree = ElementTree.fromstring(response.content)

# Парсинг курса валют
usd_to_rub = float(tree.find("./Valute[CharCode='USD']/Value").text.replace(',', '.'))
eur_to_rub = float(tree.find("./Valute[CharCode='EUR']/Value").text.replace(',', '.'))
kzt_to_rub = float(tree.find("./Valute[CharCode='KZT']/Value").text.replace(',', '.'))
aud_to_rub = float(tree.find("./Valute[CharCode='AUD']/Value").text.replace(',', '.'))
byn_to_rub = float(tree.find("./Valute[CharCode='BYN']/Value").text.replace(',', '.'))  

print()
print("Курс валют на сегодня:")
print(f"1 Доллар в рублях: {usd_to_rub:.2f}")
print(f"1 Евро в рублях: {eur_to_rub:.2f}")
print(f"1 Тенге в рублях: {kzt_to_rub:.5f}")
print(f"1 Австралийский доллар в рублях: {aud_to_rub:.5f}")
print(f"1 Белорусский рубль в рублях: {byn_to_rub:.5f}")
print()

inputUser = int(input("Введите ваш баланс в рублях = "))
print()

balanceRub = inputUser
balanceUsd = 0
balanceEur= 0
balanceKzt = 0
balanceAud = 0
balanceByn = 0

def showBalance():
    print()
    print(f"Баланс Рубля = {balanceRub:.2f}")
    print(f"Баланс Доллара = {balanceUsd}")
    print(f"Баланс Евро = {balanceEur}")
    print(f"Баланс Тенге = {balanceKzt}")
    print(f"Баланс австралийского доллара = {balanceAud}")
    print(f"Баланс Белорусского рубля = {balanceByn}")
    print()

def buyCurrency(currency):
    global balanceRub, balanceUsd, balanceEur, balanceKzt, balanceAud, balanceByn
    # Список цен валют
    currencies = [usd_to_rub, eur_to_rub, kzt_to_rub, aud_to_rub, byn_to_rub]
    # Цена выбранной валюты
    currencyPrice = currencies[currency - 1]

    # Проверка на достаточность средств
    if balanceRub >= currencyPrice:
        balanceRub -= currencyPrice
        if currency == 1:
            balanceUsd += 1
            acceptBuy = "доллар"
        elif currency == 2:
            balanceEur += 1
            acceptBuy = "евро"
        elif currency == 3:
            balanceKzt += 1
            acceptBuy = "тенге"
        elif currency == 4:
            balanceAud += 1
            acceptBuy = "австралийский доллар"
        elif currency == 5:
            balanceByn += 1
            acceptBuy = "белорусский рубль"
        print()
        print(f"Вы успешно купили валюту: 1 {acceptBuy}. Баланс рублей теперь: {balanceRub:.2f}")
    else:
        print("Недостаточно средств для покупки валюты!")

def sellCurrency(currency):
    global balanceRub, balanceUsd, balanceEur, balanceKzt, balanceAud, balanceByn
    # Список цен валют
    currencies = [usd_to_rub, eur_to_rub, kzt_to_rub, aud_to_rub, byn_to_rub]
    # Цена выбранной валюты
    currencyPrice = currencies[currency - 1]

    # Проверка на достаточность средств
    if currency == 1:
        if balanceUsd >= 1:
            balanceUsd -= 1
            balanceRub += currencyPrice
            acceptBuy = "доллар"

            print()
            print(f"Вы успешно продали валюту: 1 {acceptBuy}. Баланс рублей теперь: {balanceRub:.2f}")
        else:
            print()
            print("Баланс долларов равен 0 вы не можете их продать")
    elif currency == 2:
        if balanceEur >= 1:
            balanceEur -= 1
            balanceRub += currencyPrice
            acceptBuy = "евро"

            print()
            print(f"Вы успешно продали валюту: 1 {acceptBuy}. Баланс рублей теперь: {balanceRub:.2f}")
        else:
            print()
            print("Баланс евров равен 0 вы не можете их продать")
    elif currency == 3:
        if balanceKzt >= 1:
            balanceKzt -= 1
            balanceRub += currencyPrice
            acceptBuy = "тенге"

            print()
            print(f"Вы успешно продали валюту: 1 {acceptBuy}. Баланс рублей теперь: {balanceRub:.2f}")
        else:
            print()
            print("Баланс тенге равен 0 вы не можете их продать")
    elif currency == 4:
        if balanceAud >= 1:
            balanceAud -= 1
            balanceRub += currencyPrice
            acceptBuy = "австралийский доллар"

            print()
            print(f"Вы успешно продали валюту: 1 {acceptBuy}. Баланс рублей теперь: {balanceRub:.2f}")
        else:
            print()
            print("Баланс австралийских долларов равен 0 вы не можете их продать")
    elif currency == 5:
        if balanceByn >= 1:
            balanceByn -= 1
            balanceRub += currencyPrice
            acceptBuy = "белорусский рубль"

            print()
            print(f"Вы успешно продали валюту: 1 {acceptBuy}. Баланс рублей теперь: {balanceRub:.2f}")
        else:
            print()
            print("Баланс белорусских рублей равен 0 вы не можете их продать")
    else:
        print("Недостаточно средств для покупки валюты!")



isStart = True

while isStart:
    comandBuyCurrency = "1"
    comandSellCurrency = "2"
    comandShowBalance = "3"
    comandExit = "4"

    print()
    print("Введите команду")
    print(f"{comandBuyCurrency} - чтобы купить валюту")
    print(f"{comandSellCurrency} - чтобы продать валюту")
    print(f"{comandShowBalance} - чтобы показать баланс")
    print(f"{comandExit} - чтобы выйти из программы")
    print()

    userInput = input()
    match userInput:
        case "1":
            print()
            print("Какую валюту вы хотите купить? Выберите из списка")
            print("1 - купить usd")
            print("2 - купить eur")
            print("3 - купить kzt")
            print("4 - купить aud")
            print("5 - купить byn")
            print()
            userInput2 = int(input())
            currency = userInput2
            buyCurrency(currency)

        case "2":   
            print()
            print("Какую валюту вы хотите продать? Выберите из списка")
            print("1 - продать usd")
            print("2 - продать eur")
            print("3 - продать kzt")
            print("4 - продать aud")
            print("5 - продать byn")
            print()
            userInput2 = int(input())
            currency = userInput2
            sellCurrency(currency)
        case "3":
            showBalance()
        case "4":
            isStart = False
        case _:
            print("Неизвестное значение")


