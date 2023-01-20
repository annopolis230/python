correctAnswers = ['A','B','D','A','B','B','B','C','C','D'];

def gatherInput(iteration):
    studentAnswers = [];
    studentID = int(input("Enter your Student ID: "));
    while True:
        answerChoices = ['A','B','C','D'];
        questionAnswer = input("Your answer to question ",iteration,": ");
        if questionAnswer.upper() or questionAnswer.lower() not in answerChoices:
            print("Enter an answer A through D");
        else:
            studentAnswers[iteration] = questionAnswer;
            break;

for i in range(10):
    gatherInput(i);
