# App Installation Guide

This guide will help you install and run the app on your system.

## Prerequisites

Before proceeding with the installation, ensure that you have the following installed on your system:

- Chromium
- Lightweight desktop
- Git

## Installation Steps

1. Install Chromium, lightweight desktop, and Git using the `dietpi-software` command.

2. Clone the app from the following repository: https://github.com/OuerghieHoussem1/dist-app-last.git

3. Grant permission to run scripts from the scripts folder by running the following commands:

    ```bash
    cd scripts
    chmod +x *.*
    ```

4. Install libraries by running the `install_python_libs.sh` file:

    ```bash
    ./install_python_libs.sh
    ```

5. Go back to the main app folder and run the app by running the `test_app.py` file:

    ```bash
    cd ..
    python3 test_app.py
    ```

6. Open Chromium and go to http://localhost:5000/

7. Test the app. If everything works, you just have to configure autolaunch.

8. Go to the dietpi-config menus by running the `dietpi-config` command and go to autostart options and choose Chromium and write "http://localhost:5000/" as the default link.

9. Go to the postboot directory by running the command `cd /var/lib/dietpi/postboot.d`.

10. Create a file called `run_app.sh` by using the command `nano run_app.sh`.

11. In the file, write this:

    ```bash
    #!/bin/bash

    cd /root
    echo "Starting app now"
    cd dist-last-app
    python3 test_app.py
    ```

12. Save the file by clicking `ctrl-x` and then `Y`.

13. Grant it permissions by running the command `chmod +x *.*`.

14. Reboot your system.
