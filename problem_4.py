# Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#   (examples)
#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

import time

class Solutions:
	def __init__(self, arr: list[int]) -> int:
		self.arr = arr

	def multiplications_of_arr(self):
		array = self.arr
		dic = {}

		for key in range(1, 10):
			count = 0
			for a in array:
				if a%key == 0:
					count += 1

			dic[key] = count

		return dic

if __name__ == '__main__':
	arr = [1,2,8,9,12,46,76,82,15,20,30]
	solution = Solutions(arr)
	print(solution.multiplications_of_arr())