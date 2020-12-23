import webbrowser
import time


while True:
    Q1 = float(input("What is 9 + 10: "))
    if Q1 == 19:
        print("Nice, you are correct")
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

            
    Q2 = float(input("What is 17 + 71: "))
    if Q2 == 88:
        print("Nice, you are correct")
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')



    Q3 = float(input("What is 11 * 62: "))
    if Q3 == 682:
        print("Nice, you are correct")
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')



    Q4 = str(input("What is sin(5 × π - 6) × 62: "))
    if Q4 == 'cum':
        print("Wow... You won.. Eh, congrats!")
    else:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    time.sleep(1)
    print('Program will close in 3 seconds')
    time.sleep(3)
    print('Good night!')
    time.sleep(1)
    break