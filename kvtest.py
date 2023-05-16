from math import sqrt


baddata = True
while baddata == True:
    try:
        a = int(input('введите а:'))
        b = int(input('введите b:'))
        c = int(input('введите c:'))
        baddata =False
    except:
        print('не удалось получить данные')

D = (b*b) - (4 * a * c)
if D > 0:

      d = sqrt(D)
      X1 = ((-b) + d) / (2*a)
      X2 = ((-b) - d) / (2 * a)
      print(f'уравнение два корня X1 = {X1}, X2 = {X2}')

elif  D == 0:
    x1 = (-b) / (2 * a)
    print(f'уравнение имеет один корнь X1 = {X1}.')
else:
    print(' уравнение не имеет корней')

