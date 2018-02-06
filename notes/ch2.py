a = 2.5
b = 1
print(id(b))
b = 2.5

print(a==b)
print(id(a))
print(id(b))
print(a is b)