from collections import defaultdict

purchases = [
    ("GE", 100, "10 - sep - 2001", 48),
    ("CAT", 100, "1 - apr - 1999", 24),
    ("GE", 200, "1 - jul - 1998", 56),
]
stockDict = {"GE": "General Electric", "CAT": "Caterpillar", "EK": "Eastman Kodak"}

company_purchases = defaultdict(list)

for purchase in purchases:
    company_name, shares, date, price = purchase
    if company_name in stockDict:
        company_purchases[company_name].append((shares, date, price))

for company_name, company_details in stockDict.items():
    if company_name in company_purchases:
        print(f"------ {company_details} ------")
        total_value = 0
        for shares, date, price in company_purchases[company_name]:
            purchase_value = shares * price
            total_value += purchase_value
            print(f"{shares} shares at {price} dollars each on {date}")
        print(f"\nTotal value of stock in portfolio: ${total_value}")
