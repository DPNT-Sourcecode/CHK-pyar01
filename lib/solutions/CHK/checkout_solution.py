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
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50,
    }

    # multibuy discounts. List in the order that the discounts should be applied
    # in the format (number, discount for that number)
    discounts = {
        "A": [(5, 50), (3, 20)],
        "B": [(2, 15)],
        "F": [(3, 10)],
        "H": [(10, 20), (5, 5)],
        "K": [(2, 10)],
        "P": [(5, 50)],
        "Q": [(3, 10)],
        "U": [(4, 40)],
        "V": [(3, 20), (2, 10)]
    }

    freebies = {
        "E": (2, "B"),
        "N": (3, "M"),
        "R": (3, "Q"),
    }

    # count items
    num_items = {item: 0 for item in costs}
    for item in skus:
        if not item in num_items:
            return -1
        num_items[item] += 1

    # apply freebies first - this works out best for customer
    for item, free_info in freebies:
        num_req, free_item = free_info
        free_count = int(num_items[item] / num_req)
        num_items[free_item] = max(num_items[free_item] - free_count, 0)

    # apply discounts
    for item, discount_info in discounts:
        discount_for_item[item] = calc_discount_for_item(num_items[item], discount_info)

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






