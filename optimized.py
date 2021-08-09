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


def sort_data_by_price(data_set):
    data_set.sort(key=lambda share: share['price'], reverse=True)
    return data_set



def optimized_combinaison(remaining_shares, remaining_budget):
    # if there's no remaining shares we yield an empty list
    if len(remaining_shares) == 0:
        yield []
    else:
        for i, share in enumerate(remaining_shares):
            if share['price'] <= remaining_budget:
                for possibility in optimized_combinaison(remaining_shares[i+1:], remaining_budget - share['price']):
                    yield possibility + [share]
            # if the price is greater than the budget we yield an empty list
            else:
                yield []


if __name__ == '__main__':
    print("--- Processing ---")
    start_time = time.time()
    my_data = sort_data_by_price(read_file('stock_list.csv'))
    print("Number of shares after cleaning and optimization: " + str(len(my_data)))
    max_profit = 0
    best_combinaison = []
    counter = 0
    for result in optimized_combinaison(my_data, 500.0):
        counter += 1
        total_profit = sum([share['profit in euros'] for share in result])
        if total_profit > max_profit:
            max_profit = total_profit
            best_combinaison = result
            # print([share['name'] for share in best_portfolio])
            # print('cost', sum([share['price'] for share in best_portfolio]))
            # print('profit', max_profit)
            # print("\n")
    duration = time.time() - start_time
    print("--- Done ---")

    print(counter)
    print("Search duration: %s seconds" % duration)
    print([share['name'] for share in best_combinaison])
    print('cost', sum([share['price'] for share in best_combinaison]))
    print('profit', max_profit)
