import RPi.GPIO as GPIO
from flask import redirect, url_for
import time


def Lightswitch(blue_on, green_on):
	
	blue = 16
	green = 18
	on = True
	off = False

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(blue, GPIO.OUT)
	GPIO.setup(green, GPIO.OUT)

	if blue_on and not green_on:
		GPIO.output(blue, on)
		GPIO.output(green, off)
	elif green_on and not blue_on:
		GPIO.output(green, on)
		GPIO.output(blue, off)
	elif green_on and blue_on:
		GPIO.output(green, on)
		GPIO.output(blue, on)
	elif not green_on and not blue_on:
		GPIO.output(green, off)
		GPIO.output(blue, off)
	else:
		GPIO.cleanup()
		return "Error"


def Morsecode(message):


	blue = 16
	green = 18
	on = True
	off = False

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(blue, GPIO.OUT)
	GPIO.setup(green, GPIO.OUT)

	A = ".-" 
	B = "-..."
	C = "-.-."
	D = "-.."
	E = "."
	F = "..-."
	G = "--."
	H = "...."
	I = ".."
	J = ".---"
	K = "-.-"
	L = ".-.."
	M = "--"
	N = "-."
	O = "---"
	P = ".--."
	Q = "--.-"
	R = ".-."
	S = "..."
	T = "-"
	U = "..-"
	V = "...-"
	W = ".--"
	X = "-..-"
	Y = "-.--"
	Z = "--.."
	_ = "_"
	zero = "-----"
	one = ".----"
	two = "..---"
	three = "...--"
	four = "....-"
	five = "....."
	six = "-...."
	seven = "--..."
	eight = "---.."
	nine = "----."

	if message == "*QUIT":
		GPIO.cleanup()
		return redirect(url_for('main.home'))

	morse = []
	morse_string = ""

	for letter in message.upper():
		if letter == "A":
			morse.append(A)
		elif letter == "B":
			morse.append(B)
		elif letter == "C":
			morse.append(C)
		elif letter == "D":
			morse.append(D)
		elif letter == "E":
			morse.append(E)
		elif letter == "F":
			morse.append(F)
		elif letter == "G":
			morse.append(G)
		elif letter == "H":
			morse.append(H)
		elif letter == "I":
			morse.append(I)
		elif letter == "J":
			morse.append(J)
		elif letter == "K":
			morse.append(K)
		elif letter == "L":
			morse.append(L)
		elif letter == "M":
			morse.append(M)
		elif letter == "N":
			morse.append(N)
		elif letter == "O":
			morse.append(O)
		elif letter == "P":
			morse.append(P)
		elif letter == "Q":
			morse.append(Q)
		elif letter == "R":
			morse.append(R)
		elif letter == "S":
			morse.append(S)
		elif letter == "T":
			morse.append(T)
		elif letter == "U":
			morse.append(U)
		elif letter == "V":
			morse.append(V)
		elif letter == "W":
			morse.append(W)
		elif letter == "X":
			morse.append(X)
		elif letter == "Y":
			morse.append(Y)
		elif letter == "Z":
			morse.append(Z)
		elif letter == " ":
			morse.append(_)
		elif letter == "0":
			morse.append(zero)
		elif letter == "1":
			morse.append(one)
		elif letter == "2":
			morse.append(two)
		elif letter == "3":
			morse.append(three)
		elif letter == "4":
			morse.append(four)
		elif letter == "5":
			morse.append(five)
		elif letter == "6":
			morse.append(six)
		elif letter == "7":
			morse.append(seven)
		elif letter == "8":
			morse.append(eight)
		elif letter == "9":
			morse.append(nine)
		else:
			return "Error invalid input" 

	for i in morse:
		for x in i:
			if x == ".":
				GPIO.output(green, on)
				time.sleep(.15)
				GPIO.output(green, off)
				time.sleep(.25)
			elif x == "-":
				GPIO.output(green, on)
				time.sleep(.60)
				GPIO.output(green, off)
				time.sleep(.25)
			elif x == "_":
				GPIO.output(blue, on)
				time.sleep(1)
				GPIO.output(blue, off)
				time.sleep(.25)
		time.sleep(.25)

	GPIO.cleanup()
	return morse


def ManeuverInitialize():
	GPIO.setmode(GPIO.BOARD)

	frontRight_ControlDriver = [8, 10, 12, 16] # wires: 8 yellow, 10 green, 12 blue, 16 purple
	frontLeft_ControlDriver = [26, 24, 22, 18]
	rearRight_ControlDriver = [3, 5, 7, 11]
	rearLeft_ControlDriver = [21, 19, 15, 13] 

	allControlPins= [
		frontLeft_ControlDriver,
		frontRight_ControlDriver,
		rearLeft_ControlDriver,
		rearRight_ControlDriver
	]

	for driver in allControlPins:
		for pin in driver:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, 0)
			print("pin " + str(pin) + " initialized")

	seq = [
		[1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1]
		]

	return allControlPins, seq

def executeManeuver(motor_data):

	MI = ManeuverInitialize()

	rotations = round(1 * float(512))
	FL = motor_data["FL"]
	FR = motor_data["FR"]
	RL = motor_data["RL"]
	RR = motor_data["RR"]

	if FL != 0 :
		#determine direction -reverse +forward
		if FL > 0:
			#forward determined
			#determine speed(delay time) motor slider data max is 100, fastest speed is represented as shortest delay time in millisec 
			if FL == 100:
				speed = 1
			if 80 <= FL < 100:
				speed = 1.5
			if 60 <= FL < 80:
				speed = 2
			if 40 <= FL < 60:
				speed = 2.5
			if 20 <= FL < 40:
				speed = 3
			if 0 < FL < 20:
				speed = 3.5

			#while True:
			for i in range(rotations):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(MI[0][0][pin], MI[1][halfstep][pin])
					time.sleep(speed/float(1000))

		if FL < 0:
			FL *= -1
			if FL == 100:
				speed = 1
			if 80 <= FL < 100:
				speed = 1.5
			if 60 <= FL < 80:
				speed = 2
			if 40 <= FL < 60:
				speed = 2.5
			if 20 <= FL < 40:
				speed = 3
			if 0 < FL < 20:
				speed = 3.5

			for i in range(6):
				for halfstep in range(7, 0, -1):
					for pin in range(4):
						GPIO.output(MI[0][0][pin], MI[1][halfstep][pin])
					time.sleep(speed/float(1000))
			
	if FR != 0:
		#determine direction -reverse +forward
		if FR > 0:
			#forward determined
			#determine speed(delay time) motor slider data max is 100, fastest speed is represented as shortest delay time in millisec 
			if FR == 100:
				speed = 1
			if 80 <= FR < 100:
				speed = 1.5
			if 60 <= FR < 80:
				speed = 2
			if 40 <= FR < 60:
				speed = 2.5
			if 20 <= FR < 40:
				speed = 3
			if 0 < FR < 20:
				speed = 3.5

			#while True:
			for i in range(rotations):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(MI[0][1][pin], MI[1][halfstep][pin])
					time.sleep(speed/float(1000))

		if FR < 0:
			FR *= -1
			if FR == 100:
				speed = 1
			if 80 <= FR < 100:
				speed = 1.5
			if 60 <= FR < 80:
				speed = 2
			if 40 <= FR < 60:
				speed = 2.5
			if 20 <= FR < 40:
				speed = 3
			if 0 < FR < 20:
				speed = 3.5

			for i in range(6):
				for halfstep in range(7, 0, -1):
					for pin in range(4):
						GPIO.output(MI[0][1][pin], MI[1][halfstep][pin])
					time.sleep(speed/float(1000))

	if RL != 0:
		pass
		
	if RR != 0:
		pass
		

	GPIO.cleanup()


def ManeuverForward(which_motors, motor_speed, delay_t, seq, rotations):


	#while True:
	for i in range(rotations):	
		for halfstep in range(8):
			for pin in range(4):
				for motor in which_motors:
					GPIO.output(motor[pin], seq[halfstep][pin])
			time.sleep(delay_t)

	GPIO.cleanup()


def ManeuverReverse(which_motors, motor_speed, delay_t, seq, rotations):


	#use while True for continous rotation. needs try/except interrupt for term & GPIO.cleanup
	#while True:
	#use range(x) for degrees. 360°=512, 180°=256, 90°=128, 45°=64, 22.5°=32, 11.25°=16
	for i in range(rotations):
		for halfstep in range(7, 0, -1):
			for pin in range(4):
				for motor in which_motors:
					GPIO.output(motor[pin], seq[halfstep][pin])
			time.sleep(delay_t)

	GPIO.cleanup()


def GPIOcleanup():
	GPIO.cleanup()
