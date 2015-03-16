import RPi.GPIO as GPIO
import time

class Letter(object):
    """A factory method used to return the morse representation"""
    def factory(pin, name):
        if name == 'A' : return LetterA(pin)
        elif name == 'B' : return LetterB(pin)
        elif name == 'C' : return LetterC(pin)
        elif name == 'D' : return LetterD(pin)
        elif name == 'E' : return LetterE(pin)
        elif name == 'F' : return LetterF(pin)
        elif name == 'G' : return LetterG(pin)
        elif name == 'H' : return LetterH(pin)
        elif name == 'I' : return LetterI(pin)
        elif name == 'J' : return LetterJ(pin)
        elif name == 'K' : return LetterK(pin)
        elif name == 'L' : return LetterL(pin)
        elif name == 'M' : return LetterM(pin)
        elif name == 'N' : return LetterN(pin)
        elif name == 'O' : return LetterO(pin)
        elif name == 'P' : return LetterP(pin)
        elif name == 'Q' : return LetterQ(pin)
        elif name == 'R' : return LetterR(pin)
        elif name == 'S' : return LetterS(pin)
        elif name == 'T' : return LetterT(pin)
        elif name == 'U' : return LetterU(pin)
        elif name == 'V' : return LetterV(pin)
        elif name == 'W' : return LetterW(pin)
        elif name == 'X' : return LetterX(pin)
        elif name == 'Y' : return LetterY(pin)
        elif name == 'Z' : return LetterZ(pin)
        elif name == ' ' : return Space(pin)
        elif name == '0' : return Letter0(pin)
        elif name == '1' : return Letter1(pin)
        elif name == '2' : return Letter2(pin)
        elif name == '3' : return Letter3(pin)
        elif name == '4' : return Letter4(pin)
        elif name == '5' : return Letter5(pin)
        elif name == '6' : return Letter6(pin)
        elif name == '7' : return Letter7(pin)
        elif name == '8' : return Letter8(pin)
        elif name == '9' : return Letter9(pin)
        else: raise Exception("Faulty input!(@ '%c')" %name)
    factory = staticmethod(factory)

class AbstractLetter(object):
    def __init__(self, pin):
        self.pin = pin

    def dotSignal(self):
        #Turn light ON
        GPIO.output(self.pin, GPIO.HIGH)
        #Dot has only 1 unit of duration
        time.sleep(0.1)
        #Turn light OFF
        GPIO.output(self.pin, GPIO.LOW)
        #Same letter parts have 1 unit between them
        time.sleep(0.1)
    def dashSignal(self):
        #Turn light ON
        GPIO.output(self.pin, GPIO.HIGH)
        #Dash has a 3 unit duration
        time.sleep(0.3)
        #Turn light OFF
        GPIO.output(self.pin, GPIO.LOW)
        #Same letter parts have 1 unit between them
        time.sleep(0.1)
    def letterSpace(self):
        #only 2 units, because we add 1 after each signal
        time.sleep(0.2)   
    def wordSpace(self):
        #only 6 units, because we add 1 after each signal
        time.sleep(0.6)

    def morseVal(self):
        #Each letter has 3 units of space before the next
        self.letterSpace()
    
class Space(AbstractLetter):
    def morseVal(self): #Each letter needs to implement this method
        super().wordSpace()

class LetterA(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dashSignal()
        super().morseVal()

class LetterB(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class LetterC(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super().dashSignal()
        super().dotSignal()
        super().moreseVal()

class LetterD(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super.dotSignal()
        super().morseVal()

class LetterE(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().morseVal()

class LetterF(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dashSignal()
        super().dotSignal()
        super().morseVal()

class LetterG(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dotSignal()
        super().morseVal()

class LetterH(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class LetterI(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class LetterJ(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class LetterK(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super().dashSignal()
        super().morseVal()

class LetterL(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dashSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class LetterM(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class LetterN(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super().morseVal()

class LetterO(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class LetterP(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dashSignal()
        super().dashSignal()
        super().dotSignal()
        super().morseVal()

class LetterQ(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dotSignal()
        super().dashSigna()
        super().morseVal()

class LetterR(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dashSignal()
        super().dotSignal()
        super().morseVal()

class LetterS(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class LetterT(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().morseVal()

class LetterU(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dashSignal()
        super().morseVal()

class LetterV(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dashSignal()
        super().morseVal()

class LetterW(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class LetterX(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super().dotSignal()
        super().dashSignal()
        super().morseVal()

class LetterY(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class LetterZ(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class Letter1(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class Letter2(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class Letter3(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

class Letter4(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dashSignal()
        super().morseVal()

class Letter5(AbstractLetter):
    def morseVal(self):
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class Letter6(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class Letter7(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dotSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class Letter8(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().dotSignal()
        super().dotSignal()
        super().morseVal()

class Letter9(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().dotSignal()
        super().morseVal()

class Letter0(AbstractLetter):
    def morseVal(self):
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().dashSignal()
        super().morseVal()

