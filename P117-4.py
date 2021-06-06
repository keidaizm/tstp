answer = ["1","3","7"]
while True:
    print("Guess anser number from 1 to 9.")
    a = input("Input number:")
    if a in answer:
        print("You got it!!")
        break
    print("Try another number!!\n")
