quiz={
    "question1":{
        "question":"What is the capital of France",
        "answer":"Paris"
        },
    "question2":{
        "question":"What is the capital of germany",
        "answer":"Berlin"    
    },
    "question3":{
        "question":"What is the capital of Italy",
        "answer":"Rome"
    },
    "question4":{
        "question":"What is the capital of Spain",
        "answer":"Madrid"
        },
    "question5":{
        "question":"What is the capital of India",
        "answer":"Delhi"    
    },
    "question6":{
        "question":"What is the capital of bangladesh",
        "answer":"Dhaka"
    },  
}
score=0
for key, value in quiz.items():
    print(value['question'])
    answer=input("Answer? ")
    if answer.lower()==value["answer"].lower():
        print('Correct')
        score=score+1
        print("Your score is ", str(score))
    else:
        print("Wrong")
        print("The answer is: "+ value['answer'])
        