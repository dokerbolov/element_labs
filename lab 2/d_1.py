

def bubleSort(list):
    for i in range(0, len(list)):
        for j in range(1, len(list) - i):
            if(list[j-1] > list[j]):
                list[j], list[j-1] = list[j-1], list[j]
    return list

n = int(input())
a = []

for i in range(0,n):
    a.append(int(input()))

print(bubleSort(a))


