import random
from colorama import Fore, Back,Style,init


def read_words(lang):
    if lang=="en":
        file = open(r"C:\Users\HP\PycharmProjects\wordle\wordlist.txt", "r")
        words_str = file.read().upper()
        words_list = words_str.split("\n")
        return words_list
    elif lang=="tr":
        file1 = open(r"C:\Users\HP\PycharmProjects\wordle\tr.txt", "r", encoding="utf8")
        file2=open(r"C:\Users\HP\PycharmProjects\wordle\trr.txt", "r", encoding="utf8")
        words_str1 = file1.read().upper()
        words_list1 = words_str1.split("\n")
        words_str2 = file2.read().upper()
        words_list2 = words_str2.split(", ")
        words_list=words_list1+words_list2
        #print(words_list2)
        #print("s"if "bela" in words_list2 else "b")
        return words_list




class Wordle:

    def __init__(self,num,lang,mode="wordle"):
        self.words_list=read_words(lang)
        self.mode=mode
        self.num = num
        self.word_list = []
        self.attempts=[]
        for word in self.words_list:
            if len(word) == self.num:
                self.word_list.append(word)
        self.secret_word = random.choice(self.word_list)
        self.max_attempts = self.maximum_attempts()

    def maximum_attempts(self):
        if self.mode=="wordle":
            return len(self.secret_word) + 1
        elif self.mode=="quordle":
            return (2*len(self.secret_word))-1


    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def solved(self):
        if len(self.attempts)>=1 and self.attempts[-1]==self.secret_word:
            return True
        else:
            return False

    def can_attempt(self):
        return self.max_attempts-len(self.attempts) > 0 and not self.solved()

    def color_of_letter(self):
        colors={}
        for i in range(len(self.secret_word)):
            if self.attempts[-1][i]==self.secret_word[i]:
                colors[self.attempts[-1][i]+str(i)]="a"
            elif self.attempts[-1][i] in self.secret_word:
                colors[self.attempts[-1][i]+str(i)] = "y"
            else:
                colors[self.attempts[-1][i]+str(i)] = "w"
        return colors

    def wordle(self,letters,lang):
        if lang=="en":
            while self.can_attempt():
                guess = input("     Your Guess:").upper()
                if len(guess) != letters:
                    print(f"your guess should be {letters} characters long")
                    continue
                if guess not in self.word_list:
                    print("enter a valid word",end="  ")
                    continue

                self.attempt(guess)
                color_dict = self.color_of_letter()
                # print(color_dict)
                print("│",end="")
                for key, value in color_dict.items():
                    if value == "a":
                        print(f"{Fore.GREEN} {key[0]}", end=" ")
                    elif value == "y":
                        print(f"{Fore.YELLOW} {key[0]}", end=" ")
                    else:
                        print(f"{Fore.BLACK} {key[0]}", end=" ")

                print(f"│     You have {self.max_attempts - len(self.attempts)} attempts left.",end="   ")

                if self.solved():
                    print("\nYou've solved the puzzle.")
                elif self.can_attempt():
                    continue
                else:
                    print("\nYou failed to solve the puzzle!")
                    print(f"The secret word was: {self.secret_word}")
        elif lang =="tr":
            while self.can_attempt():
                guess = input("\nTahmininiz:").upper()
                if len(guess) != letters:
                    print(f"Tahmininiz {letters}karakterden oluşmalı")
                    continue
                if guess not in self.word_list:
                    print("geçerli bir kelime girin")
                    continue

                self.attempt(guess)
                color_dict = self.color_of_letter()
                # print(color_dict)
                for key, value in color_dict.items():
                    if value == "a":
                        print(f"{Fore.GREEN} {key[0]}", end=" ")
                    elif value == "y":
                        print(f"{Fore.YELLOW} {key[0]}", end=" ")
                    else:
                        print(f"{Fore.BLACK} {key[0]}", end=" ")

                print(f"     {self.max_attempts - len(self.attempts)} hakkınız kaldı.")

                if self.solved():
                    print("\nBulmacayı çözdünüz.")
                elif self.can_attempt():
                    continue
                else:
                    print("\nBulmacayı çözemediniz!")
                    print(f"Gizli kelime: {self.secret_word}")


"""

def read_words():
    file=open("wordlist.txt","r")
    words_str=file.read()
    words_list=words_str.split("\n")
    four_lettered=[]
    five_lettered=[]
    six_lettered=[]

    for word in words_list:
        if len(word)==4:
            four_lettered.append(word)
        elif len(word)==5:
            five_lettered.append(word)
        elif len(word)==6:
            six_lettered.append(word)
    """


