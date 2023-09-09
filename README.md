# KU Polls
## Online Polls questions

An application for conducting a poll or survey with multiple-choice questions, written in Python using Django. It is based on the [Django tutorial project][django-tutorial], and adds additional functionality.

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

## Requirements

Requires Python 3.9 or newer.  Required Python packages are listed in [requirements.txt](./requirements.txt).

## Install and Configure the Application

1. Clone the repository.
```
git clone https://github.com/Yanatg/ku-polls.git
```
2. Change directory to the repository.
```
cd ku-polls
```
3. Create a virtual environment.
```
python -m venv venv
```
4. Activate the virtual environment.
```
venv\Scripts\activate
```
5. Install required packages.
```
pip install -r requirements.txt
```


## Running the Application

1. Change directory to the repository.
```
cd ku-polls
```
2. Activate the virtual environment.
```
venv\Scripts\activate
```
3. Run the application.
```
python manage.py runserver
```
4. Open the application in a browser at http://localhost:8000/ or 127:0.0.1:8000
5. To stop the application, press `Ctrl+C` in the terminal window where it is running.
6. To deactivate the virtual environment, run `deactivate` in the terminal window where it is running.
```
deactivate
```

## Demo User Accounts

to be added.

## Project Documents

All project-related documents are in the [Project Wiki](../../wiki/Home)

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Development Plan](../../wiki/Development%20Plan)

### Iterations
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](https://github.com/users/Yanatg/projects/1/views/2?filterQuery=iteration+1)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan) and [Task Board](https://github.com/users/Yanatg/projects/1/views/3?filterQuery=iteration+2)

[![Django CI](https://github.com/Yanatg/ku-polls/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/Yanatg/ku-polls/actions/workflows/django.yml)

[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
