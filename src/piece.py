class Piece:
	def __init__(self, team, name):
		self.name_ = name
		self.team_ = team

	def name(self):
		return self.name_

	def team(self):
		return self.team_

	def display_name(self):
		return self.team_ + ":" + self.name_

if __name__ == '__main__':
	print(Piece('红', '马').name())