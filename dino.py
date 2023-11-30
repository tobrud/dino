#%%
import random
import time

def intro():
    print("Du står midt i en juratidsskog, og plutselig ser du en sulten dinosaur!")

def choose_action():
    print("Hva vil du gjøre?")
    print("1. Løp for livet!")
    print("2. Prøv å gjemme deg.")
    return input("Skriv inn valg (1 eller 2): ")

def result(action):
    if action == "1":
        print("Du løper så fort du kan, men dinosauren er raskere. Du blir spist opp!")
    elif action == "2":
        print("Du prøver å gjemme deg bak et tre. Dinosauren ser deg ikke og går forbi. Du overlever!")

def play_dinosaur_game():
    intro()
    time.sleep(1)
    action = choose_action()
    result(action)

if __name__ == "__main__":
    play_dinosaur_game()



# %%
