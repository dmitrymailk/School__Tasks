#TASK 8
num = list(range(1, 11))

max = num[0]

for i in range(0,len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] > max and j - i >= 7:
            max = num[i] + num[j]

print(max)

#TASK 9

num2  = [123, 2000, 10, 3716, 10]
min = num2[0]

for i in range(0, len(num2)):
    for j in range(i+1, len(num2)):
        if num2[i] * num2[j] < min:
            min = num2[i] * num2[j]

print(min)

#TASK 10

word = "It is not a simple task. Yes!"

max_w = 0
count = 0
letter_box = []

for i in range(0, len(word)):
    count = 0
    for j in range(i+1, len(word)):
        if word[i].lower() == word[j].lower() and word[i] != " " and word[j] != " ":
            count += 1
            if max_w < count:
                print(f"letter_box[0] -- {word[i].lower()} count - {count}")
                letter_box.append(word[i].lower())
                max_w = count



letter_box = sorted(letter_box)


print(f"{letter_box[0]} {max_w}")
