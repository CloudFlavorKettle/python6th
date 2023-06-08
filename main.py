a = {10, 20, 30}
b = {10, 20, 30, "멋쟁이사자", "Bae", 40}
c = {10, 20, 30, "멋쟁이사자", "Bae", 40, 10, 20}

new_set = a.copy()

b = set()
print(type(b))
a.add(50)
a.update([10,20,60,70])
print(a)
a.discard('멋쟁이사자')
a.discard(70)
print(a)

# new_set.clear()
# print(new_set)

intersection_a_new = a.intersection(new_set)

print(intersection_a_new)

union_a = a.union(new_set)
print('union_a:', union_a)

differnce_a = a.difference(new_set)
print('difference_a: ', differnce_a)

print(b.issubset(a))
print(a.issuperset(b))

sym_a = a.symmetric_difference(new_set)
print('symmetric_difference: ', sym_a)