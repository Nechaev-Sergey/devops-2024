
print ("Складываем два числа")
print("введите а и в значения как число")
bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите a:"))
        b = int(input("Введите b:"))
        bad_data = False

    except ValueError:
        print("Ошибка данных")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except:
        print("какая-то ошибка")
print(f"Сумма {a} и {b} равна {a + b}.")