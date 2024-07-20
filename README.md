# Automatic Fish Feeder with Raspberry Pi

This project uses a Raspberry Pi to control an SG-90 servo motor for feeding fish automatically. The servo is scheduled to rotate and dispense food at a specific time every day. It also sends an email notification whenever the feeding process is completed.
<img src="https://github.com/user-attachments/assets/0b893b78-51a2-4768-be4d-f9ca62e84620" alt="Servo motor for this project" width="300" height="300">

## Components

- Raspberry Pi 4
- Servo motor (The one the code is configured for is the SG-90 Micro Servo Motor)

  [Datasheet](https://www.friendlywire.com/projects/ne555-servo-safe/SG90-datasheet.pdf)
- Internet connection for email notifications

## Features

- Automatically feeds fish at a scheduled time.
- Sends email notifications when the fish is fed.
- Logs feeding actions for troubleshooting.

## Prerequisites
- An internet connection
- An email account for sending email notifications

## Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/Mustaali256/Automatic-fish-feeder.git
    cd Automatic-fish-feeder/
    ```

2. **Install Required Libraries**

    ```sh
    sudo apt-get update
    sudo apt-get install python3-rpi.gpio python3 smtplib
    ```

3. **Set Up the Python Script**

    Update the email configuration in `fishFeeder.py`:

    ```python
    EMAIL_ADDRESS = '<sender email>'
    EMAIL_PASSWORD = '<gmail app password>'
    TO_EMAIL_ADDRESS = '<recipient email>'
    ```
    Update the pin used for the servo motor:
   ```python
    SERVO_PIN = 14 # Set GPIO pin to data pin of servo
    ```

## Usage

1. **Run the Script Manually**

    To test the script, you can run it manually:

    ```sh
    sudo python3 fishFeeder.py
    ```

2. **Set Up a Scheduled Task with Crontab**

    Edit your crontab to schedule the script to run every day at 11 AM:

    ```sh
    crontab -e
    ```

    Add the following line to the crontab file (make sure the path to the file is correct):

    ```sh
    0 11 * * * sudo python3 ~/Automatic-fish-feeder/fishFeeder.py # Set to 11am everyday
    ```
    You can connect a drum to the servo motor which will dispense fish food out of a hole one it rotates 180 degrees.
## Gmail
  If you are using a Gmail account to send the confirmation email, you will need to turn on two-factor authentication and [set an app-specific password](https://myaccount.google.com/apppasswords) which you will use to replace your password in the `fishFeeder.py` file.
  For example, if your app password looks like this:
  ```
  abcd efgh ijkl mnop
  ```
  then set the EMAIL_PASSWORD variable to this:
  ```python
  EMAIL_PASSWORD = 'abcdefghijklmnop'
  ```
## Troubleshooting

- **Power Issues**: Ensure the Raspberry Pi and servo motor are properly powered. A more powerful power supply might be needed.
- **Servo Motor Issues**: Check connections and ensure the servo pin has been set to the pin mentioned in the Python file. you may want to check your servo's datasheet for PWN timing if it is different.
- **Email Sending Issues**: Verify email credentials and internet connection.
- **Log Files**: Check `~/fish_feeder.log` for detailed logs.
