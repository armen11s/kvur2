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
elif D == 0:
    print('один корень')
else:
    print('нет корней')

