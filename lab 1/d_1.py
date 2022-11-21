a, b, c = int(input()), int(input()), int(input())
max_num = max(a, b, c)

if ( a + b > c and a + c > b and b + c > a ):
    if ( a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 ):
        print('right')
    elif ((max_num == a and a**2 > b**2 + c**2) or (max_num == b and b**2 > a**2 + c**2) or (max_num == c and c**2 > b**2 + a**2)):
        print('obtuse')
    else:
        print('acute')
else:
    print('impossible')