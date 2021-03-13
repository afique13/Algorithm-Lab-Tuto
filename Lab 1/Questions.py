import random

def calculateAge():
    name = input('Enter your name: ')
    age = input('Enter your age: ')
    years = 2021 + (100 - int(age))
    print('You will turn 100 in',years)
    
def evenOdd():
    number = input('Enter a number: ')
    input_num = int(number)
    if input_num%2==0:
        print('Number is even')
    else:
        print('Number is odd')
        
def numList():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for x in a:
        if(x<5):
            print(x, end=' '),

def Duplicates():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for x in a:
        for y in b:
            if(x == y):
                print(x, end=' ')
                break

def Palindrome():
    word = input('Enter a word: ')
    count = len(word);
    pal = ""
    for x in range(len(word), 0, -1):
        count -= 1
        pal+=word[count]
    if(pal == word):
        print(pal, 'is a palindrome') 
    else:
        print(word, 'is not a palindrome')  
        
def randomNumber():
    rando = random.randint(1,9)
    num = input('Guess the number: ')
    print('The answer is', rando)
    if(int(num)==rando):
        print('You guessed correctly!')
    elif(int(num)>rando):
        print('You guessed too high')
    else:
        print('You guessed too low')
        
def Fibonacci():
    count = input('How many numbers would you like to generate? ')
    seq = 1
    seq_bfr = 0
    flag = 0
    for x in range(0,int(count),1):
        print(seq, end=' ')
        if(x==0):
            seq_bfr = 1
            continue
        elif(x==1):
            flag = 1
            seq += 1
        if(x>1):    
            seq = flag+seq_bfr
        seq_bfr = flag
        flag = seq
           
funcs = [calculateAge,evenOdd,numList,Duplicates,Palindrome,randomNumber,Fibonacci]
n = input('Which function do you want to run? ')
funcs[int(n)]()