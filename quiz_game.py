# Python Quiz Game

# tuple of questions
questions = (
    "What is the output of print(2 ** 3)?",
    "Which keyword is used to define a function in Python?",
    "What data type is used to store True or False values?",
    "Which of the following is an immutable data type?",
    "What does the len() function do?"
)

# tuple of options 
options = (
    ("A. 6", "B. 8", "C. 9", "D. 5"),
    ("A. func", "B. define", "C. def", "D. function"),
    ("A. int", "B. str", "C. bool", "D. list"),
    ("A. List", "B. Set", "C. Tuple", "D. Dictionary"),
    ("A. Returns length", "B. Adds numbers", "C. Prints data", "D. Exits program")
)

# tuple of answers 
answers = ("B", "C", "C", "C", "A")

# guesses
guesses = []

# game variables
score = 0

# question count
question_num = 0

# loop through questions
for question in questions:
  print("------------------------------------------------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  
  guess = input("Enter your answer (A, B, C, or D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("Correct! ^-^")
  else:
    print(f"Incorrect! >_<")
    print(f"{answers[question_num]} is the correct answer!")
  question_num += 1

print("------------------------------------------------------------")
print("                        RESULTS                             ")
print("------------------------------------------------------------")

print("answer:  ", end=" ")
for answer in answers:
  print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
  print(guess, end=" ")
print()

score= int(score/ len(questions) * 100)
print(f"Your score is {score}%.")
