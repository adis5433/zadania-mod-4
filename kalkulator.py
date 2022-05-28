import logging
import math
from enum import IntEnum

logging.basicConfig(level=logging.DEBUG)

def sum_icnome_numbers(firs_num, second_num, nums=0):
    result = firs_num + second_num + nums
    return result

def multiply_numbers(firs_num, second_num, nums=1):
    result = firs_num * second_num * nums
    return result


def nums_to_reduction(first_num,second_num):
    result = int(first_num) - int(second_num)
    return result
def nums_to_divie(first_num, second_num):
    result = int(first_num) / int(second_num)
    return "wynik daiałania to:"+ str(result)

print("Witaj w kalkulatorze")

while(True):
    menu = (
          "1 - dodawanie nieograniczonej ilości liczb\n"
          "2 - mnożenie nieograniczonej ilości liczb\n"
          "3 - odejmowanie dwóch licz\n"
          "4 - dzielenie dwóch liczb\n"
          "0 - zamknij kalkulator\n"
          )

    try:
        user_choice_in_menu=input("Którą z opcji wybierasz :\n%s..." % menu)
        if  user_choice_in_menu == "1":
            first_num = int(input("Podaj pierwszą liczbę do sumowania: "))
            second_num = int(input("Podaj pierwszą liczbę do sumowania: "))
            nums = 0
            logging.info("podane do zsumowania liczby to: %s i %s" % (first_num, second_num))
            while (True):
                choice = input("Chcesz podać kolejną liczbę(Y), czy przejść do wyniku(N) ")
                if choice.upper() == "Y":
                    number = int(input("Podaj kolejną liczbę do sumowania: "))
                    nums += number
                    logging.info("dodana do zsumowania liczba to: %s" % (number))
                    continue
                elif choice.upper() == "N":
                    print("wynik dodawania to: ",sum_icnome_numbers(first_num, second_num, nums))
                    break

        elif user_choice_in_menu == "2":

            first_num = int(input("Podaj pierwszą liczbę do mnożenia: "))
            second_num = int(input("Podaj drugą liczbę do mnożenia: "))
            nums = 1
            logging.info("podane do mnożenia liczby to: %s i %s\n" % (first_num, second_num))
            while (True):
                choice = input("Chcesz podać kolejną liczbę(Y), czy przejść do wyniku(N)")
                if choice.upper() == "Y":
                    number = int(input("Podaj kolejną liczbę do mnożenia: "))
                    nums = nums * number
                    logging.info("dodatkowa liczba podana do pomnożenia liczby liczby to: %s" % (number))
                    continue
                elif choice.upper() == "N":
                    print("wynik mnożenia to ",multiply_numbers(first_num, second_num, nums))
                    break

        elif user_choice_in_menu == "3":

            first_num = int(input("Wybrałeś odejmowanie.Podaj pierwszą liczbę: "))
            second_num = int(input("Podaj drugą liczbę: "))
            logging.info("wykonane działanie to:%s - %s" % (first_num, second_num))
            result = str(nums_to_reduction(first_num, second_num))
            print("wynik odejmowania to %s" % (result))




        elif user_choice_in_menu == "4":
            first_num = int(input("Dzielenie.Podaj liczbę która będzie dzielona (Dzielna): "))
            second_num = int(input("Podaj liczbę przez którą będzie dzielona pierwsza liczba (Dzielnik): "))
            logging.info("wykonywane działanie to: %s / %s" % (first_num, second_num))
            if second_num == 0:
                logging.warning("nie dzielimy przez zero! Zmień dzielnik")
                second_num = int(input("Podaj inny dzielnik: "))
            print(nums_to_divie(first_num,second_num))



        elif user_choice_in_menu == "0":
            print("Kończymy program")
            exit()
    except  ValueError :
        print("miała być podana  wartość liczbowa")