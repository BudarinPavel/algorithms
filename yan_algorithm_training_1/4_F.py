customers = {}

with open('input_4F.txt') as f:
    data = f.readlines()
    for line in data:
        name, item, amount = line.split()
        if name not in customers:
            customers[name] = {}
        if item not in customers[name]:
            customers[name][item] = 0
        customers[name][item] += int(amount)

# output
for customer in sorted(customers):
    print(customer, ':', sep='')
    for item in sorted(customers[customer]):
        print(item, customers[customer][item])


