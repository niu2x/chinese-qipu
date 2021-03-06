import sys
import json

from chinese_chess import ChineseChess
from qpcode import decode_step_qpcode

if __name__ == '__main__':
	lines = open(sys.argv[1], 'r').readlines()
	steps_qpcode = lines[0].strip()
	try:
		board_qpcode = lines[1].strip()
	except:
		board_qpcode = ''

	steps = decode_step_qpcode(steps_qpcode)

	board = ChineseChess()
	if len(board_qpcode) > 0:
		board.make_board_by_qpcode(board_qpcode)
	else:
		board.make_default_board()

	redWin = len(steps) % 2 == 1
	counter = 0
	
	for step in steps:
		info = board.encode() + " : " + ("%d,%d,%d,%d" % (step[0][0], step[0][1], step[1][0], step[1][1]))
		board.move_piece(step[0], step[1])
		counter += 1

		if redWin and counter % 2 == 1 :
			print(info)
		elif (not redWin) and counter % 2 == 0:
			print(info)

