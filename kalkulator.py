import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


def get_numbers():
        while (True):
            try:
                nums = []
                first_num = int(input("Podaj pierwszą liczbe : "))
                nums.append(first_num)
                second_num = int(input("Podaj drugą liczbę : "))
                nums.append(second_num)
                logging.info ("///Liczby na których będzie wykonywane zadanie na ten moment to: %s" % nums)
                sum_choice = input("Chcesz podać kolejną liczbę(Y), czy przejść do wyniku(N)")
                if sum_choice.upper() == "Y":
                        num = int(input("Podaj kolejną liczbę do dodania : "))
                        nums.append(second_num)
                        logging.info ("///Liczby na których będzie wykonywane zadanie na ten moment to: %s" % nums)
                elif sum_choice.upper() == "N":
                    logging.info ("///Ostatecznie będziemy wykonywali działanie na : %s" % nums)
                    return nums
                    break
            except:
                logging.error ("///Podałeś nieprawidłową wartość")
                ValueError



def addition():
    result = sum(get_numbers())
    return "Wynik dodoawania to %s" % result

def multipy():
    result = 1
    nums = get_numbers()
    for num in nums:
        result = result * num
    return "Wynik mnożenia to %s" % result


def reduction():
    nums = get_numbers()
    result=nums[0]*2
    for num in nums:
        result = result - num
    return "Wynik odejmowania to %s" % result


def divide():
    nums = get_numbers()
    result = nums[0]*nums[0]
    for num in nums:
        result = result / num
    return "Wynik dzielenia to %s" % result


def calculator(user_choice):
        match user_choice:
            case "1":
                print("Wybrałeś dodawanie")
                print(addition())
            case "2":
                print("Wybrałeś mnożenie")
                print(multipy())
            case "3":
                print("Wybrałeś odejmowanie")
                print(reduction())
            case "4":
                print("Wybrałeś dzielenie")
                try:
                    print(divide())
                except:
                    ZeroDivisionError
                    logging.error("///nie dzielimy przez zero")
            case "e" :
                print("Kończymy program")
                exit()
            case _:
                logging.error("///Podałeś wartość z poza menu podaj jeszcze raz prawidłową")
                print(f"Nie prawidłowa wartość!")



while(True):
        print("Witaj w kalkulatorze\n"
            "1 - dodawanie nieograniczonej ilości liczb\n"
            "2 - mnożenie nieograniczonej ilości liczb\n"
            "3 - odejmowanie dwóch licz\n"
            "4 - dzielenie dwóch liczb\n"
            "e - zamknij kalkulator\n")
        user_choice=input("Którą z opcji wybierasz...")
        calculator(user_choice)