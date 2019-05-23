
#
#
import machine
from time import sleep

#
#
SERVOS = []
PINS = [18, 5, 17]


#
#
def main():
        move()


# a function to initiate the servo connectoins
# and append them to seroves list
# then set the Bot to straight pos
#
def init():
    for pin in PINS:
        m_pin = machine.Pin(pin)
        servo = machine.PWM(m_pin, feq=50)
        SERVOS.append(servo)


    straight()



def move():
    # move the
    #
    #while True:
        # the plus 20 is for the caliprating the head
        #
    SERVOS[0].duty(96)
    SERVOS[1].duty(96)
    SERVOS[2].duty(77)
    sleep(1)

        #straigh()



        #straigh()

def move2():
    SERVOS[0].duty(50)
    SERVOS[1].duty(40)
    SERVOS[2].duty(40)
    sleep(1)



def move3():
    SERVOS[0].duty(160)
    SERVOS[1].duty(70)
    SERVOS[2].duty(120)
    sleep(1)


def straight():
    SERVOS[0].duty(77+20)
    SERVOS[1].duty(60)
    SERVOS[2].duty(77)
    sleep(1)









if __name__ == "__main__":
    main()