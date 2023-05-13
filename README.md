# Time-Blocker
This repository contains two Python scripts, Bmais.py and BmaisTask.py, which are designed to monitor and control system processes.

Bmais.py
The Bmais.py script is responsible for monitoring and blocking time changes on the computer system. It utilizes various libraries and APIs to achieve its functionality.

Dependencies:

requests: Used for making HTTP requests to the time API.
datetime: Used for handling date and time objects.
win32api: Provides access to system-level APIs for Windows.
time: Provides time-related functions.
os: Provides operating system-related functions.
logging: Used for logging messages and events.
plyer: Used for displaying notifications.
psutil: Provides system and process-related functions.
subprocess: Used for launching and managing subprocesses.
socket: Used for retrieving the hostname of the computer.
Usage:

Make sure all the dependencies are installed on your system.
Replace the values of variables notification_title1, notification_message1, notification_icon1, notification_title2, notification_message2, log_file, main_script, and main_script_path with appropriate values for your use case.
Execute the script.
The script continuously checks the current time from a time API. If the time is within a specific tolerance range, no action is taken. Otherwise, the script attempts to change the system time to match the received time. If the time change is successful, a notification is displayed. Any errors encountered during the process are logged. The script also monitors the presence of a file (C:\\ever1401.txt) and terminates if the file exists.

BmaisTask.py
The BmaisTask.py script is responsible for monitoring and restarting a specific process on the computer system.

Dependencies:

psutil: Provides system and process-related functions.
subprocess: Used for launching and managing subprocesses.
time: Provides time-related functions.
logging: Used for logging messages and events.
socket: Used for retrieving the hostname of the computer.
os: Provides operating system-related functions.
Usage:

Make sure all the dependencies are installed on your system.
Replace the values of variables main_script and main_script_path with appropriate values for your use case.
Execute the script.
The script continuously checks if a specific process is running. If the process is not running, it is restarted. The script also monitors the presence of a file (C:\\ever1401.txt) and terminates if the file exists.

Please note that these scripts are provided as examples and may require modifications to suit your specific use case. Make sure to read and understand the code before executing it.
