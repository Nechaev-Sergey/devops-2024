print ("Решаем квадратное уравнение")
print("Для решения уравнения введите следующие значения как число")
bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите a:"))
        b = int(input("Введите b:"))
        c = int(input("Введите c:"))
        bad_data = False

    except ValueError:
        print("Ошибка данных")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except:
        print("какая-то ошибка")
