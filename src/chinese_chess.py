#-*- coding: utf-8 -*-

from board import Board
from piece import Piece

class ChinesePieceTypeClass:
	def __init__(self):
		self.kRC = 0
		self.kRM = 1
		self.kRX = 2
		self.kRS = 3
		self.kRJ = 4
		self.kRB = 5
		self.kRP = 6
		self.kBC = 7
		self.kBM = 8
		self.kBX = 9
		self.kBS = 10
		self.kBJ = 11
		self.kBB = 12
		self.kBP = 13

ChinesePieceType = ChinesePieceTypeClass()

class ChinesePiece(Piece):
	def __init__(self, type, team, name):
		super(ChinesePiece, self).__init__(team, name)
		self.type_ = type

	def type(self):
		return self.type_

class ChineseChess(Board):
	def __init__(self):
		super(ChineseChess, self).__init__()

		self.pieces = {}

		self.pieces[ChinesePieceType.kRC] = ChinesePiece(ChinesePieceType.kRC, '红', '车')
		self.pieces[ChinesePieceType.kRM] = ChinesePiece(ChinesePieceType.kRM, '红', '马')
		self.pieces[ChinesePieceType.kRX] = ChinesePiece(ChinesePieceType.kRX, '红', '相')
		self.pieces[ChinesePieceType.kRS] = ChinesePiece(ChinesePieceType.kRS, '红', '仕')
		self.pieces[ChinesePieceType.kRJ] = ChinesePiece(ChinesePieceType.kRJ, '红', '帅')
		self.pieces[ChinesePieceType.kRB] = ChinesePiece(ChinesePieceType.kRB, '红', '兵')
		self.pieces[ChinesePieceType.kRP] = ChinesePiece(ChinesePieceType.kRP, '红', '炮')

		self.pieces[ChinesePieceType.kBC] = ChinesePiece(ChinesePieceType.kBC, '黑', '车')
		self.pieces[ChinesePieceType.kBM] = ChinesePiece(ChinesePieceType.kBM, '黑', '马')
		self.pieces[ChinesePieceType.kBX] = ChinesePiece(ChinesePieceType.kBX, '黑', '象')
		self.pieces[ChinesePieceType.kBS] = ChinesePiece(ChinesePieceType.kBS, '黑', '士')
		self.pieces[ChinesePieceType.kBJ] = ChinesePiece(ChinesePieceType.kBJ, '黑', '将')
		self.pieces[ChinesePieceType.kBB] = ChinesePiece(ChinesePieceType.kBB, '黑', '卒')
		self.pieces[ChinesePieceType.kBP] = ChinesePiece(ChinesePieceType.kBP, '黑', '炮')

	def make_default_board(self):

		self.clear()

		self.put_piece(ChinesePieceType.kBC, 0, 0)
		self.put_piece(ChinesePieceType.kBM, 1, 0)
		self.put_piece(ChinesePieceType.kBX, 2, 0)
		self.put_piece(ChinesePieceType.kBS, 3, 0)
		self.put_piece(ChinesePieceType.kBJ, 4, 0)
		self.put_piece(ChinesePieceType.kBC, 8, 0)
		self.put_piece(ChinesePieceType.kBM, 7, 0)
		self.put_piece(ChinesePieceType.kBX, 6, 0)
		self.put_piece(ChinesePieceType.kBS, 5, 0)
		self.put_piece(ChinesePieceType.kBP, 1, 2)
		self.put_piece(ChinesePieceType.kBP, 7, 2)
		self.put_piece(ChinesePieceType.kBB, 0, 3)
		self.put_piece(ChinesePieceType.kBB, 2, 3)
		self.put_piece(ChinesePieceType.kBB, 4, 3)
		self.put_piece(ChinesePieceType.kBB, 6, 3)
		self.put_piece(ChinesePieceType.kBB, 8, 3)

		self.put_piece(ChinesePieceType.kRC, 0, 9)
		self.put_piece(ChinesePieceType.kRM, 1, 9)
		self.put_piece(ChinesePieceType.kRX, 2, 9)
		self.put_piece(ChinesePieceType.kRS, 3, 9)
		self.put_piece(ChinesePieceType.kRJ, 4, 9)
		self.put_piece(ChinesePieceType.kRC, 8, 9)
		self.put_piece(ChinesePieceType.kRM, 7, 9)
		self.put_piece(ChinesePieceType.kRX, 6, 9)
		self.put_piece(ChinesePieceType.kRS, 5, 9)
		self.put_piece(ChinesePieceType.kRP, 1, 7)
		self.put_piece(ChinesePieceType.kRP, 7, 7)
		self.put_piece(ChinesePieceType.kRB, 0, 6)
		self.put_piece(ChinesePieceType.kRB, 2, 6)
		self.put_piece(ChinesePieceType.kRB, 4, 6)
		self.put_piece(ChinesePieceType.kRB, 6, 6)
		self.put_piece(ChinesePieceType.kRB, 8, 6)

	def do_step_by_qpcode(self, step):
		step = step.strip()
		for i in range(int(len(step)/4)):
			x1, y1, x2, y2 = step[i*4], step[i*4+1], step[i*4+2], step[i*4+3]
			x1 = ord(x1) - ord('a')
			x2 = ord(x2) - ord('a')

			y1 = 9 - (int(y1))
			y2 = 9 - (int(y2))

			self.move_piece((x1, y1), (x2, y2))

	def make_board_by_qpcode(self, sz):

		self.clear()

		maps = {}
		maps['k'] = ChinesePieceType.kBJ
		maps['K'] = ChinesePieceType.kRJ

		maps['p'] = ChinesePieceType.kBB
		maps['P'] = ChinesePieceType.kRB

		maps['c'] = ChinesePieceType.kBP
		maps['C'] = ChinesePieceType.kRP

		maps['r'] = ChinesePieceType.kBC
		maps['R'] = ChinesePieceType.kRC

		maps['b'] = ChinesePieceType.kBX
		maps['B'] = ChinesePieceType.kRX

		maps['a'] = ChinesePieceType.kBS
		maps['A'] = ChinesePieceType.kRS

		maps['n'] = ChinesePieceType.kBM
		maps['N'] = ChinesePieceType.kRM

		e = sz.find('w')
		sz = sz[0:e]
		sz = sz.strip()
		sz = sz.split('/')
		for y in range(10):
			x = 0
			for v in sz[y]:
				if v in [str(c) for c in range(10)]:
					x += int(v)
				else:
					self.put_piece(maps[v], x, y)
					x += 1

	def put_piece(self, piece_type, x, y):
		super(ChineseChess, self).put_piece(self.pieces[piece_type], x, y)

	def empty_width(self):
		return 5

	def encode(self):
		result = []
		for y in range(10):
			for x in range(9):
				piece = self.piece_at(x, y)
				if piece:
					result.append(2 ** self.piece_at(x, y).type())
				else:
					result.append(0)
		result = map(str, result)
		return ','.join(result)

if __name__ == '__main__':
	board = ChineseChess()
	board.make_default_board()
	print(board.encode())
	board.make_board_by_qpcode('1rbckaP2/3PaP1r1/1P2b4/1R7/Nn7/CRBp1n3/4C4/9/4p1p2/1c3K3 w')
	print(board)
	print('\n---------------------\n')
	board.do_step_by_qpcode('g9f9d9f9d8e8e9d9e8e9d9d8b6d6b5d6a5c6d8d7b7c7d7d8b4b8b9b8c7b7d8d7a4a7')
	print(board.encode())
