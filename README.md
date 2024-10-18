Foreword:
GotoGro-MRMS is built on a python base with django dependencies, hosted on a local server. Please follow the instructions below for this program to be able to work on your systems.

________________________________________
Install Python
1.	Download Python:
•	Visit the official Python website and download the latest stable version (preferably Python 3.9 or later).
https://www.python.org/downloads/

3.	Install Python:
•	Run the installer and follow the prompts.
•	Important: During installation, check the box that says “Add Python to PATH”.

4.	Verify Installation:
•	Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux).
•	Run in cmd / terminal: python --version

Install Visual Studio Code
1.	Download VS Code:
•	Visit the VS Code website and download the appropriate installer for your operating system.

2.	Install VS Code:
•	Run the installer and follow the prompts.

Install Git
1.	Download Git:
•	Visit the Git website and download the installer for your OS.
https://git-scm.com/downloads

3.	Install Git:
•	Run the installer and follow the prompts.

4.	Verify Installation:
•	Open your terminal and run: git --version
________________________________________
Install Django
1.	Open VS Code Terminal:
•	Open VS Code.
•	Open the integrated terminal by pressing Ctrl+` or navigating to View > Terminal.

2.	Create a Project Directory:
•	Terminal (RUN ONCE): -- mkdir member_management
•	Terminal (RUN ONCE): -- cd member_management

3.	Set Up a Virtual Environment:
•	It’s good practice to use a virtual environment to manage dependencies.
•	Terminal (RUN ONCE): python -m venv env

Activate the Virtual Environment:
4.	Windows (ALWAYS START FIRST):
•	Terminal: env\Scripts\activate

5.	macOS/Linux (ALWAYS START FIRST):
•	Terminal: source env/bin/activate

6.	Upgrade pip (RUN ONCE)
•	pip install --upgrade pip

Install Django
•	Terminal and run (RUN ONCE): pip install django
•	Verify Django Installation using terminal:  django-admin –version


________________________________________
Create a New Django Project
7.	Start a New Project:
•	Terminal (RUN ONCE): django-admin startproject GotoGroMRMS

8.	Navigate to the Project Directory:
•	Terminal (ALWAYS): cd GotoGroMRMS

9.	Run the Development Server:
•	Terminal (RUN ALWAYS): python manage.py runserver
•	Open your browser and go to http://127.0.0.1:8000/ to see the Django welcome page.

Stop the Server: Press Ctrl+C in the terminal.

Basic Setup after Initialization

Windows (ALWAYS START FIRST):
Terminal: env\Scripts\activate

macOS/Linux (ALWAYS START FIRST):
Terminal: source env/bin/activate

Navigate to the Project Directory:
Terminal (ALWAYS): cd GotoGroMRMS

Run the Development Server:
Terminal (RUN ALWAYS): python manage.py runserver
Note: if cannot try the option below-
python manage.py runserver 127.0.0.1:8080    
