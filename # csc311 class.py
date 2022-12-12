count = 0
txt = "quduywf  euyuygGUFGVHJBB"
for letter in txt:
    if letter == letter.upper():
        count+=1
        if letter == " ":
            count-=1

print(count)