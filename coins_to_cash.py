def create_person(first_name, last_name, age, occupation):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation,
    }


andy = create_person("Andy", "Knepshield", 42, "Software Developer")

# print(andy)


def calculate_dollars(pennies, dimes, quarters, nickels):
    total_pennies = pennies
    total_dimes = dimes * 10
    total_quarters = quarters * 25
    total_nickels = nickels * 5

    total_cents = total_pennies + total_dimes + total_quarters + total_nickels
    total_dollars = total_cents / 100

    return total_dollars


dollar_amount = calculate_dollars(pennies=342, nickels=9, dimes=32, quarters=4)

print(f"${dollar_amount}")
