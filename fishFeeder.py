import RPi.GPIO as GPIO
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
EMAIL_ADDRESS = '<sender email>'
EMAIL_PASSWORD = '<gmail app password>'  # App specific password if you're using gmail
TO_EMAIL_ADDRESS = 'recipient email'
SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587

# Set up logging
logging.basicConfig(filename='~/fish_feeder.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s>
# Set up GPIO pin
SERVO_PIN = 14 # Set GPIO pin to data pin of servo

GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set up PWM on the servo pin at 50Hz (common for servos)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def set_servo_angle(angle):
    # Convert the angle to a duty cycle
    duty_cycle = 2.5 + (angle / 18.0)
    pwm.ChangeDutyCycle(duty_cycle)
    logging.info(f'Servo angle set to {angle} degrees')

def sendEmail():
    msg = MIMEMultipart()
    msg['From'] = f'<{EMAIL_ADDRESS}>'
    msg['To'] = TO_EMAIL_ADDRESS
    msg['Subject'] = 'Fish has been fed successfully!'
    body = r'\(ˆ˚ˆ)/'
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL_ADDRESS, text)
        server.quit()
        logging.info('Email sent successfully.')
    except Exception as e:
        logging.error(f'Failed to send email: {e}')

try:
    logging.info('Starting fish feeder script')

    # Ensure angle is set to 0 initially
    set_servo_angle(0)
    time.sleep(1)

    # Move the servo to 180 degrees to release food
    set_servo_angle(180)
    time.sleep(1)

    # Return to 0 degrees
    set_servo_angle(0)
    time.sleep(1)

    logging.info('Fish feeder script completed successfully')
    sendEmail()
except Exception as e:
    logging.error(f'Error occurred: {e}')
finally:
    # Clean up
    pwm.stop()
    GPIO.cleanup()
    logging.info('Cleaned up GPIO')
