def calculate_total(price, quantity):
    return price * quantity

def calculate_discount(total, discount):
    return total - (total * discount / 100)


if __name__ == "__main__":
    total = calculate_total(100, 2)
    final_amount = calculate_discount(total, 10)

    print("Total Amount:", total)
    print("Final Amount:", final_amount)
