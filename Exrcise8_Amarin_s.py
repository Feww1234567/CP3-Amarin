username=input('Username :')
password=input('Passwword :')
if username == 'admin' and password == 'admin':
    print('Your WELCOME !!')
    print('--------------------------')
    print('Product list')
    print('1.Milk  42THB')
    print('2.Water 10THB')
    print('3.Cake  65THB')
    userselected = int(input('>>>'))
    if userselected == 1:
        amount=int(input('amount :'))
        sum1=amount*42
        print('Total',sum1)
    if userselected == 2:
        amount = int(input('amount :'))
        sum1 = amount * 10
        print('Total', sum1)
    if userselected == 3:
        amount=int(input('amount :'))
        sum1 =amount*65
        print('Total',sum1)
