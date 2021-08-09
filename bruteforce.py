import csv
import time


def read_file(file):
    reader = csv.DictReader(open(file))
    info = []
    for row in reader:
        row['price'] = float(row['price'])
        row['profit in (%)'] = float(row['profit in (%)'])
        row['profit in euros'] = row['price'] * row['profit in (%)'] / 100.0
        info.append(row)
    return info


def bruteforce(my_list):
    if len(my_list) <= 1:
        yield my_list
    else:
        my_new_list = my_list.copy()
        first_element = my_new_list.pop(0)
        for possibility in bruteforce(my_new_list):             # [3] in [[3],]
            yield possibility                                   # [3]
            yield possibility + [first_element]                 # [3] + [2] =(yield)[3,2]
        yield [first_element]                                   # [2]


if __name__ == '__main__':
    my_data = read_file('stock_list.csv')
    start_time = time.time()
    best_profit = 0
    wallet = 500.0
    best_combinaison = []

    for combinaison in bruteforce(my_data):
        total_price = 0
        total_profit = 0
        for share in combinaison:
            total_price += share['price']
            total_profit += share['profit in euros']
        if total_price >= wallet:
            continue
        if total_profit > best_profit:
            best_profit = total_profit
            best_combinaison = combinaison

    print(best_profit)
    print(best_combinaison)

    duration = time.time() - start_time
    print("Search duration: %s seconds" % duration)





