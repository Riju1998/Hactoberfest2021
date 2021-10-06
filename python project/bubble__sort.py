import time
def up_sort(n):
    a = []
    print('Enter numbers one by one:\n')
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        for j in range(0,n-(i+1)):
            if a[j]>a[j + 1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
    print('The sorted list is   ',a)

def down_sort(n):
    a = []
    print('Enter numbers one by one:\n')
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        for j in range(0,n-(i+1)):
            if a[j]<a[j + 1]:
                t = a[j]
                a[j] = a[j + 1]
                a[j + 1] = t
    print('The sorted list is   ',a)
print(time.asctime(time.localtime()))
s = int(input('Press 0 for ascending order and 1 for descending order:\n'))
n = int(input('Enter the size of list:\n'))
if s == 0:
    up_sort(n)
else:
    down_sort(n)

