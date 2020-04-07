# statement-of-works

This project allows for the automatic generation of Statement of Works forms, created as part of the 2020 Data Hub Firebreak week.

## Setup Instructions

1. Clone this repository, then create and activate a virtual environment
2. Run `requirements.txt` by using `pip install -r example-requirements.txt`
3. Run the commands `python manage.py makemigrations` and `python manage.py migrate` to set up the database
4. Go into the `frontend` directory and run `npm install` to install the required frontend packages, then run `npm run dev` to compile them
5. Go back to the project root and run `python manage.py runserver` to start the project
6. The project is viewable at http://localhost:8000
