import random
import time


def exit_game():
    option = input("Are you sure you want to exit? Yes or No\n")
    while option.lower() == 'no':
        if option.lower() == 'no':
            start_game()
        elif option.lower() == 'yes':
            print("Exit successful")
            break

    print("You did not enter the right option")
    exit_game()


def start_game():
    print("Welcome to the adventure game")
    time.sleep(3)
    start = int(input("Press 1 to start the game\n"))
    if start == 1:
        print("loading...")
        time.sleep(3)
        print("\n")
        print_intro()
        game_body()
        enemyApproach()
        fight()
    else:
        print("Game exited")


def print_pause(one, two, three, four):
    print(one)
    time.sleep(2)
    print(two)
    time.sleep(2)
    print(three)
    time.sleep(2)
    print(four)


def print_intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.",
                "Rumor has it that a wicked fairy is somewhere around here, "
                "and has been terrifying the nearby village",
                "There is a house in the middle of the field of the river.",
                "There is also a cave nearby.")


def game_body():
    enter_option = int(input("Enter 1 to knock on the door of the house.\n"
                             "Enter 2 to peer into the cave.\n"
                             "What would you like to do? \n"
                             ))
    while 0 < enter_option < 2:
        if enter_option == 1:
            enter_house()
        elif enter_option == 2:
            enter_cave()

    print("You did not enter the right option\n")
    time.sleep(2)
    game_body()


def enter_house():
    print_pause("You are in the house",
                "There are weapons in the house you could use use to fight",
                "", ""
                )
    pick_weapons()


def pick_weapons():
    weapon = input("Pick a weapon of a your choice\n"
                   "1 = knife\n"
                   "2 = axe\n"
                   "3 = gun\n"
                   "4 = dagger\n"
                   )
    weapons = ["knife", "axe", "gun", "dagger"]
    if weapon == '1':
        print("You picked knife")
    elif weapon == '2':
        print("You picked axe")
    elif weapon == '3':
        print("You picked gun")
    elif weapon == '4':
        print("You picked dagger")
    else:
        print("You have not picked any weapon. You have to pick one")
        pick_weapons()


def enter_cave():
    print("You are inside the cave")


def enemyApproach():
    listOfEnemies = ["pirate", "monster", "Bear", "Witch", "wizard",
                     "vampire", "undead", "snake", "giant-monkey"]
    enemy_tag = random.randint(1, 8)
    enemy = listOfEnemies[enemy_tag]
    print(enemy, "approaches. You have to fight and kill it")


def fight():
    state = random.randint(1, 2)
    if state == 1:
        print("You won the fight!!!")
        field()
    else:
        print("You lose!!!")
        time.sleep(3)
        game_over()


def field():
    time.sleep(3)
    print("Runnning back to the field")
    time.sleep(3)


def game_over():
    ans = input("Would you like to play again? (y/n)\n")
    while ans.lower() == 'y':
        if ans.lower() == 'y':
            start_game()
        elif ans.lower() == 'n':
            exit_game()
    print("You did not enter the right option")
    game_over()
    # if ans.lower() == 'y':
    #     start_game()
    # else:
    #     exit_game()


start_game()
