import RPi.GPIO as GPIO
import sys, letters

def print_usage():
    print('The program requires exactly 2 arguments in order to operate.\n',
            'Usage: morse.py pin message\n'
            'E.g.:\n','morse.py 25 SOS\n','morse.py 18 "HOLY COW"\nPlease refrain',
            'from using punctuation.')
    sys.exit()

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3 or len(args) > 3:
        print_usage()
    pin = int(args[1])
    message = args[2]
    error = False
    upperCaseMsg = message.upper()
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    print("Sending message: %s to pin %i."%(message,pin))
    try: 
        for char in upperCaseMsg:
            myLetter = letters.Letter.factory(pin, char)
            myLetter.morseVal()
    except Exception as e:
        print(e)
        error = True
        
    if error:
        print("Please reformat your text...")
    else:
        print("Done!")

