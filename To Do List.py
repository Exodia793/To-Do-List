a = "[ ] tugas b.indo"

b = "[ ]" in a

print(b)
print()
if b == True:
    a = a.replace("[ ]", "[\u2713]")

print(a)