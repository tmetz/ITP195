file = open("grade_book.txt", "r", encoding="utf8")

print(file.readline(6))
print(file.tell())
file.seek(0)
print(file.tell())
print(file.readline())
#file.seek(5, 1) # can only use for binary files??
file.seek(0,2) # go to the end
print(file.tell())
