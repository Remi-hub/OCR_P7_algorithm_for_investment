import csv
import time


def read_file(file):
    reader = csv.DictReader(open(file))
    info = []
    for row in reader:
        row['price'] = float(row['price'])
        row['profit'] = float(row['profit'])
        row['profit in euros'] = row['price'] * row['profit'] / 100.0
        info.append(row)
    return info


def bruteforce(my_list):
    if len(my_list) <= 1:
        yield my_list
    else:
        my_new_list = my_list.copy()
        first_element = my_new_list.pop(0)
        for possibility in bruteforce(my_new_list):
            yield possibility
            yield possibility + [first_element]
        yield [first_element]


if __name__ == '__main__':
    my_data = read_file('stock_list.csv')
    start_time = time.time()
    best_profit = 0
    wallet = 500.0
    best_combinaison = []
    total_combinaison = 0
    for combinaison in bruteforce(my_data):
        total_price = 0
        total_profit = 0
        total_combinaison += 1
        for share in combinaison:
            total_price += share['price']
            total_profit += share['profit in euros']
        if total_price >= wallet:
            continue
        if total_profit > best_profit:
            best_profit = total_profit
            best_combinaison = combinaison

    print(f'list of shares bought: {best_combinaison}')
    print('money spend', sum([share['price'] for share in best_combinaison]), '€')
    print(f'Profit made : {best_profit} €')
    duration = time.time() - start_time
    print(f'Total search Time {duration}s')
    print(f'Total number of possible combinaison : {total_combinaison:,}')

