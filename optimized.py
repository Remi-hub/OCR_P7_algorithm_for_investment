import csv
import time


def read_file(file):
    """Read a file  and return rows of share price and profit"""
    reader = csv.DictReader(open(file))
    info = []
    for row in reader:
        row['price'] = float(row['price'])
        row['profit'] = float(row['profit'])
        if row['price'] > 0.0:
            row['profit in euros'] = row['price'] * row['profit'] / 100.0
            row['profit in euros'] = float(row['profit in euros'])
            info.append(row)
    return info


def optimized_combinaison(shares, budget):
    """take a list and a budget as parameters, returning a list of shares with the greatest % of profit"""
    best_shares = []
    shares.sort(key=lambda share: share['profit'], reverse=True)
    for share in shares:
        if share['price'] <= budget:
            budget = budget - share['price']
            best_shares.append(share)
    return best_shares


if __name__ == '__main__':
    print('--- processing ---')
    start_time = time.time()
    my_data = read_file('dataset1_Python+P7.csv')
    print("Number of shares after cleaning and optimization: " + str(len(my_data)))
    best_combinaison = optimized_combinaison(my_data, 500)
    max_profit = sum([share['profit in euros'] for share in best_combinaison])
    duration = time.time() - start_time
    expanse = sum([share['price'] for share in best_combinaison])
    list_of_shares = ([share['name'] for share in best_combinaison])
    print("Search duration: %s seconds" % duration)
    print("--- Done ---")
    print(f'money spend : {expanse} €')
    print(f'profit made : {max_profit} €')
    print(f'list of shares bought: {list_of_shares}')


