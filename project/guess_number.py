import random
secret_number = random.randint(1 , 100)

attempt = 0


while True:
    guess  = int(input("Guess The Number 1 to 100 : "))
    attempt =+ 1

    if guess > secret_number:
        print("Too High !!!")
    elif guess < secret_number:
        print("Too Low !!!")
    else:
        print("Congratulation you did it !!!")