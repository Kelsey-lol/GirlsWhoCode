# --- Define your functions below! ---
def intro():
    print("I am a robot...")
    print("  _ _")
    print(" [O_O] ")
    print(" -[ ]-")
    print("  l l ")
    print("   ")
def process_input(answer):
    if is_valid_input(answer):
        say_greeting()
    else:
        say_default()

def is_valid_input(word):
    valid = ["hi", "hello", "sup", "hey", "yo"]
    if word in valid:
        return True
    else:
        return False

def say_greeting():
    print("Hello there me friend ^_^")
def say_default():
    print("Wut? -_-")

def ask():
    print("umm...")
    print("Do you like strawberries or watermelones?")
def process1_input(answer):
    if answer == "strawberries":
        say_yay()
    else:
        say_wut()
def say_yay():
    print("Good, you can be my friend.")
def say_wut():
    print("It's okay, I guess.")

def game():
    print("   ")
    print("Do you want to play a guessing game?")
def process2_input(answer):
    if answer == "yes":
        say_yes()
    else:
        say_no()
def say_yes():
    print("Ok!!")
    print("...")
    print("......")
    print("hahaha... ^.^ ")
    print("It seems I don't know any games")

def say_no():
    print ("Lol, its okay. I don't know any.")
    print("   ")
    print("(O.O)")
    print("<( )>")
    print(" l l ")

def go():
    print("   ")
    print("You should get going now.")
    print ("* * * * * * * * * * * * * * *")
    print (" * *   * * * * * * * *   * * ")
    print ("* *     * * * * * * *     * *")
    print (" * * * * * * * * * * * * * * ")
    print ("* * * * * * * * * * * * * * *")
    print (" * * * * *         * * * * * ")
    print ("* * * * * * * * * * * * * * *")
def process3_input(answer):
    say_k()
def say_k():
    print("Bye")
# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)
        break
    ask()
    while True:
        answer = input("(What will you say?) ")
        process1_input(answer)
        break
    game()
    while True:
        answer = input("(What will you say?)")
        process2_input(answer)
        break
    go()
    while True:
        answer = input("(What will you say?)")
        process3_input(answer)
        break
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
