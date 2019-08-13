#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 06:03:35 2018

@author: Matheus Homrich, Thiago Mello
"""

### Configuraçao Inicial
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "palavras.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

lc = string.ascii_lowercase + "áéíóçãõ"
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""
    for letter in lc:
        if letter not in letters_guessed:
            available_letters+=letter
    return available_letters


# end of helper code

### Final da Configuraçao Inicial


### Início da Tarefa 1a
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
            
    return True 
### Final da Tarefa 1a


### Início da Tarefa 1b
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word=''
    for letter in secret_word:
        if letter in letters_guessed:
            word+=letter+' '
        else:
            word+='_ '
    return word
### Final da Tarefa 1b
    
### Início da Tarefa 2
### CODE START ###
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. !
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    '''
    contador=0 
    letters_guessed=''
    wrong_letters=''
    while (is_word_guessed(secret_word, letters_guessed) or (contador==6))==False:
        print(get_available_letters(letters_guessed))        
        print(get_guessed_word(secret_word, letters_guessed))
        print("\nLetras Erradas: "+wrong_letters)
        if contador==0:
            print('+----+ ')
            print('|   ')
            print('|  ')
            print('|   ')
            print('|  ')
            print('| ')
            print('=========')
        letra=''
        letra=input("Digite uma letra: ")
        letters_guessed+=letra
        if letra not in secret_word:
            contador+=1
            wrong_letters+=letra+''
        if contador==1:
            print('+----+ ')
            print('|  O ')
            print('|  ')
            print('|   ')
            print('|  ')
            print('| ')
            print('=========')
        if contador==2:
            print('+----+ ')
            print('|  O ')
            print('|  | ')
            print('|  | ')
            print('|   ')
            print('| ')
            print('=========')
        if contador==3:
            print('+----+ ')
            print('|  O ')
            print('| \| ')
            print('|  | ')
            print('|  ')
            print('| ')
            print('=========')
        if contador==4:
            print('+----+ ')
            print('|  O ')
            print('| \|/ ')
            print('|  | ')
            print('|  ')
            print('| ')
            print('=========')
        if contador==5:
            print('+----+ ')
            print('|  O ')
            print('| \|/ ')
            print('|  | ')
            print('| /  ')
            print('| ')
            print('=========')

            
    if is_word_guessed(secret_word, letters_guessed)==True:
        print("Você venceu!")
        print(get_guessed_word(secret_word, letters_guessed))
        
        
    if contador == 6:
        
        print("Você perdeu!")
        print('+----+ ')
        print('|  O ')
        print('| \|/ ')
        print('|  | ')
        print('| / \ ')
        print('| ')
        print('=========')
        print(secret_word)
### Final da Tarefa 2    



### Configuraçao e testes

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
print("Letras disponíveis : ", get_available_letters([]))


#Código para teste da tarefa 1a
#secret_word = 'astuto'
#letters_guessed = ['a', 'm', 'l', 'e', 'v']
#print("\nWord guessed?: ",is_word_guessed(secret_word, letters_guessed))
#letters_guessed = ['a', 'e', 'o', 't', 's', 'u']
#print("Word guessed?: ",is_word_guessed(secret_word, letters_guessed))
# Saída esperada:
###    Word guessed?:  False
###    Word guessed?:  True


### Código para teste da tarefa 1b
#secret_word = 'banana'
#letters_guessed = ['a', 'p', 'm', 'b']
#print(get_guessed_word(secret_word, letters_guessed))
#letters_guessed = ['a', 'p', 'm', 'b', 'n']
#print(get_guessed_word(secret_word, letters_guessed))
### Saída esperada:
###    'ba_ a_ a'
###    'banana'



### Teste do jogo 
hangman(choose_word(wordlist))



