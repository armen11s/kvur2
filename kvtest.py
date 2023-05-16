import math


baddata = True
while baddata == True:
    try:
        a = int(input('введите а:'))
        b = int(input('введите b:'))
        c = int(input('введите c:'))
    except:
        print('не удалось получить данные')

D = (b*b) - (4 * a * c)
if D > 0:
      print('два кеорня')
      d = math.sqrt(D)
      x1 = ((-b) + d) / (2*a)
      x2 = ((-b) - d) / (2 * a)
elif D == 0:
    print('один корень')
    x1 = (-b) / (2 * a)
else:
    print('нет корней')

