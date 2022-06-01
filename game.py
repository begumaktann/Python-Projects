#how to play
#

from wordle import Wordle
from colorama import Fore, Back,Style,init
init(autoreset=True)

def game_mode():
    lang=input(f"Please choose a language:English/Turkish\n{Fore.BLUE}Press 1 for English, 2 for Turkish\n{Fore.RESET}Lütfen bir dil seçiniz\n{Fore.BLUE}İngilizce için 1, Türkçe için 2'ye basın\n")
    mode=""
    if lang=="1":
        mode = input(f"Please choose a game mode:\nWordle/Quordle\n{Fore.BLUE}Press 1 for Wordle, 2 for Quordle\nHow to play(3)\n")
        if mode == "1":
            print(f"{Fore.LIGHTMAGENTA_EX}You are playing Wordle")
            letters = input(f"how many lettered words?\n{Fore.BLUE}4,5,6\n")
            if letters == "4":
                print(f"\n{Fore.LIGHTMAGENTA_EX}4-lettered Wordle")
                return "4wordle","en"
            elif letters == "5":
                print(f"\n{Fore.LIGHTMAGENTA_EX}5-lettered Wordle")
                return "5wordle","en"
            elif letters == "6":
                print(f"\n{Fore.LIGHTMAGENTA_EX}6-lettered Wordle")
                return "6wordle","en"

        elif mode == "2":
            print("You are playing Quordle")
            letters = input("how many lettered words?\n4,5,6\n")
            if letters == "4":
                print(f"\n            4-lettered Quordle")
                return "4quordle","en"
            elif letters == "5":
                print("\n            5-lettered Quordle")
                return "5quordle","en"
            elif letters == "6":
                print("\n            6-lettered Quordle")
                return "6quordle","en"

        elif mode == "3":
            print(
                f"\nYour challenge is to guess a five-letter word in six attempts.\nEach time you guess, you're told which of your chosen letters are in the target word, and whether they are in the right place.\nFor Example: \nYour Guess:{Fore.RED}LIME{Fore.RESET} Secret Word:{Fore.RED}KILO\n{Fore.YELLOW}L{Fore.GREEN}I{Fore.BLACK}ME\nThe letters that are in the secret word and in the right position are highlighted with green.\nIf the letter is in the word but it's not in the right position, it's yellow. Black is for letters that are not in the word.\n")
            game_mode()
        else:
            print(f"{Fore.RED}Your answer should be 1/2")


    elif lang=="2":
        mode = input(f"Lütfen bir oyun modu seçin:\nWordle/Quordle\nWordle için 1, Quordle için 2\nNasıl oynanır(3)\n")
        if mode == "1":
            print("Wordle oynuyorsunuz")
            letters = input("Kaç harfli kelimeler olsun?\n4,5,6\n")
            if letters == "4":
                print(f"\n4-harfli Wordle")
                return "4wordle","tr"
            elif letters == "5":
                print("\n5-harfli Wordle")
                return "5wordle","tr"
            elif letters == "6":
                print("\n6-harfli Wordle")
                return "6wordle","tr"

        elif mode == "2":
            print("Quordle oynuyorsunuz")
            letters = input("Kelimeler kaç harfli olsun?\n4,5,6\n")
            if letters == "4":
                print(f"\n            4-harfli Quordle")
                return "4quordle","tr"
            elif letters == "5":
                print("\n            5-harfli Quordle")
                return "5quordle","tr"
            elif letters == "6":
                print("\n            6-harfli Quordle")
                return "6quordle","tr"

        elif mode == "3":
            print(
                f"\nOyunun amacı 6 denemede 5 harfli gizli kelimeyi bulmaktır.\nHer denemede harflerin yeri doğru mu, o harf kelimede yer alıyor mu gösterilir.\nÖrneğin: \nTahmin:{Fore.RED}OYUN {Fore.RESET}Secret Word:{Fore.RED}UNUT\n{Fore.BLACK}O{Fore.BLACK}Y{Fore.GREEN}U{Fore.YELLOW}N")
            game_mode()
        else:
            print(f"{Fore.RED}Your answer should be 1/2")
            game_mode()
    else:
        print(f"{Fore.RED}Your answer should be 1/2")
        game_mode()





def game(mode,lang):
    if lang=="en":
        if mode == "4wordle":
            wordlee(letters=4,lang="en")
        elif mode == "5wordle":
            wordlee(letters=5,lang="en")
        elif mode == "6wordle":
            wordlee(letters=6,lang="en")
        elif mode == "4quordle":
            quordle(letters=4,lang="en")
        elif mode == "5quordle":
            quordle(letters=5,lang="en")
        elif mode == "6quordle":
            quordle(letters=6,lang="en")
    elif lang=="tr":
        if mode == "4wordle":
            wordlee(letters=4,lang="tr")
        elif mode == "5wordle":
            wordlee(letters=5,lang="tr")
        elif mode == "6wordle":
            wordlee(letters=6,lang="tr")
        elif mode == "4quordle":
            quordle(letters=4,lang="tr")
        elif mode == "5quordle":
            quordle(letters=5,lang="tr")
        elif mode == "6quordle":
            quordle(letters=6,lang="tr")



def wordlee(letters=5,lang="en"):
    wordlex=Wordle(letters,lang)
    wordlex.wordle(letters,lang)




def quordle(letters,lang="en"):
    wordle=Wordle(letters,lang)
    words=[]
    for i in range(4):
        words.append(Wordle(letters,lang,mode="quordle"))
    while words[0].can_attempt() or words[1].can_attempt() or words[2].can_attempt() or words[3].can_attempt():
        #print(" ",end="")
        guess = input(f"  Your Guess:").upper()
        if len(guess) != letters:
            print(f"your guess should be {letters} characters long")
            continue
        if guess not in wordle.word_list:
            print("                                                                                                ",
                  end="")
            #print("enter a valid word")
            continue
        for word in words:
            #print(word.secret_word)
            if not word.solved():
                word.attempt(guess)


            color_dict = word.color_of_letter()
            print("│",end="")
            for key, value in color_dict.items():

                if value == "a":
                    print(f"{Fore.GREEN} {key[0]}", end=" ")
                elif value == "y":
                    print(f"{Fore.YELLOW} {key[0]}", end=" ")
                else:
                    print(f"{Fore.BLACK} {key[0]}", end=" ")
            print("", end="│       ")
            if word.solved():
                continue
        if words[0].solved() and words[1].solved() and words[2].solved() and words[3].solved():
            print("You've completely solved the puzzle")
        elif  not(words[0].can_attempt() or words[1].can_attempt() or words[2].can_attempt() or words[3].can_attempt()):
            print("\nYou failed to solve the puzzle")
            print(f"The secret words were:{Fore.RED}{words[0].secret_word} {words[1].secret_word} {words[2].secret_word} {words[3].secret_word}")
        else:
            continue











mode,lang=game_mode()
game(mode,lang)





