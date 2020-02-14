# Python-MongoDB-CV-Application-With-Gui

# What is this application ?
This is an testing python application for storing user's CV in a list using PyQt5 graphics and storing user's info
in a mongo database

# Requirements
* Python3.6.9
* setuptools (39.0.1)
* PyQt5 5.14.0
* pymongo 3.10.1
* MongoDB 4.0.4 - Database Server
* (Optional)MongoDB Compass - To view database
* (might add more later)

# How to run the program
1. Start localhost mongod ($sudo mongod)
2. Run controller_ui.py

# What does this application do so far:
1. Uses gui to insert/delete user's CV with name,description and image
2. User images are saved and updated outside the database (/image_of_profiles) for further processing 

# Todo list: 
* Upon opening the app, load all user profiles in the widget list
* Add a debug  make a white qlabel go instantly green and then progressively white again
with text indicating a successful insertion