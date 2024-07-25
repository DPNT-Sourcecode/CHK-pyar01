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
    discount_for_item = []
    for item, discount_info in discounts:
        discounts.append(calc_discount_for_item(num_items[item], discount_info))

    price = sum(costs[x] * num_items[x] for x in num_items) - sum(discount_for_item[x])

    return price

def calc_discount_for_item(num_items, discount_info):
    total_discount = 0
    for discount in discount_info:
        num_req, val = discount
        # discount is a tuple, looks like (5, 50)
        total_discount += int(num_items / num_req) * val

        # proceed with remaining items
        num_items = num_items % num_req


    return total_discount
