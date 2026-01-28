questions=("What is the capital of France?","What is the largest planet in our solar system?","Who painted the Mona Lisa?")
options=(("A) Paris","B) London","C) Berlin","D) Madrid"),("A) Earth","B) Jupiter","C) Saturn","D) Mars"),("A) Vincent van Gogh","B) Pablo Picasso","C) Leonardo da Vinci","D) Claude Monet"))
answers=("A","B","C")
guesses=[]
score=0
question_num=0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A, B, C, or D): ")
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer was: {answers[question_num]}")
    question_num+=1
print("---------------")
print("     Results   ")
print("---------------")
print("answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()
print("Guesses:",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(f"Your score is: {score}%")
