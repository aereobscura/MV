import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# set letter variables to morse values
A = ".-", B = "-...", C = "-.-.", D = "-..", E = ".", F = "..-."
G = "--.", H = "....", I = "..", J = ".---", K = "-.-", L = ".-.."
M = "--", N = "-.", O = "---", P = ".--.", Q = "--.-", R = ".-."
S = "...", T = "-", U = "..-", V = "...-", W = ".--", X = "-..-"
Y = "-.--", Z = "--..", _ = "_", zero = "-----", one = ".----"
two = "..---", three = "...--", four = "....-", five = "....."
six = "-....", seven = "--...", eight = "---..", nine = "----."

def GPIO_MorseOutput():
    message = input("Type a message. '*quit' to quit: ").upper()
    if message == "*QUIT":
        GPIO.cleanup()
        quit()
    morse = []

    for letter in message:
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
            print("Sorry, thats not a valid input")


    print(morse)

    for i in morse:
        for x in i:
            if x == ".":
                GPIO.output(16, True)
                time.sleep(.15)
                GPIO.output(16, False)
                time.sleep(.25)
            elif x == "-":
                GPIO.output(16, True)
                time.sleep(.60)
                GPIO.output(16, False)
                time.sleep(.25)
            elif x == "_":
                GPIO.output(18, True)
                time.sleep(1)
                GPIO.output(18, False)
                time.sleep(.25)
            
        time.sleep(.25)

    def RunAgain():

        run_again = input("type '*quit' to quit, or 'run' to run again").lower()

        if run_again == "*quit":
            GPIO.cleanup()
            quit()
        elif run_again == "run":
            GPIO_MorseOutput()
        else:
            print("huh?")
            time.sleep(.3)
            RunAgain()

    RunAgain()

GPIO_MorseOutput()

GPIO.cleanup()
