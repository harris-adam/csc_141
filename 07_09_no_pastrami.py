sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami']
print("The deli has run out of pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nRemaining sandwich orders:")
for sandwich in sandwich_orders:
    print(f"{sandwich.title()} sandwich")