all: des compile

compile:
	pyinstaller -F -w -i "design/ic.ico" code/tester.py

des:
	pyuic5 design/des.ui -o code/des.py
