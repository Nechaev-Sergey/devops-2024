import math

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

D = b*b - (4*a*c)
print(f'Дискриминант равен: {D}.')

if D > 0:
    d = math.sqrt(D)
    X1 = ((-b) + d)/(2*a)
    X2 = ((-b) - d)/(2*a)
    print(f"Первый корень равен {X1}, второй {X2}")
elif D == 0:
    X1 = (-b)/(2*a)
    print("Корень уравнения {}".format(X1))
else:
    print('У уравнения нет корней')