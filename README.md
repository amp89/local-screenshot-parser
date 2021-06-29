# local-screenshot-parser
Simple Django / Vue app to parse text from screenshots locally

Easily parse and search through text from screenshots.

![image](https://user-images.githubusercontent.com/16569440/123744849-9acb1480-d86c-11eb-9009-5ddd58c92422.png)


# NOTE: THIS IS ONLY DESIGNED TO BE RAN LOCALLY ON LOCALHOST!

## Features
- Search through text in screenshots
- Get a link to the original image on your system
- Search results are cached in an SQLite database until the search is ran again


## How to setup:

1. Clone
2. Install requrements from `requirements.txt`. **You must have tesseract installed on your system for this to work.** See https://pypi.org/project/pytesseract/ for details
3. run `python manage.py migrate` to create your database
4. Make note of the **full** path of the directory where your screenshots are located. It will look through directories recursively, but it is best if it has only images in it.


## How to use (Option 1):
1. `python manage.py migrate` if you haven't already
2. `python manage.py runserver`
3. go to `localhost:8000` in your browser
4. Put the **full path** to the directory in which your screenshots are located.
5. Click search. This may take several minutes depending on how many images are in the directory, and how big they are.
6. The results will show up when it is complete. If you turn the server off or close the browser before it is finished, you will have to start over.  Otherwise, the results are stored in an SQLite database.


## How to use (Option 2):
1. `python manage.py migrate` if you haven't already
2. `python manage.py parse_screenshots --path /full/path/to/your/screenshots/`
3. After step two, it will say "Done Parsing"
4. `python manage.py runserver`
5. go to `localhost:8000` in your browser
6. The results will show up here. if you search again from the UI, it may take serveral minutes to complete. Search results are cached in an sqlite database.



