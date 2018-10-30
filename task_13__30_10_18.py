arr = [
	   'party one',
	   'party one',
	   'party one',
	   'party two',
	   'party one',
	   'party three',
	   'party three',
	   'party two',
	   'party three',]

count = 0

arrFlags = []
for i in range(0, len(arr)):
	arrFlags.append(1)

for i in range(0, len(arr)):
	count = 0
	for j in range(i, len(arr)):
		if arr[i] == arr[j] and arrFlags[j] != 0:
			count += 1
			arrFlags[j] = 0
			arrFlags[i] += 1

print(arrFlags)

def findMax(m):
	for i in range(0, len(arrFlags)):
		if m < arrFlags[i]:
			m = arrFlags[i]
	return m

max = findMax(arrFlags[0])

while max != 0:
	for i in range(0, len(arr)):
		if arrFlags[i] == max:
			print(arr[i])
			arrFlags[i] = 0
	max = findMax(arrFlags[0])


	

