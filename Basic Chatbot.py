# Rule based CHATBOT 

import datetime

name=input("enter your name:")
presentHour= datetime.datetime.now().hour 


if 3<= presentHour <=11:
    print("Good morning,",name)
elif 11< presentHour <=16:
    print("Good afternoon,",name)
else :
    print("Good evening,", name)



print("Hello!, welcome to a simple rule based chatbot")
print("You can ask me basic questions, type 'exit' to exit from the chatbot")

responses={
    "hello": "Hi!, welcome. How can i help you?" ,
    "how are you": "I am great. Thank You",
    "who are you": " I am a smart AI chatbot.",
    "motivate me": "Keep going. Every bug of your project makes you a better developer. ",
    "what is the capital of india":" New Delhi is the capital of India.",
    "who is the current prime minister of india":"The current pm of India is Narendra Modi",
    "bye": "Goodbye, have a great day!",
    }

def BotResponse(UserQuestion):
    UserQuestion=UserQuestion.lower()
    for eachKey in responses:
        if eachKey in UserQuestion:
            return responses[eachKey]
    
    return " I am not able to answer that yet. I will learn it soon!"


while True:
    userInput=input("Please ask your question:")
    reply=BotResponse(userInput)
    print("Bot response:",reply)

    if "exit" in userInput.lower():
        print("Exitting from the chatbot...See you soon!")
        break


