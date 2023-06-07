import array
str_roll = array.array('i', [101, 102, 103, 104, 105])
print(str_roll[0])
print(str_roll[1])
print(str_roll[2])
print(str_roll[3])
print(str_roll[4])

for element in str_roll:
    print(element)

print("인덱스를 이용한 순회")
n = len(str_roll)
for i in range(n):
    print(i, "=", str_roll[i])

print("인덱스를 사용한 while 루프 배열 순회")
i = 0
while i < n:
    print(str_roll[i])
    i += 1