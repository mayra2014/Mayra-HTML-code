import random
def quiz():
    
    questions = {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
   },  {
        "question": "What is 8x9?",
        "options": ["A) 67", "B) 71", "C) 72", "D) 89"],
        "answer": "C"
   },  {
        "question": "Does it hurt to die?",
        "options": ["A) Yes", "B) No", "C) Maybe", "D) everyone dies eventually"],
        "answer": "D,C"
    },  {
        "What is 9 x 7?": "63",
        "What is the capital of Morroco?": "Rabat",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who is the president of the United States in 2024?": "Joe Biden",
        "Do you like donald trump?": "No"
    }
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Please enter the letter of your answer: ").upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
print()
quiz()