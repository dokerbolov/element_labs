a, b, c = int(input()), int(input()), int(input())

if ( a <= b and a <= c ):
    if ( b <= c ):
        print(f'{a} {b} {c}')
    else:
        print(f'{a} {c} {b}')
elif ( b <= c and b <= a ):
    if ( a <= c ):
        print(f'{b} {a} {c}')
    else:
        print(f'{b} {c} {a}')
else:
    if ( a <= b ):
        print(f'{c} {a} {b}')
    else:
        print(f'{c} {b} {a}')