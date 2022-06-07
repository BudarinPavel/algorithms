def depose(clients, params):
    name, sum = params.split()
    if name not in clients:
        clients[name] = 0
    clients[name] += int(sum)


def withdraw(clients, params):
    name, sum = params.split()
    if name not in clients:
        clients[name] = 0
    clients[name] -= int(sum)


def show_balance(clients, params):
    name = params.split()[0]
    if name not in clients:
        print('ERROR')
    else:
        print(clients[name])


def transfer(clients, params):
    name1, name2, sum = params.split()
    if name1 not in clients:
        clients[name1] = 0
    if name2 not in clients:
        clients[name2] = 0
    depose(clients, name2 + ' ' + sum)
    withdraw(clients, name1 + ' ' + sum)


def income(clients, params):
    p = int(params)
    for client in clients:
        if clients[client] > 0:
            clients[client] *= 1 + p / 100
            clients[client] = int(clients[client])


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


