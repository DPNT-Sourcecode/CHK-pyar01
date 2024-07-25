from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    costs = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }
    num_items = {item: 0 for item in costs}
    for item in skus:
        if not item in num_items:
            return -1
        num_items[item] += 1

    # apply free Bs
    free_bs = int(num_items["E"] / 2)
    num_items["B"] = max(num_items["B"] - free_bs, 0)

    price_as = calc_as_price(num_items["A"], costs["A"])

    # apply Bs discount
    two_bs = int(num_items["B"] / 2)
    two_bs_discount = 15

    # apply Fs discount (treat buy 2 get one free as a 10 discount for every 3)
    three_fs = int(num_items["F"] / 3)
    three_fs_discount = 10

    total_discounts = (two_bs * two_bs_discount) + (three_fs * three_fs_discount)

    price = sum(num_items[item] * costs[item] for item in num_items if item != "A") - total_discounts + price_as

    return price

def calc_as_price(num_as, cost_as):
    # pricing structure means we can calculate the number of 5As first, and charge for those
    # then if there's 0-2 left over, no extra discount, or if there's 3-4 left over, apply a 20 discount
    five_as = int(num_as / 5)
    leftover_as = num_as - 5 * five_as
    price_as = five_as * 200 + leftover_as * cost_as
    if leftover_as >= 3:
        price_as -= 20

    return price_as


