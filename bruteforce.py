import csv

reader = csv.DictReader(open('stock_list.csv'))
info = []
for row in reader:
    # print(row['name'], row['price'], row['profit in (%)'])
    profit = float(row['price']) * float(row['profit in (%)']) / 100
    # print('profit for ' + row['name'] + ' is : ' + str(profit))
    # adding new key(profit in euros) and profit as value
    row['profit in euros'] = profit
    info.append(row)
# print(info)


def all_possibilities(remaining_shares, remaining_budget):
    # if there's no remaining shares we yield an empty list
    if len(remaining_shares) == 0:
        yield []

    else:
        for share in remaining_shares:
            if float(share['price']) <= remaining_budget:
                remaining_budget = remaining_budget - float(share['price'])
                remaining_shares.remove(share)
                for possibility in all_possibilities(remaining_shares, remaining_budget):
                    yield possibility + [share]
            # if the price is greater than the budget we yield an empty list
            else:
                yield []


for result in all_possibilities(info, 500.0):
    print(result)
