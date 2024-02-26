import logging
from re import S
import string
import random
# loggning.py
# A simple logging utility that uses a standard function log()
# to log information to a log file.
# the name of the log file is defined by logName and logFileName.
# The log is cleared every time this module is called
#


# --- define the log file name ---
logName = "eliza"
filename = logName+'.log'

# --- create a logging object called logger ---
logger = logging.getLogger(logName)
hdlr = logging.FileHandler(filename)

# --- set the format to be just the message ---
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
# --- log all levels above and including info messages ---
logger.setLevel(logging.INFO)

# --- clear the log file when starting ---
logFile = open(filename, "w")
logFile.write("")
logFile.close()

# --- the main log function. Appends the string s to the log ---


def log(s):
    logger.error(s)


positiva = ["Berätta mer", "Jag förstår...",
            "Ahaa...",
            "Jag lyssnar..."]
negativa = ["Varför är du så negativ?", "Är du på så dåligt humör?",
            "Don't be a negative Nelly!", "Never say never!"]
mammasvar = ["varför är din mamma så elak?",
             "Har du försökt prata med din mamma om det?"]

pappasvar = ["varför är din pappa så elak?",
             "När har du senast försökt prata med din pappa?"]
tecken = "!?"


def svar(text):
    urspr_ord = str.split(text)
    nya_ord = urspr_ord[:]
    for i in range(len(urspr_ord)):
        ord = urspr_ord[i]
        if "jag" in ord:
            nya_ord[i] = nya_ord[i].replace("jag", "du")
        elif "min" in ord:
            nya_ord[i] = nya_ord[i].replace("min", "din")
        elif "mitt" in ord:
            nya_ord[i] = nya_ord[i].replace("mitt", "ditt")
        elif "mig" in ord:
            nya_ord[i] = nya_ord[i].replace("mig", "dig")
        elif "mina" in ord:
            nya_ord[i] = nya_ord[i].replace("mina", "dina")
        elif "din" in ord:
            nya_ord[i] = nya_ord[i].replace("din", "min")
        elif "ditt" in ord:
            nya_ord[i] = nya_ord[i].replace("ditt", "mitt")
        elif "dina" in ord:
            nya_ord[i] = nya_ord[i].replace("dina", "mina")
        elif "du" in ord:
            nya_ord[i] = nya_ord[i].replace("du", "jag")
        elif "dig" in ord:
            nya_ord[i] = nya_ord[i].replace("dig", "mig")
        elif "mamma" in ord:
            mamma = (random.choice(mammasvar))
            print(mamma)
            log(mamma)
        elif "pappa" in ord:
            pappa = (random.choice(pappasvar))
            print(pappa)
            log(pappa)
    if "nej" in urspr_ord or "aldrig" in urspr_ord:
        randomnegativa = (random.choice(negativa))
        print(randomnegativa)
        log(randomnegativa)
    elif nya_ord == urspr_ord:
        randompositiva = (random.choice(positiva))
        print(randompositiva)
        log(randompositiva)
    else:
        svar = " ".join(nya_ord)
        print(svar)
        log(svar)


def main():
    print("**************************************************")
    print()
    print(" Välkommen till Elizas mottagning ")
    print()
    print("**************************************************")
    print()
    print('(Du kan sluta när som helst genom att svara "hejs svejs" eller "god natt")')
    print()
    print('Berätta för mig om dina problem...')

    while True:
        text = input("\n> ")
        text = text.lower()
        log(text)
        if text == "hejs svejs":
            randompositiva = (random.choice(positiva))
            print(randompositiva)
            log(randompositiva)
            print('Tack för besöket. Betala in 150 EUR på mitt konto.')
            sluttext = "Tack för besöket. Betala in 150 EUR på mitt konto."
            log(sluttext)
            break
        elif text == "god natt":
            randompositiva = (random.choice(positiva))
            print(random.choice(positiva))
            log(randompositiva)
            print('Tack för besöket. Betala in 150 EUR på mitt konto.')
            sluttext = 'Tack för besöket. Betala in 150 EUR på mitt konto.'
            log(sluttext)
            break
        else:
            svar(text)


main()
