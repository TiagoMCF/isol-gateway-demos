def apply_discount(price, percent):
    return price - price * percent / 100

def checkout(items, coupon=None):
    total = sum(i["price"] * i["qty"] for i in items)
    if coupon:
        total = apply_discount(total, coupon["percent"])
    return total
