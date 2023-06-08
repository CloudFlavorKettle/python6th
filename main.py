a = {10, 20, 30}
b = {10, 20, 30, "멋쟁이사자", "Bae", 40}
c = {10, 20, 30, "멋쟁이사자", "Bae", 40, 10, 20}

b = set()
print(type(b))
a.add(50)
a.update([10,20,60,70])
print(a)
a.discard('멋쟁이사자')
print(a)

new_set = a.copy()
new_set.clear()
print(new_set)