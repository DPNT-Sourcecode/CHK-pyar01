from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = ("A", "B", "C", "D", "E")
    num_items = {item: 0 for item in items}
    costs = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    for item in skus:
        if not item in num_items:
            return -1
        num_items[item] += 1

    # capture how many lots of 3 As there are
    three_as = int(num_items["A"] / 3)
    three_as_discount = 20
    two_bs = int(num_items["B"] / 2)
    two_bs_discount = 15
    price = sum(num_items[item] * costs[item] for item in num_items) - three_as * three_as_discount - two_bs * two_bs_discount

    return price
