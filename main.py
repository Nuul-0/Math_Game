import webbrowser
from time import sleep

def correct_ans_res():
    print("Nice, you are correct")
def wrong_answer():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

def set_answers():
    global QA
    QA = []
    going = True
    while going:
        key = input("Question: ")
        QA.append(key)
        value = input("Answer: ")
        QA.append(value)
        i = 1
        sleep(0.5)
        print("Question added")
        i+1
        add_more = input("Do you want to add another question? ")
        if add_more == "Yes" or add_more == "yes" or add_more == 1:
            going = True
        else:
            going = False     


def main():
    run = True
    sleep(1)
    for i in range(10):
        print(" ")
    sleep(1)
    print("Let the game beginn!")
    sleep(1)
    for i in range(2):
        print(" ")
    while run:
        n = 0
        d = 0
        for i in range(len(QA)):
            if d % 2 == 0:
                x = input(QA[n])
                if x == QA[n+1]:
                    correct_ans_res()
                else:
                    wrong_answer()
                n += 2
                d += 1
            else:
                d += 1

        run = False

        sleep(1)
        print('Program will close in 3 seconds')
        sleep(3)
        print('Good night!')
        sleep(1)
        run = False

set_answers()
main()