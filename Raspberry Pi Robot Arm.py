# Raspberry Pi Robot Arm using Python

import RPi.GPIO as GPIO
import time

# GPIO mode

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Servo GPIO pins

BASE = 17
SHOULDER = 18
ELBOW = 27
GRIPPER = 22

# Setup servo pins

for pin in [BASE, SHOULDER, ELBOW, GRIPPER]:
GPIO.setup(pin, GPIO.OUT)

# Create PWM objects

base_servo = GPIO.PWM(BASE, 50)
shoulder_servo = GPIO.PWM(SHOULDER, 50)
elbow_servo = GPIO.PWM(ELBOW, 50)
gripper_servo = GPIO.PWM(GRIPPER, 50)

# Start PWM

base_servo.start(0)
shoulder_servo.start(0)
elbow_servo.start(0)
gripper_servo.start(0)

def set_angle(servo, angle):
# Convert angle to duty cycle
duty = 2 + (angle / 18)

```
servo.ChangeDutyCycle(duty)
time.sleep(0.5)
servo.ChangeDutyCycle(0)
```

def move_robot_arm():
print("\n===== RASPBERRY PI ROBOT ARM =====")

```
# Move base
print("Moving Base...")
set_angle(base_servo, 90)

# Move shoulder
print("Moving Shoulder...")
set_angle(shoulder_servo, 60)

# Move elbow
print("Moving Elbow...")
set_angle(elbow_servo, 120)

# Open gripper
print("Opening Gripper...")
set_angle(gripper_servo, 30)

time.sleep(1)

# Close gripper
print("Closing Gripper...")
set_angle(gripper_servo, 80)

print("Robot Arm Movement Completed.")
```

try:

```
while True:
    print("\n===== ROBOT ARM MENU =====")
    print("1. Move Robot Arm")
    print("2. Reset Arm")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        move_robot_arm()

    elif choice == "2":
        print("Resetting Robot Arm...")

        set_angle(base_servo, 90)
        set_angle(shoulder_servo, 90)
        set_angle(elbow_servo, 90)
        set_angle(gripper_servo, 90)

        print("Robot Arm Reset.")

    elif choice == "3":
        print("Robot Arm System Closed.")
        break

    else:
        print("Invalid choice!")
```

finally:
base_servo.stop()
shoulder_servo.stop()
elbow_servo.stop()
gripper_servo.stop()

```
GPIO.cleanup()
```
