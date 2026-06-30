questions = [
    "What is the capital of India?\na) Mumbai\nb) New Delhi\nc) Kolkata\nd) Chennai",
    "Which programming language is known for simplicity?\na) Java\nb) C++\nc) Python\nd) Kotlin",
    "What is 5 + 7?\na) 10\nb) 11\nc) 12\nd) 13"
]

answers = ["b", "c", "c"]
score = 0

for i in range(len(questions)):
    print("\n" + questions[i])
    user_ans = input("Your answer (a/b/c/d): ").lower()
    if user_ans == answers[i]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {answers[i]}.")

print(f"\nQuiz Finished! Your total score is: {score}/{len(questions)}")