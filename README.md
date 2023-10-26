
# LAN File Sharing

This is a python based program which creates a connection between two devices that are connected to the same local are network (LAN) and let's the user transmit and receive data directly without any other device or server in between them.

## Installation

Install the Server and Client programmes using git.

```bash
  git clone https://github.com/jeeban-jyoti/LAN-File-Sharing.git
```

Below methods are mentioned to run Main-v0.0.1.py on system startup so that everyone in the network can download the file that you save in the source folder in your desktop.

For Windows:-
1) Open Run command box by pressing the Windows logo + R keys. In the Run command field, type shell: Startup and then press Enter key to open Startup folder.
2)Copy and paste the Main-v0.0.1.py shortcut from the desktop to this Startup folder and the app is added to startup.

For Linux:-
1) Add " python3 /home/ec2-user/Main-v0.0.1.py " to last line of " /etc/rc.d/rc.local" file
2) execute " chmod +x /etc/rc.d/rc.local " in terminal.

   For Mac:-
1) Click the Apple menu in the top-left corner and select System Preferences. Then choose Users & Groups.
2) Click the Login Items tab to see your list of startup programs.
3) Add the Main-v0.0.1.py to the list.

## Screenshots

<img width="1512" alt="Screenshot 2023-10-26 at 4 30 52 PM" src="https://github.com/jeeban-jyoti/LAN-File-Sharing/assets/72793803/517a2d35-4854-4a80-af77-85e0b4ae9f78">

<img width="1512" alt="Screenshot 2023-10-26 at 4 30 36 PM" src="https://github.com/jeeban-jyoti/LAN-File-Sharing/assets/72793803/10272f0c-39f0-4dea-a5a5-018e98333b4d">


## Usage

• Run the socket_client.py file as a python file  and give the ip address of the device to which you want to connect.

• It will connect to the device and there you can see the list of files and folders that you can access.

• Note - You can download only files and not folders.

• To see the contents of a folder type the path of folder assuming the initial location as root.

• To download any file type "fetch" before the filename.(Must give the complete filepath assuming the inital location as root)
## Authors

- [Jeeban Jyoti Patra](https://github.com/jeeban-jyoti)

