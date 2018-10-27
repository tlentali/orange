
import pulp
from pulp import LpVariable, LpProblem, lpSum, LpMinimize
import pandas as pd


def bin_packing(items, binCapacity, binCost):
    itemCount = len(items)
    maxBins = len(binCapacity)

    y = pulp.LpVariable.dicts('BinUsed', range(
        maxBins), lowBound=0, upBound=1, cat=pulp.LpInteger)

    possible_ItemInBin = [(itemTuple[0], binNum)
                          for itemTuple in items for binNum in range(maxBins)]

    x = pulp.LpVariable.dicts('itemInBin', possible_ItemInBin,
                              lowBound=0, upBound=1, cat=pulp.LpInteger)

    # Model formulation
    prob = pulp.LpProblem("Bin Packing Problem", LpMinimize)

    # Objective
    prob += pulp.lpSum([binCost[i] * y[i] for i in range(maxBins)])

    # Constraints
    for j in items:
        prob += pulp.lpSum([x[(j[0], i)] for i in range(maxBins)]) == 1
    for i in range(maxBins):
        prob += pulp.lpSum([items[j][1] * x[(items[j][0], i)]
                            for j in range(itemCount)]) <= binCapacity[i] * y[i]
    prob.solve()
    return x


def display_result(x):
    # convert to dataframe
    df_items = pd.DataFrame(items, columns=['item_number', 'size'])
    df_bin_capacity = pd.DataFrame(binCapacity, columns=['capacity'])
    df_bin_cost = pd.DataFrame(binCost, columns=['cost'])
    df_bin = pd.merge(df_bin_capacity, df_bin_cost,
                      right_index=True, left_index=True)
    df_bin['bin_number'] = df_bin.index

    res = []
    for i in x.keys():
        if x[i].value() == 1:
            res.append(i)

    df_res = pd.DataFrame(res, columns=['item', 'bin']).sort_values(by=['bin'])
    df_summary = pd.merge(df_res, df_bin, left_on=[
                          'bin'], right_on=['bin_number'])
    df_summary = pd.merge(df_summary, df_items, left_on=[
                          'item'], right_on=['item_number'])
    col_summary = list(set(df_summary).difference(
        set({'bin_number', 'item_number'})))
    df_summary = df_summary[col_summary]

    # display result
    nb_bin_used = df_summary['bin'].nunique()
    df_comp_size = df_summary.copy()
    size_used = df_comp_size.groupby('bin')['size'].sum().reset_index()
    df_remaining = pd.merge(
        size_used, df_bin, left_on=['bin'], right_index=True, how='left')
    df_remaining['spare'] = df_remaining['capacity'] - df_remaining['size']
    remain = df_remaining['spare'].sum()
    cost = df_remaining['cost'].sum()

    print('Number of bin used : {}'.format(nb_bin_used))
    print('Remaining total : {}'.format(remain))
    print('Cost tot : {}'.format(cost))
    print('\nSize remaining for each bin :\n')
    print(df_remaining[['bin', 'spare', 'cost']])
    print('\nDetail :\n')
    print(df_summary)

    #print("Bins used: " + str(sum(([y[i].value() for i in range(maxBins)]))))
    '''
    for i in x.keys():
        if x[i].value() == 1:
            print("Item {} is packed in bin {}.".format(*i))
    '''


if __name__ == '__main__':

    items = [("a", 5),
             ("b", 6),
             ("c", 7),
             ("d", 32),
             ("e", 2),
             ("f", 32),
             ("g", 5),
             ("h", 7),
             ("i", 9),
             ("k", 12),
             ("l", 11),
             ("m", 1),
             ("n", 2)]

    binCapacity = [11, 15, 10, 32, 32, 20, 32, 32, 32, 32, 32]
    binCost = [10, 30, 20, 23, 23, 23, 32, 3, 3, 3, 3]
    display_result(bin_packing(items, binCapacity, binCost))
