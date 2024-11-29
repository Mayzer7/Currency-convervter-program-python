import requests
from xml.etree import ElementTree


class CurrencyConverter:
    def __init__(self) -> None:
        print(
            f"\nДобро пожаловать в конвертер валют!\n"
            f"Данная программа позволяет производить покупку и продажу валюты по курсу в реальном времени."
        )
        self.url = 'https://www.cbr.ru/scripts/XML_daily.asp'

        # Получение и парсинг данных ЦБ РФ
        response = requests.get(self.url)
        self.tree = ElementTree.fromstring(response.content)

        # Курсы валют
        self.usd_to_rub = float(self.tree.find("./Valute[CharCode='USD']/Value").text.replace(',', '.'))
        self.eur_to_rub = float(self.tree.find("./Valute[CharCode='EUR']/Value").text.replace(',', '.'))
        self.kzt_to_rub = float(self.tree.find("./Valute[CharCode='KZT']/Value").text.replace(',', '.'))
        self.aud_to_rub = float(self.tree.find("./Valute[CharCode='AUD']/Value").text.replace(',', '.'))
        self.byn_to_rub = float(self.tree.find("./Valute[CharCode='BYN']/Value").text.replace(',', '.'))

        # Балансы
        self.mainBalanceRub = 0
        self.balanceUsd = 0
        self.balanceEur = 0
        self.balanceKzt = 0
        self.balanceAud = 0
        self.balanceByn = 0

        self.balances = [
            self.balanceUsd,
            self.balanceEur,
            self.balanceKzt,
            self.balanceAud,
            self.balanceByn
        ]

    def showExchangeRates(self):
        print(
            f"\nКурс валют на сегодня:\n"
            f"1 Доллар ($) = {self.usd_to_rub:.2f}₽\n"
            f"1 Евро (€) = {self.eur_to_rub:.2f}₽\n"
            f"1 Тенге (₸) = {self.kzt_to_rub:.5f}₽\n"
            f"1 Австралийский доллар (A$) = {self.aud_to_rub:.2f}₽\n"
            f"1 Белорусский рубль (Br) = {self.byn_to_rub:.2f}₽"
        )

    def set_initial_balance(self):
        while True:
            try:
                self.mainBalanceRub += int(input("Введите ваш баланс в рублях (₽): "))
                print(f"Баланс пополнен: {self.mainBalanceRub:.0f}₽")
                break
            except ValueError:
                print("\nОшибка: введите число!\n")

    def showBalance(self):
        print(
            f"\nБаланс:\n"
            f"Рубли: {self.mainBalanceRub:.0f}₽\n"
            f"Доллары: {self.balances[0]}$\n"
            f"Евро: {self.balances[1]}€\n"
            f"Тенге: {self.balances[2]}₸\n"
            f"Австралийские доллары: {self.balances[3]}A$\n"
            f"Белорусские рубли: {self.balances[4]}Br"
        )

    def buyCurrency(self):
        currencies = [self.usd_to_rub, self.eur_to_rub, self.kzt_to_rub, self.aud_to_rub, self.byn_to_rub]
        currencyNames = ['$','€','₸','A$','Br']
        
        while True:
            try:
                print("Выберите валюту для покупки:")
                for i, name in enumerate(currencyNames, 1):
                    print(f"{i} - {name}")

                choice = int(input("Ваш выбор: ")) - 1
                if not (0 <= choice < len(currencies)):
                    raise ValueError("Некорректный выбор")

                price = currencies[choice]
                max_qty = int(self.mainBalanceRub // price)

                print(f"Вы можете купить до {max_qty}{currencyNames[choice]} (по цене {price:.2f}₽ за единицу)")
                qty = int(input(f"Сколько {currencyNames[choice]} вы хотите купить: "))
                if qty > max_qty:
                    print("Недостаточно средств!")
                else:
                    self.mainBalanceRub -= price * qty
                    self.balances[choice] += qty
                    print(f"Вы купили {qty}{currencyNames[choice]}!")
                break
            except (ValueError, IndexError):
                print("\nОшибка: введите корректное число!\n")

    def sellCurrency(self):
        currencies = [self.usd_to_rub, self.eur_to_rub, self.kzt_to_rub, self.aud_to_rub, self.byn_to_rub]
        currencyNames = ['$','€','₸','A$','Br']
        
        while True:
            try:
                print("Выберите валюту для продажи:")
                for i, name in enumerate(currencyNames, 1):
                    print(f"{i} - {name}")

                choice = int(input("Ваш выбор: ")) - 1
                if not (0 <= choice < len(currencies)):
                    raise ValueError("Некорректный выбор")

                balance = self.balances[choice]
                if balance <= 0:
                    print(f"У вас недостаточно {currencyNames[choice]} для продажи!")
                    return

                price = currencies[choice]
                print(f"У вас есть {balance}{currencyNames[choice]}. Цена за единицу: {price:.2f}₽")
                qty = int(input(f"Сколько {currencyNames[choice]} вы хотите продать: "))
                if qty > balance:
                    print("Недостаточно валюты для продажи!")
                else:
                    self.balances[choice] -= qty
                    self.mainBalanceRub += price * qty
                    print(f"Вы продали {qty}{currencyNames[choice]} за {price * qty:.2f}₽!")
                break
            except (ValueError, IndexError):
                print("\nОшибка: введите корректное число!\n")

    def addRubForMainBalance(self):
        while True:
            try:
                amount = int(input("Сумма для пополнения: "))
                if amount > 0:
                    self.mainBalanceRub += amount
                    print(f"Баланс пополнен: {amount}₽")
                else:
                    print("Введите число больше нуля!")
                break
            except ValueError:
                print("\nОшибка: введите число!\n")

    def run(self):
        while True:
            print(
                f"\nМеню:\n"
                f"1 - Купить валюту\n"
                f"2 - Продать валюту\n"
                f"3 - Показать баланс\n"
                f"4 - Пополнить баланс\n"
                f"5 - Курс валют\n"
                f"6 - Выйти"
            )
            choice = input("Ваш выбор: ")
            if choice == "1":
                self.buyCurrency()
            elif choice == "2":
                self.sellCurrency()
            elif choice == "3":
                self.showBalance()
            elif choice == "4":
                self.addRubForMainBalance()
            elif choice == "5":
                self.showExchangeRates()
            elif choice == "6":
                break
            else:
                print("Ошибка: выберите пункт меню!")


if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.showExchangeRates()
    converter.set_initial_balance()
    converter.run()