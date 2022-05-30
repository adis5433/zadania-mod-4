
def sum(*nums):
    result = sum(nums)
    return result

def multipy(*nums):
    result = 1
    for num in nums:
        result = result * num
    return result




def reduction(first_num, second_num):
    result = int(first_num) - int(second_num)
    return result


def divide(first_num, second_num):
    result = int(first_num) / int(second_num)
    return result


print("Witaj w kalkulatorze\n"
        "1 - dodawanie nieograniczonej ilości liczb\n"
        "2 - mnożenie nieograniczonej ilości liczb\n"
        "3 - odejmowanie dwóch licz\n"
        "4 - dzielenie dwóch liczb\n"
        "e - zamknij kalkulator\n")
def calculator(user_choice):
        match user_choice:
            case "1":
                print("wybrałeś dodawanie")
                nums=[]
                first_num = int(input("Podaj pierwszą liczbe : "))
                nums.append(first_num)
                second_num = int(input("Podaj drugą liczbę : "))
                nums.append(second_num)
                while (True):
                    sum_choice = input("Chcesz podać kolejną liczbę(Y), czy przejść do wyniku(N)")
                    if sum_choice.upper() =="Y":
                        num = int(input("Podaj kolejną liczbę do dodania : "))
                        nums.append(num)
                        continue
                    elif sum_choice.upper() =="N":
                        print(sum(*nums))
            case "2":
                print("wybrałeś mnożenie")
                nums = []
                first_num = int(input("Podaj pierwszą liczbe : "))
                nums.append(first_num)
                second_num = int(input("Podaj drugą liczbę : "))
                nums.append(second_num)
                while(True):
                    sum_choice = input("Chcesz podać kolejną liczbę(Y), czy przejść do wyniku(N)")
                    if sum_choice.upper() == "Y":
                        num = int(input("Podaj kolejną liczbę do mnożenia : "))
                        nums.append(num)
                        continue
                    elif sum_choice.upper() == "N":
                        print(multipy(*nums))
                    break
            case "3":
                print("wybrałeś odejmowanie")
                first_num = int(input("Podaj pierwszą liczbę : "))
                second_num = int(input("Podaj pierwszą liczbę : "))
                print(reduction(first_num, second_num))
            case "4":
                print("wybrałeś dzielenie")
                first_num = int(input("Podaj pierwszą liczbę : "))
                second_num = int(input("Podaj pierwszą liczbę : "))
                print(divide(first_num, second_num))
            case "e" :
                exit()
            case _:
                print(f"Nie prawidłowa wartość!")








user_choice=input("Którą z opcji wybierasz...")

calculator(user_choice)
