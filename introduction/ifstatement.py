#
# Sha He
# 1/21/2023
# Total cost of purchase
#
pur_amount = float(input("Enter the total purchase amount: "))
member = input("Is the customer a loyalty program member(y/n): ")
if member == "y":
    if pur_amount <= 100:
        amount_ad = pur_amount * (1 - 0.15)
        tax = amount_ad * 0.06
        total = amount_ad + tax
    else:
        amount_ad = pur_amount * (1 - 0.25)
        tax = amount_ad * 0.06
        total = amount_ad + tax
else:
    amount_ad = pur_amount * (1 - 0.05)
    tax = amount_ad * 0.06
    total = amount_ad + tax

    print(f"Total after discount: ${amount_ad:.2f}")
    print(f"Sales tax: ${tax:.2f}")
    print(f"Total after tax: ${total:.2f}")