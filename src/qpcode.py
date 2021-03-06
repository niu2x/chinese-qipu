def decode_step_qpcode(step_qpcode):
	step_qpcode = step_qpcode.strip()
	steps = []
	for i in range(int(len(step_qpcode)/4)):
		x1, y1, x2, y2 = step_qpcode[i*4], step_qpcode[i*4+1], step_qpcode[i*4+2], step_qpcode[i*4+3]
		x1 = ord(x1) - ord('a')
		x2 = ord(x2) - ord('a')
		y1 = 9 - (int(y1))
		y2 = 9 - (int(y2))
		steps.append(((x1, y1), (x2, y2)))
	return steps