f = open("example1.txt", "r")

f.seek(6)
print(f.read(5))

f.close()
