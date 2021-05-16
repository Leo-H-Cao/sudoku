arr =  [[0, 0, 1, 0, 0, 9, 0, 0, 8], 
        [0, 6, 0, 0, 5, 0, 0, 3, 0], 
        [4, 0, 0, 3, 0, 0, 5, 0, 0], 
        [2, 0, 0, 8, 0, 0, 3, 0, 0], 
        [0, 7, 0, 0, 9, 0, 0, 2, 0], 
        [0, 0, 6, 0, 0, 3, 0, 0, 7], 
        [0, 0, 8, 0, 0, 2, 0, 0, 1], 
        [0, 4, 0, 0, 6, 0, 0, 7, 0], 
        [7, 0, 0, 5, 0, 0, 9, 0, 0]]

def print_grid():
	for i in range(9):
		for j in range(9):
			print(str(arr[i][j])+' '),

		print('\n')

def used_in_row(row, num):
	for i in range(9):
		if arr[row][i] == num:
			return True
	return False

def used_in_col(col, num):
	for i in range(9):
		if arr[i][col] == num:
			return True
	return False

def used_in_box(row, col, num):
	for i in range(3):
		for j in range(3):
			if arr[row+i][col+j] == num:
				return True
	return False

def can_place(row, col, num):
	return not used_in_row(row, num) and not used_in_col(col, num) and not used_in_box(row - row%3, col - col%3, num)

def find_empty():
	for i in range(9):
		for j in range(9):
			if arr[i][j] == 0:
				return (i,j)
	return (10,10)


def solve():
	row, col = find_empty()
	if row == 10 and col == 10:
		return True
	for num in range(1,10):
		if can_place(row, col, num):
			arr[row][col] = num
			if solve():
				return True
			else:
				arr[row][col] = 0
	return False


print_grid()
if solve():
	print('---------------------------')
	print_grid()
else:
	print('Not solvable')










