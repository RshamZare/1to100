# Dice Roller Simulator

users_answer = str(input("Do you want to roll the dice?y/n"))


if users_answer == "y":
    times = int(input("how many times?"))
    for x in random.range(1,6):
        print(x)

else:
    print("sucker")


