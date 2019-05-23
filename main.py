
#
#
import machine
from time import sleep

#
#
SERVOS = []
PINS = [18, 5, 17]


"""
PIN_1 = machine.Pin(18)
PIN_2 = machine.Pin(5)
PIN_3 = machine.Pin(17)

# create
#
SERVO_1 = machine.PWM(PIN_1, freq=50)
SERVO_2 = machine.PWM(PIN_2, freq=50)
SERVO_3 = machine.PWM(PIN_3, freq=50)
"""

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
        servo = machine.PWM(m_pin, freq=50)
        SERVOS.append(servo)


    straight()


#
#
def move():
    # move the
    #
    #while True:
        # the plus 20 is for the caliprating the head
        #
    SERVOS[0].duty(96)
    SERVOS[1].duty(96)
    SERVOS[2].duty(77)


#
#
def move2():
    SERVOS[0].duty(50)
    sleep(0.4)

    SERVOS[1].duty(60)
    sleep(0.4)

    SERVOS[2].duty(40)
    sleep(0.4)



#
#
def move3():
    SERVOS[0].duty(160)
    sleep(0.4)

    SERVOS[1].duty(77)
    sleep(0.4)

    SERVOS[2].duty(120)
    sleep(0.4)



# this function sets each servo to it's straight value
#
def straight():
    SERVOS[0].duty(77+20)
    #sleep(0.5)
    SERVOS[1].duty(60)
    #sleep(0.5)
    SERVOS[2].duty(77)


#
#
def test_motion():

    try:
        while True:
            move2()
            #sleep(2)
            move3()
            #sleep(2)

    except KeyboardInterrupt as err:
        print("Force stoped, going to Straight posision...")
        straight()





if __name__ == "__main__":
    main()