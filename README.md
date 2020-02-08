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


# What does this application do so far:
1. Uses gui to insert/delete user's CV with name,description and image ( /gui/cotroller.ui.py)
2. Connects to a localhost mongo database (not implemented yet) ( /Mongo/main_mongo.py)

# Todo list:
* make images have an ID, save the image on a folder.
* When an insert action is successful, make a white qlabel go instantly green and then progressively white again
with text indicating a successful insertion
* Finally, connect the profiles to the database with working inserts/deletes
* On open app, load profiles
