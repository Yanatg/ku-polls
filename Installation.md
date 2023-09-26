# KU Polls Installation Guide
This guide will walk you through the installation and setup process for the KU Polls application.

## Requirements
* Requires Python 3.9 or newer.
* Required Python packages are listed in [requirements.txt](./requirements.txt).

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

    For Windows:
    ```
    venv\Scripts\activate
    ```
    For Linux/Mac:
    ```
    source venv/bin/activate
    ```

5. Install required packages.
    ```
    pip install -r requirements.txt
    ```
   
6. Create a file named `.env` in the same directory as `manage.py`. or copy the 'sample.env' file
   
    For Windows:
    ```
    copy sample.env .env
    ```
    For Linux/Mac:
    ```
    cp sample.env .env
    ```
   
7. Run migrations.
    ```
    python manage.py migrate
    ```
8. Install Data from Data Fixture.
    ```
    python manage.py loaddata data/polls-no-vote.json     
    python manage.py loaddata data/users.json
    ```
    
   
## Running the Application

1. Run the application.
    ```
    python manage.py runserver
    ```
2. Open the application in a browser at http://localhost:8000/ or 127:0.0.1:8000
3. To stop the application, press `Ctrl+C` in the terminal window where it is running.
4. To deactivate the virtual environment, run `deactivate` in the terminal window where it is running.
    ```
    deactivate
    ```
The application is now installed and configured. You will see the polls questions on index page.

## Run Tests
1. Run the tests.
    ```
    python manage.py test polls
    ```
