#
# Author: Aydin Arif
# Student Email: aarif24@myseneca.ca
#
# Place the code for your lab 5 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab5.py
#



class MinHeap:

	def __init__(self, inital_data = None):
		if inital_data is None:
			self.heap = []
		else:
			self.heap = list(inital_data)

		last_parent = (len(self.heap) - 2) // 2
		for index in range(last_parent, -1, -1):
			size = len(self.heap)
			current = index

			while True:
				left = 2 * current + 1
				right = 2 * current + 2
				smallest = current

				if left < size and self.heap[left] < self.heap[smallest]:
					smallest = left
				if right < size and self.heap[right] < self.heap[smallest]:
					smallest = right
				if smallest == current:
					break

				self.heap[current], self.heap[smallest] = self.heap[smallest], self.heap[current]
				current = smallest
# ------------------------------------------
	def is_empty(self):
		return len(self.heap) == 0
# ------------------------------------------
	def size(self):
		return len(self.heap)
# ------------------------------------------
	def push(self, data):
		self.heap.append(data)
		index = len(self.heap) - 1

		while index > 0:
			parent = (index - 1) // 2
			if self.heap[parent] <= self.heap[index]:
				break
			self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
			index = parent
# ------------------------------------------
	def pop(self):
		if self.is_empty():
			return None

		removed = self.heap[0]
		last = self.heap.pop()

		if not self.is_empty():
			self.heap[0] = last
			size = len(self.heap)
			index = 0

			while True:
				left = 2 * index + 1
				right = 2 * index + 2
				smallest = index

				if left < size and self.heap[left] < self.heap[smallest]:
					smallest = left
				if right < size and self.heap[right] < self.heap[smallest]:
					smallest = right
				if smallest == index:
					break

				self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
				index = smallest

		return removed
# ------------------------------------------
	def min(self):
		if self.is_empty():
			return None
		return self.heap[0]

