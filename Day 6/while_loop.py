#while loop
i = 1
while i < 6:
    print(i)
    i += 1
#while loop with break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
#while loop with continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#while loop with else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
#while loop with else and break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1