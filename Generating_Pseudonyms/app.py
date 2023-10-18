import name_list
import random

print(" Hello stanger do you want to play some games? lets generate some silly names for you")
play = input("Enter Y to play or N not to play: ")
if play.lower() == 'n':
    print(" you are no fun")
elif play.lower() == 'y':
    play = True
    while (play):
        print("i think i like you lets play")
        generate = input("type start to generate a name: ")
        if generate == "start":
            first_name = random.choice(name_list.first_names)
            last_name = random.choice(name_list.last_names)
            print(f"your name is {first_name} {last_name}")
            print("its a funny name right?")
            play_again = input("want to play again? [y/n]")
            if play_again == "y":
                play = True
            else:
                print("alright goodbye player")
                play = False
else:
    print("oh no, your selected option is not avialable")