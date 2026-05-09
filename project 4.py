# ======================================
# General Knowledge Quiz Game
# Project 4
# ======================================

print("====================================")
print("     WELCOME TO THE QUIZ GAME")
print("====================================")
print()

# score variable
score = 0

# -----------------------------
# Question 1
# -----------------------------
print("Question 1")
print("What is the capital of France?")
answer1 = input("Your Answer: ").strip().lower()

if answer1 == "paris":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! The correct answer is Paris.")

print()

# -----------------------------
# Question 2
# -----------------------------
print("Question 2")
print("Which planet is known as the Red Planet?")
answer2 = input("Your Answer: ").strip().lower()

if answer2 == "mars":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! The correct answer is Mars.")

print()

# -----------------------------
# Question 3
# -----------------------------
print("Question 3")
print("Who invented Python programming language?")
answer3 = input("Your Answer: ").strip().lower()

if answer3 == "guido van rossum":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! The correct answer is Guido van Rossum.")

print()

# ======================================
# Final Score Section
# ======================================
print("====================================")
print("             QUIZ OVER")
print("====================================")

print(f"Your Final Score: {score}/3")

# Performance Message
if score == 3:
    print("Excellent! Perfect Score!")
elif score == 2:
    print("Great Job!")
elif score == 1:
    print("Good Try! Keep Practicing.")
else:
    print("Better Luck Next Time!")

print()
print("Thank you for playing the quiz game!")
