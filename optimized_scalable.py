import csv
import time


def read_file(file):
    reader = csv.DictReader(open(file))
    info = []
    for row in reader:
        row['price'] = float(row['price'])
        row['profit'] = float(row['profit'])
        if row['price'] > 0.0:
            row['profit'] = row['price'] * row['profit'] / 100.0
            row['profit'] = float(row['profit'])
            info.append(row)
    return info


# def sort_data_by_profit(data_set):
#     data_set.sort(key=lambda share: share['profit'], reverse=True)
#     return data_set

def sort_data_by_profit(data_set):
    data_set.sort(key=lambda share: share['profit']/share['price'], reverse=True)
    return data_set


def optimized_combinaison(shares, budget):
    best_shares = []
    for share in shares:
        if share['price'] <= budget:
            budget = budget - share['price']
            best_shares.append(share)
    return best_shares


if __name__ == '__main__':
    print('--- processing ---')
    my_data = sort_data_by_profit(read_file('stock_list.csv'))
    print("Number of shares after cleaning and optimization: " + str(len(my_data)))
    start_time = time.time()
    best_combinaison = optimized_combinaison(my_data, 500)
    max_profit = sum([share['profit'] for share in best_combinaison])
    duration = time.time() - start_time
    expanse = sum([share['price'] for share in best_combinaison])
    list_of_shares = ([share['name'] for share in best_combinaison])
    print("Search duration: %s seconds" % duration)
    print("--- Done ---")
    print(f'money spend : {expanse} €')
    print(f'profit made : {max_profit} €')
    print(f'list of shares bought: {list_of_shares}')


