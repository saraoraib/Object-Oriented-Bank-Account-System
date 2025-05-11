from datetime import datetime


class Transaction:
    def __init__(self, transaction_type: str, amount: float):
        self.transaction_type = transaction_type  # "Deposit" or "Withdrawal"
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        day_name = self.timestamp.strftime('%A')
        date = self.timestamp.strftime('%d %B %Y')
        time = self.timestamp.strftime('%I:%M%p').lower()
        if self.transaction_type == "Deposit":
            return f"تم إيداع {self.amount:.2f} ريال في يوم {day_name}، {date}، الساعة {time}."
        else:
            return f"تم خصم {self.amount:.2f} ريال من رصيدك البنكي في يوم {day_name}، {date}، الساعة {time}."


class BankAccount:
    def __init__(self, owner_name: str):
        self.__owner = owner_name
        self.__balance = 0.0
        self.__transactions = []  # List to keep track of all transactions

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("المبلغ المُودع يجب أن يكون أكبر من صفر.")
        self.__balance += amount
        transaction = Transaction("Deposit", amount)
        self.__transactions.append(transaction)
        print(transaction)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("المبلغ المسحوب يجب أن يكون أكبر من صفر.")
        if amount > self.__balance:
            print("رصيد غير كافٍ.")
            return
        self.__balance -= amount
        transaction = Transaction("Withdrawal", amount)
        self.__transactions.append(transaction)
        print(transaction)

    def get_balance(self) -> float:
        print(f"الرصيد الحالي: {self.__balance:.2f} ريال")
        return self.__balance

    def get_transaction_history(self):
        if not self.__transactions:
            print("لا يوجد عمليات حتى الآن.")
        else:
            print(f"سجل العمليات لحساب {self.__owner}:")
            for transaction in self.__transactions:
                print("-", transaction)

    def get_account_owner(self) -> str:
        return self.__owner

account = BankAccount("Sara Oraib")

account.deposit(2500)
account.withdraw(400)
account.get_balance()
account.get_transaction_history()