import random
THE_GREAT_HANGMAN = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

def pick_car():
    cars = ["ferrari_gtc4lusso", "lamborghini_huracan", "bugatti_veyron", "mclaren_speedtail", "porsche_911_roadster", "aston_martin_vantage", "koenigsegg_agera", "pagani_imola", "ferrari_sf90_stradale", "lamborghini_aventador", "bugatti_chiron", "mclaren_p1", "porsche_918_spyder", "aston_martin_valkyrie", "koenigsegg_jesko", "pagani_huayra", "rollsroyce_boatail"]
    return random.choice(cars)

def display_car(car, guessed_letters):
    displayed_car = ""
    for letter in car:
        if letter in guessed_letters:
            displayed_car += letter
        else:
            displayed_car += "_"
    return displayed_car

def hangman():
    global kk
    car = pick_car()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_car(car, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in car:
            attempts -= 1
            kk=kk+1
            print(THE_GREAT_HANGMAN[kk])
            print("Incorrect guess. You have", attempts, "attempts left.")
            if attempts == 0:
                print("You've run out of attempts. The car was:",car)
                break
        else:
            print("Correct guess!")

        displayed_car = display_car(car, guessed_letters)
        print(displayed_car)

        if "_" not in displayed_car:
            print("Congratulations! You've guessed the car:",car)
            break
kk=0
hangman()