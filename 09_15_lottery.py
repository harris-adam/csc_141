lottery_numbers = [1, 2, 3, 4, 5, 'A', 'B', 'C', 'D', 'E']
winning_ticket = []

for _ in range(4):
    winning_ticket.append(choice(lottery_numbers))

print("The winning ticket is:", winning_ticket)


# Exercise 9-16: Lottery Analysis
my_ticket = [1, 'A', 3, 'D']
attempts = 0

while True:
    attempts += 1
    drawn_ticket = [choice(lottery_numbers) for _ in range(4)]
    if drawn_ticket == my_ticket:
        break

print(f"It took {attempts} attempts to win the lottery with ticket {my_ticket}.")