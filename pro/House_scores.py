# Initialize house scores
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Question 1
print("Q1) Do you like Dawn or Dusk?")
print("   1) Dawn")
print("   2) Dusk")
answer1 = int(input("Enter your answer (1 or 2): "))

if answer1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

# Question 2
print("\nQ2) When I’m dead, I want people to remember me as:")
print("   1) The Good")
print("   2) The Great")
print("   3) The Wise")
print("   4) The Bold")
answer2 = int(input("Enter your answer (1, 2, 3, or 4): "))

if answer2 == 1:
    hufflepuff += 2
elif answer2 == 2:
    slytherin += 2
elif answer2 == 3:
    ravenclaw += 2
elif answer2 == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# Question 3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("   1) The violin")
print("   2) The trumpet")
print("   3) The piano")
print("   4) The drum")
answer3 = int(input("Enter your answer (1, 2, 3, or 4): "))

if answer3 == 1:
    slytherin += 4
elif answer3 == 2:
    hufflepuff += 4
elif answer3 == 3:
    ravenclaw += 4
elif answer3 == 4:
    gryffindor += 4
else:
    print("Wrong input.")

# Print final scores
print("\nHouse Scores:")
print("Gryffindor:", gryffindor)
print("Ravenclaw:", ravenclaw)
print("Hufflepuff:", hufflepuff)
print("Slytherin:", slytherin)

# Bonus: Determine the house with the highest score
house_scores = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}

max_score = max(house_scores.values())
winning_houses = [house for house,
                  score in house_scores.items() if score == max_score]

if len(winning_houses) == 1:
    print("\nThe house with the most points is:", winning_houses[0])
else:
    print("\nIt's a tie between:", ", ".join(winning_houses))
