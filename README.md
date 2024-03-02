## Directory Watcher

### Overview
This script is designed to monitor a specified directory for any changes, including file creations, deletions, modifications, and moves. It utilizes the `pyinotify` library to achieve this functionality.

### Motivation
The primary motivation behind this script is to provide a tool for monitoring directories in real-time, allowing users to stay informed about any changes occurring within them. This can be particularly useful in various scenarios, such as:

- Keeping track of modifications made to important files or directories.
- Monitoring directories for incoming files or data streams.
- Automating tasks based on changes detected within a directory.

### Features
- Watches a specified directory for various types of events, including file creations, deletions, modifications, and moves.
- Provides real-time notifications for each detected event.
- Automatically handles permissions errors and missing directories.
- Utilizes the `pyinotify` library for efficient event monitoring.

### Installation
To use this script, ensure you have Python 3 installed on your system.
to install dependencies on archlinux:
```shell
sudo pacman -Syu extra/python-click extra/python-pyinotify
```

then just `sudo cp zfsmtime/zfsmtime.py /usr/bin/zfsmtime && sudo chmod +x /usr/bin/zfsmtime`

#### Systemd
There is a sample service script available, you probably want to edit the `User=` and the folder to watch then install with:
```shell
sudo cp systemd/zfsmtime.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now zfsmtime
```

### Usage
1. **Running the Script:** Execute the script with Python, providing the directory you want to monitor as an argument:

   ```
   zfsmtime watch /path/to/directory
   ```

2. **Monitoring:** Once the script is running, it will continuously monitor the specified directory for any changes.

3. **Handling Permissions Errors:** If the script encounters a permission error while attempting to access a directory, it will log the error and continue monitoring other directories.

### Example
Suppose you want to monitor the directory `/var/log` for any changes. You can use the script as follows:

```
zfsmtime watch /var/log
```
