def get_total(n):
    total = 0
    for i in range(1, n + 1):
        price = float(input(f"Enter price of item {i}: "))
        if price <= 0:
            print("Invalid price")
            return None
        total += price
    return total
def apply_discount(total):
    if total > 200:
        return total * 0.10
    return 0
def apply_tax(amount):
    return amount * 0.05
def show_bill(total, discount, tax, final_amount):
    print("\nBill Summary:")
    print("Total Amount: ₹", round(total, 2))
    print("Discount Applied: ₹", round(discount, 2))
    print("Tax Added: ₹", round(tax, 2))
    print("Final Payable Amount: ₹", round(final_amount, 2))
def main():
    n = int(input("Enter number of items: "))
    if n <= 0 or n > 20:
        print("Invalid number of items")
        return
    total = get_total(n)
    if total is None:
        return
    discount = apply_discount(total)
    amount_after_discount = total - discount
    tax = apply_tax(amount_after_discount)
    final_amount = amount_after_discount + tax
    show_bill(total, discount, tax, final_amount)
main()
