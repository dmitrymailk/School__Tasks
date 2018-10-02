arr = [1,2,3,4,1,8,7,1,10,12]

max_sum = float('-inf')
maximum = max_sum

for i in range(0,len(arr)-1):
	
	if arr[i] < arr[i+1]:
		max_sum += arr[i]

	if max_sum > maximum:
		maximum = max_sum + arr[i+1]

	if arr[i] > arr[i+1]:
		max_sum = 0

print(f'maximum -- {maximum}') # output == 23
