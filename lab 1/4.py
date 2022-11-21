a = int(input())

break_1 = a//2
break_2 = (a-1)//2

minute = 9*60 + a*45 + break_1 * 5 + break_2 * 15

print(f'{minute//60} {minute%60}')