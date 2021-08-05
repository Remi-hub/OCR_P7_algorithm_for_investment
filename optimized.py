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
        for i, share in enumerate(remaining_shares):
            if float(share['price']) <= remaining_budget:
                # remaining_budget = remaining_budget - float(share['price'])
                updated_shares = remaining_shares[i:].copy()
                updated_shares.remove(share)
                for possibility in all_possibilities(updated_shares, remaining_budget - float(share['price'])):
                    yield possibility + [share]
            # if the price is greater than the budget we yield an empty list
            else:
                yield []


max_profit = 0
best_combinaison_of_share = []
for result in all_possibilities(info, 20.0):
    print(result)
    total_profit = sum([share['profit in euros'] for share in result])
    if total_profit > max_profit:
        max_profit = total_profit
        best_combinaison_of_share = result
        cost = sum([float(share['price']) for share in result])
        # print(cost)

print(best_combinaison_of_share)
print(max_profit)
