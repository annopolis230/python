correctAnswers = ['A','B','D','A','B','B','B','C','C','D'];
studentAnswers = [];
studentDictionary = {};


def gatherInput(iteration):
    studentID = int(input("Enter your Student ID: "));
    answerChoices = ['A','B','C','D'];
    numCorrect = 0;
    for i in range(10):
        while True:
            questionAnswer = input("Your answer to question: ");
            if questionAnswer.upper() not in answerChoices:
                print("Enter an answer A through D");
            else:
                studentAnswers.append(questionAnswer);
                break;
    for i in range(10):
        if studentAnswers[i] == correctAnswers[i]:
            numCorrect+=1;
    studentAnswers.clear();
    studentDictionary.update({studentID: numCorrect});
    
continueLoop = True;
iteration = 0;

while continueLoop:
    gatherInput(iteration);
    iteration+=1;
    doContinue = str(input("Would you like to continue? Enter Y or N."))
    if doContinue.upper() == "N":
        break;

print(studentDictionary);

