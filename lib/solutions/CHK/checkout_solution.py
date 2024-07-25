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

    # apply free Bs
    free_bs = int(num_items["E"] / 2)
    num_items["B"] = max(num_items["B"] - free_bs, 0)

    # pricing structure means we can calculate the number of 5As first.
    # then if there's 0-2 left over, no extra discount, or if there's 3-4 left over, apply a 20 discount
    five_as = int(num_items["A"] / 5)
    leftover_as = num_items["A"] - 5 * five_as
    price_as = five_as * 200 + leftover_as * costs["A"]
    if leftover_as >= 3:
        price_as -= 20


    # apply Bs discount
    two_bs = int(num_items["B"] / 2)
    two_bs_discount = 15
    price = sum(num_items[item] * costs[item] for item in num_items) - three_as * three_as_discount - two_bs * two_bs_discount

    return price


