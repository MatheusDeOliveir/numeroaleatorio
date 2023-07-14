import os
import time
import math
from random import randint
NUMERO_SECRETO = randint(0, 101)


def verifica_num(num):
    if num == NUMERO_SECRETO:
        return True
    else:
        return False
        
def dica(num):
    print ("Você errou, mas ai vai uma dica... \n")
    if math.fabs(num - NUMERO_SECRETO) > 15:
        print ("Muito longe")
    elif math.fabs(num - NUMERO_SECRETO) < 15 and math.fabs(num - NUMERO_SECRETO)>10:
        print ("Perto")
    elif math.fabs(num-NUMERO_SECRETO) < 10:
        print ("Muito perto!!")
        



while True:
    print ("Tente adivinhar o número secreto entre 1 e 100... \n")
    escolha = input ("Digite 1 para Tentar \nDigite 2 para saber a resposta\n\n")
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            num = input ("Dê um palpite: ")
            if num.isdigit():
                num = int(num)
                if num >0 and num<101:
                    if verifica_num(num):
                        print ("Você acertou!! O número secreto é", NUMERO_SECRETO)
                        break
                    else:
                        dica(num)
                        time.sleep(3)
                        os.system('cls')
                        continue
            else:
                print ("Palpite inválido...")
                time.sleep(3)
                os.system('cls')
                continue
        elif escolha ==2:
            print (f"A resposta é {NUMERO_SECRETO}")
            time.sleep(3)
            os.system('cls')
            break
        else:
            print ("Escolha inválida")
            time.sleep(3)
            os.system('cls')
            continue
    else:
        print ("Escolha inválida")
        time.sleep(3)
        os.system('cls')
        continue