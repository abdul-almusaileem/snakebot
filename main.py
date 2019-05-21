
#
#
import machine
from time import sleep

# define the pins for each servoe
#
PIN_1 = machine.Pin(18)
PIN_2 = machine.Pin(5)
PIN_3 = machine.Pin(17)

# create
#
SERVO_1 = machine.PWM(PIN_1, freq=50)
SERVO_2 = machine.PWM(PIN_2, freq=50)
SERVO_3 = machine.PWM(PIN_3, freq=50)


#
#
SERVOS = [SERVO_1, SERVO_2, SERVO_3]


#
#
def main():
        move()



def move():
    # move the
    #
    #while True:
        # the plus 20 is for the caliprating the head
        #
    SERVOS[0].duty(96)
    SERVOS[1].duty(96)
    SERVOS[2].duty(96)
    sleep(1)

        #straigh()



        #straigh()

def move2():
    SERVOS[0].duty(50)
    SERVOS[1].duty(40)
    SERVOS[2].duty(40)
    sleep(1)


def straigh():
    SERVOS[0].duty(77+20)
    SERVOS[1].duty(77-20)
    SERVOS[2].duty(77)
    sleep(1)









if __name__ == "__main__":
    main()