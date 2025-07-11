name = input("Enter your name: ").lower()

for i in range(len(name)):
    ch = name[i]
    if name[:i].count(ch) == 0:  # Check If already counted
        count = 0
        for j in range(len(name)):
            if name[j] == ch:
                count += 1
        print(ch, ":", count)