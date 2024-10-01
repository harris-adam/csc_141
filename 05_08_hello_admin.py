usernames = ['admin', 'user1', 'user2']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")  # Output
    else:
        print(f"Hello {username}, thank you for logging in.")
