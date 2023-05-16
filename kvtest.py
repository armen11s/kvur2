baddata = True
while baddata == True:
    try:
        a = int(input('введите а:'))
        b = int(input('введите b:'))
        c = int(input('введите c:'))
    except:
        print('не удалось получить данные')
