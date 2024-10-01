current_users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
new_users = ['alice', 'Frank', 'George', 'bob', 'Hank']

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"Username '{new_user}' is already taken.")
    else:
        print(f"Username '{new_user}' is available.")
