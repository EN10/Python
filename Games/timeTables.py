import random
import time
second_number = 2
score = 0
while True:
    number_1 = random.randint(1,second_number)
    number_2 = random.randint(1,second_number)
    start_time = time.time()
    question = int(input("what is "+ str(number_1)+ " times "+ str(number_2)+ ": "))
    end_time = time.time()
    time_difference = end_time - start_time
    time_difference = int(time_difference)
    if time_difference < 5 and question == (number_1 * number_2):
        print("you got it right")
        score = score + 1
        second_number = second_number + 2
    elif time_difference > 5:
        print("you ran out of time")
        print("your score is: "+ str(score))
        break
    else:
        print("you got it wrong")
        print("your score is: "+ str(score))
        break
