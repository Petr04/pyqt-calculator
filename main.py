import sys
from PyQt5 import QtWidgets as qw


class MainWindow(qw.QMainWindow):
	def __init__(self):
		super().__init__()

		self.clear = 'Clear'
		self.backspace = '<='

		self.initUI()

	def initUI(self):
		w = qw.QWidget()

		self.setWindowTitle('Calculator')
		self.setMinimumSize(300, 200)

		container = qw.QGridLayout()

		grid = qw.QGridLayout()

		self.expression = qw.QLineEdit()
		self.expression.returnPressed.connect(self.onEnter)

		grid.addWidget(self.expression, 0, 0, 1, 2)

		self.buttons = []

		for i in list(range(1, 11)):
			if i == 10:
				text = '0'
			else:
				text = str(i)

			button = qw.QPushButton(text)
			grid.addWidget(button, (i-1) / 3 + 1, (i-1) % 3)
			self.buttons.append(button)

		for i, text in enumerate([self.backspace, '/', '*', '-', '+']):
			button = qw.QPushButton(text)

			grid.addWidget(button, i, 3)

			self.buttons.append(button)

		dot = qw.QPushButton('.')
		grid.addWidget(dot, 4, 1)
		self.buttons.append(dot)

		eq = qw.QPushButton('=')
		grid.addWidget(eq, 4, 2)
		self.buttons.append(eq)

		clear = qw.QPushButton('Clear')
		grid.addWidget(clear, 0, 2)
		self.buttons.append(clear)

		for i in range(len(self.buttons)):
			self.buttons[i].clicked.connect(self.onPress)

		container.addLayout(grid, 0, 0)
		w.setLayout(container)
		self.setCentralWidget(w)
		self.show()


	def onPress(self):
		text = self.sender().text()
		text_expr = self.expression.text()

		if text == '=':
			self.expression.returnPressed.emit()
		elif text == self.clear:
			self.expression.clear()
		elif text == self.backspace:
			self.expression.setText(text_expr[:-1])
		else:
			self.expression.setText(text_expr + text)

	def onEnter(self):
		try:
			result = eval(self.expression.text())
		except:
			self.expression.setText('Invalid input')
		else:
			self.expression.setText(str(result))

if __name__ == '__main__':
	app = qw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())
