class Board:
	def __init__(self):
		self.clear()

	def __str__(self):
		result = ""
		for y in range(10):
			for x in range(9):
				cell = self.cells_[x][y]
				if cell == None:
					result += " " * self.empty_width()
				else:
					result += cell.display_name()
				result += " "
			result += "\n"
		return result

	def put_piece(self, piece, x, y):
		self.cells_[x][y] = piece

	def move_piece(self, src, dst):
		self.cells_[dst[0]][dst[1]] = self.cells_[src[0]][src[1]]
		self.cells_[src[0]][src[1]] = None

	def empty_width():
		return 1

	def clear(self):
		self.cells_ = [[None for y in range(10)] for x in range(9)]

	def piece_at(self, x, y):
		return self.cells_[x][y]


if __name__ == '__main__':
	print(Board())
