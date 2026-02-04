from itertools import count

class BankAccount:

    id = count(1)

    def __init__(self, name, surname, balance, enabled_overdraft):
        self.__account_number = next(self.id)
        self.__name = name
        self.__surname = surname
        self.__balance = balance
        self.__enabled_overdraft = enabled_overdraft
        self.__display()

    def __display(self):
        print("=================================")
        print(f"Compte n°{self.__account_number}")
        print(f"Nom: {self.__surname}") 
        print(f"Prénom: {self.__name}") 
        print(f"Solde: {self.__balance}€")
        print("=================================")
    
    def __display_balance(self):
        print(f"Compte n°{self.__account_number} -- Solde: {self.__balance}€")

    def __overdraft_charges(self):
        if self.__balance < 0:
            self.__balance -= self.__balance*0.07
            print(f"Agios de 7% appliqués sur le compte n°{self.__account_number}.")
    
    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):
        self.__balance += amount
        print(f"Dépot de {amount}€ sur le compte n°{self.__account_number}.")
        self.__display_balance()

    def withdrawal(self, amount):
        if isinstance(amount, int):
            if amount > 0:
                if self.__balance > amount or self.__enabled_overdraft:
                    self.__balance -= amount
                    print(f"Retrait de {amount}€ sur le compte n°{self.__account_number}.")
                    self.__overdraft_charges()
                    self.__display_balance()
                else:
                    print(f"Désolé M. {self.__surname}, il ne vous reste que {self.__balance}€ et vous n'avez pas d'autorisation de découvert, vous ne pouvez pas retirer {amount}€.")
            else:
                print(f"Désolé M. {self.__surname}, le retrait doit être supérieur à 0€.")
        else:
            print(f"Désolé M. {self.__surname}, la valeur du retrait doit être un nombre entier.")

    def transfer(self, target_account, amount):
        if self.__balance > amount or self.__enabled_overdraft:
            self.__balance -= amount
            print(f"Transfert de {amount}€ depuis le compte n°{self.__account_number} vers le compte n°{target_account.get_account_number()}.")
            target_account.deposit(amount)
            self.__overdraft_charges()
            self.__display_balance()
        else:
            print(f"Désolé M. {self.__surname}, il ne vous reste que {self.__balance}€ et vous n'avez pas d'autorisation de découvert, vous ne pouvez pas envoyer {amount}€.")


bank_account_1 = BankAccount("Bill","GATES",10000000000,True)
bank_account_2 = BankAccount("Jay","PADARGENT",50, True)
bank_account_3 = BankAccount("John","DOE", 10000, False)

bank_account_1.withdrawal(-350)
bank_account_1.withdrawal(350.6)
bank_account_2.withdrawal(350)
bank_account_1.withdrawal(350)

bank_account_3.deposit(245.6)

bank_account_2.withdrawal(600)

bank_account_3.transfer(bank_account_2, 20000)

bank_account_1.transfer(bank_account_2, 817.47) 