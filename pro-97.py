import random
name=input('Enter your Name here : ')
chances=3
ans=0
a=1
print('Hi!"',name,'"\nWelcome to number Guessing game\nYou will only have 3 chances to guess the number')
num=random.randint(1,10)
ans=int(input('Guess the number between 1 & 10 : '))
while a == 1 :
    if ans<11:
        if ans!=num:
            if chances!=1:
                chances=chances-1
                print('Wrong guess \nTry again\n You have only',chances,'guesses left')
                ans= int(input('Guess the number between 1 & 10 : '))
            else:
                print('!! You lost the Game !!\nThe correct number was',num)
                exit()
        else :
            print('!! You guessed correctly !!\n Number of chances:',chances)
            exit()
    else :
        print('Please give a valid number')