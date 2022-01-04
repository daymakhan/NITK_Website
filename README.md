# Online NITK website and management Software
A replication of  https://nitk.ac.in/.


# Software Requirements : 
    Browser : Google Chrome, Firefox, etc.
    Code Editor : Visual Studio Code, Sublime Text, etc.
   
# Technology Stack : 
    Frontend : HTML, CSS, Javascript,Bootstrap
    Backend : Python Django Framework.
    Database : SQLite
    
# Directory Structure 
- The Main Folder Contains subfolders for project and app, readme.md file. 
- Within app folder, we have 3 folders :  static - containing images, scripts and stylesheets; templates - containing HTML pages pycache : containing python logs; and files like views.py, urls.py, admin.py etc. 
- Project folder contains 5 files : init.py : __init__.py, asgi.py, settings.py, urls.py, wsgi.py. Also, there is a database file db.sqlite3.


# How to run:
1. Create a virtual environment: virtualenv env
2. Activate it : source env/bin/activate
3. Install django : pip install django
4. Run the server : python manage.py runserver
