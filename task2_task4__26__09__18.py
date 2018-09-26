# Task number 2
print('Task number 2')

string = 'Day 10, mice 8: "Year" 7 is a mistake 91'
num = []
numExists = False

for letter in string:
	if letter.isdigit():
		num.append(letter)
		numExists = True

num = sorted(num)[::-1]

if numExists:
	print(f"Yes\n{''.join(num)}")

else: print('No')



# Task number 4
print('\nTask number 4')

point_list = [[7,7],[3,7],[5,5],[7,3],[3,3]]
min_rad = float('inf')
rad = float('inf')
index = None

for i in range(0,len(point_list)):
	if rad < min_rad:
			min_rad = rad
			index = i
	print('\n')
	rad = 0
	for j in range(0, len(point_list)):
		rad += ((point_list[j][0] - point_list[i][0])**2 + (point_list[j][1] - point_list[i][1])**2)**0.5
		print(f'i -- {i} j -- {j} rad -- {rad}')


print(f'\nindex -- {index} min_rad -- {min_rad}')
