import questions
import random

#setting up the basics with a welcome text, a counter for the questions
def game(questionCounter):
    print("Welcome to my Game!")
    print("Are you Ready? Y/N" )
    inputStart = input()
    if inputStart == "Y" or inputStart == "y":
        while questionCounter <= 10:
            if questionCounter != 9:
                print("Here comes the question:")
                questionAnswerPair = questions.questionAnswers[random.randint(0,9)]
                questionCorrectAnswer = list(questionAnswerPair.keys())
                print(questionCorrectAnswer[0])
                answers = []
                answers = list(questionAnswerPair.values())[0]
                print("1: {A1}, 2: {A2}, 3: {A3}, 4: {A4}".format(A1 = answers[0], A2 = answers[1], A3 = answers[2], A4 = answers[3]))
                inputAnswer = int(input())
                if inputAnswer >= 1 and inputAnswer <= 4:
                    if inputAnswer == questionCorrectAnswer[1]:
                        questionCounter += 1
                        print("Correct!")
                        game(questionCounter)
                    else:
                        print("Not correct! The right answer would have been \"{answer}\". Thank you for playing and good luck next time!".format(answer = questionCorrectAnswer[1]))
                        break
                else:
                    print("Please select a number between 1 - 4!")
            else:
                print("You're doing amazingly! You're about to be a millionaire!")
                print("Here comes the final question:")
                questionAnswerPair = questions.questionAnswers[questionCounter]
                questionCorrectAnswer = list(questionAnswerPair.keys())
                print(questionCorrectAnswer[0])
                answers = []
                answers = list(questionAnswerPair.values())[0]
                print("1: {A1}, 2: {A2}, 3: {A3}, 4: {A4}".format(A1 = answers[0], A2 = answers[1], A3 = answers[2], A4 = answers[3]))
                inputAnswer = int(input())
                if inputAnswer >= 1 and inputAnswer <= 4:
                    if inputAnswer == questionCorrectAnswer[1]:
                        print("Congratulations! With your wisdom and knowledge you won 1 Million $! Have fun with it!")
                        break
            break