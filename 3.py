import random
print("We're going to play a guess-game but you've got to enter a range!")
a = int(input("From what: "))
b = int(input("to what: "))
pick_of_the_machine = random.randint(a, b)
print("Alright, I picked a number between {} and {}, now it's your turn!".format(a, b))
player = int(input("I think you've chosen: "))
while player != pick_of_the_machine:
    if player < pick_of_the_machine:
        print("Oh, you're so close but my pick was bigger.")
        player = int(input("Alright then, this time I'll find it: "))
    elif player > pick_of_the_machine:
        print("Oh, you're really close but my pick was smaller.")
        player = int(input("Alright then, this time I'll find it: "))
print("Congratulations! You've guessed my pick right, it was: ", player)
