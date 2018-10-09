#TASK 1

word = input()
word = word.strip().replace(" ", '').lower()
count = 0
letters = []

for i in word:
    count = 0
    for j in word:
        if i == j:
            count += 1
    word = word.strip().replace(i, "0")
    if count > 0:
        print(f"{i} -- {round(count/len(word), 4)*100}%")



# Task 2

text = input()

count = 0
num = []
num2 = ""
for i in text:
    if i.isdigit():
        num.append(i)
        count = 1

if count == 0:
    print("No number")

if count == 1:
    num = sorted(num)
    for i in num:
        num2 += i

print(num2)

# Task 3
pos = 0
pupils = {0: "Петя", 1: "Ваня", 2: "Толя", 3: "Семен"}

sequence = input().split(" ")

min = int(sequence[0])

for i in range(0,len(sequence)):
    if min > int(sequence[i]):
        min = int(sequence[i])
        pos = i

print(pupils[pos])
