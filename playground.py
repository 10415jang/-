
def print_times_table(number):
    print(number, "*", 1, "=", number * 1)
    print(number, "*", 2, "=", number * 2)
    print(number, "*", 3, "=", number * 3)
    print(number, "*", 4, "=", number * 4)
    print(number, "*", 5, "=", number * 5)
    print(number, "*", 6, "=", number * 6)
    print(number, "*", 7, "=", number * 7)
    print(number, "*", 8, "=", number * 8)
    print(number, "*", 9, "=", number * 9)

#test
import random
import time

def updown():
    result = random.randrange(1, 101)
    print("WELCOME TO UP DOWN")
    while True:
        user_input= int(input("값을 입력하세요:"))
        if user_input == result:
            print("정답입니다.")
            break
        else:
            if user_input<result:
                print("up")
            else:
                print("down")
updown()



















def stop_watch():
    print("WELCOME TO STOPWATCH")
    #random 초를 제공하면 ex)7초
    start= time.time()
    print("시작하고 7초후에 c키를 누르세요")
    user_input = str(input("c키를 누르세요:"))
    end = time.time()
    if user_input=="c":
        print(end-start)
        if 6.7<=end-start<=7.3:
            print("성공입니다")
        else:
            print("실패입니다")



