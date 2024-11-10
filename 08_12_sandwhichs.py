def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('ham', 'cheese')
make_sandwich('bacon', 'lettuce', 'tomato', 'avocado')