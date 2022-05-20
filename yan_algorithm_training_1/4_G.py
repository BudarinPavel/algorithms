def depose(clients, params):
    pass


def withdraw(clients, params):
    pass


def show_balance(clients, params):
    pass


def transfer(clients, params):
    pass


def income(clients, params):
    pass


bank_accounts = {}

with open('input_4G.txt') as f:
    commands = f.readlines()
    for line in commands:
        command, params = line.split(maxsplit=1)
        if command == 'DEPOSIT':
            depose(bank_accounts, params)
        elif command == 'WITHDRAW':
            withdraw(bank_accounts, params)
        elif command == 'BALANCE':
            show_balance(bank_accounts, params)
        elif command == 'TRANSFER':
            transfer(bank_accounts, params)
        elif command == 'INCOME':
            income(bank_accounts, params)


