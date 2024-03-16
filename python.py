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
    cars = ["Ferrari_GTC4Lusso", "Lamborghini_Huracan", "Bugatti_Veyron", "McLaren_Speedtail", "Porsche_911_Roadster", "Aston_Martin_Vantage", "Koenigsegg_Agera", "Pagani_Imola", "Ferrari_SF90_Stradale", "Lamborghini_Aventador", "Bugatti_Chiron", "McLaren_P1", "Porsche_918_Spyder", "Aston_Martin_Valkyrie", "Koenigsegg_Jesko", "Pagani_Huayra", "RollsRoyce_Boatail"]

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


