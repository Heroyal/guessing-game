from random import randint
def main():
    num=randint(1,10)
    a=0
    while a<5:
        guess=input('Plaease give a number between on and ten: ')
        if int(guess)==num:
            print('Yor are right!')
            break
        else:
            print('Sorry,that\'s wrong,please guess again!')
            a+=1
if __name__=='__main__':
    main()
