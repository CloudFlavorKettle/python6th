from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

print("배열 슬라이싱")
n = len(stu_roll)
for i in range(n):
    print(i, "=", stu_roll[i])

print("1:5까지")
a= stu_roll[1:5]
for i in a:
    print(i)

print("0부터 끝까지")
b = stu_roll[0:]
for i in b:
    print(i)

print("처음부터 5번째까지")
c = stu_roll[:5]
for i in c:
    print(i)

print("마지막 요소 4개 출력")
d = stu_roll[-4:]
for i in d:
    print(i)

print("0부터 6번째 까지 2개씩 건너뛰어 출력")
e = stu_roll[0:7:2]
for i in e:
    print(i)