
#
#
import machine
from time import sleep


#
#
DELAY = 0.4

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
    pass

# a function to initiate the servo connectoins
# and append them to seroves list
# then set the Bot to straight pos
#
def init():
    for pin in PINS:
        m_pin = machine.Pin(pin)
        servo = machine.PWM(m_pin, freq=50)
        SERVOS.append(servo)


    idle()


#
#
def move():

    SERVOS[0].duty(96)
    SERVOS[1].duty(96)
    SERVOS[2].duty(77)


#
#
def move2():
    SERVOS[0].duty(50)
    sleep(DELAY)

    SERVOS[1].duty(55)
    sleep(DELAY)

    SERVOS[2].duty(120)
    sleep(DELAY)



#
#
def move3():
    SERVOS[0].duty(120)
    sleep(DELAY)

    SERVOS[1].duty(55)
    sleep(DELAY)

    SERVOS[2].duty(40)
    sleep(DELAY)



# this function sets each servo to it's straight value
#
def idle():
    SERVOS[0].duty(77+15)
    sleep(DELAY)
    SERVOS[1].duty(60)
    sleep(DELAY)
    SERVOS[2].duty(77)
    sleep(DELAY)



#
#
# if the middle part is lifted it turnes right,
def test_motion():

    try:
        while True:
            move2()
            sleep(DELAY)
            move3()
            sleep(DELAY)

    except KeyboardInterrupt:
        print("Force stoped, going to Straight posision...")
        idle()





if __name__ == "__main__":
    main()