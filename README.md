# browser_with_python


This code will create a browser window with Google loaded on the main page. If you want to further customize your browser, you can use more PyQt5 modules to add navigation buttons, address bars, etc.

## facility

To install PyQt5 on Ubuntu, you first need to make sure you have Python installed and pip, which is the Python package manager. If you don't have Python installed, you can install it with the following command:

- _sudo apt-get install python3_

Once you have Python installed, you can install pip with the following command:

- _sudo apt-get install python3-pip_

Once you have pip installed, you can install PyQt5 with the following command:

- _pip3 install PyQt5_

This command will download and install the latest stable version of PyQt5. Once the installation is complete, you will be able to import PyQt5 into your Python scripts and start running the script.

## possible errors

1: "error: ModuleNotFoundError: No module named 'PyQt5.QtWebEngineWidgets'"
- pip3 install PyQt5-sip PyQt5
- pip install PyQtWebEngine
This command will install the QtWebEngineWidgets module along with the modules needed to make it work. Once the installation is complete, you should be able to import QtWebEngineWidgets without issue.

2: qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found. This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

 install the xcb dependency (found at https://wiki.qt.io/Building_Qt_5_from_Git )
- _apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev_ 

