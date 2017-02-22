learning_journal README
==================

This is a starting point for Session 7. It picks up where we left off at the end of session 6
but with the following changes:

- added User class to mymodel.py

- added some database imports to scripts/initializedb.py

- added an EntryEditForm class to forms.py

- added home and edit buttons in templates/detail.jinja2

- fleshed out the update view in views/default.py

- added some images and fun css files


Getting Started
---------------

- with your virtual environment active:

Get into the right directory
- cd <directory containing development.ini>

Install all the setup files
- run: python setup.py develop

Create the database
- run: setup_db development.ini

Start the server
- run: pserve development.ini

It will be running on localhost:6543

- included are the basic static/styles.css that we started with plus
-styles_hiking.css
-styles_spooky.css

To switch which file the app is using, change the name of styles.css to
something else, and rename the one you want to use to styles.css.
Restart your server and clear your cache to see the change.
