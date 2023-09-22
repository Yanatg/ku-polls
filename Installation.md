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
   
6. Create a file named `.env` in the same directory as `manage.py`.
7. Set the value of `SECRET_KEY` in `.env` to a random string of characters.

   see the example in `.env.example`
    ```
    SECRET_KEY=your_secret_key
    ```
8. Run migrations.
    ```
    python manage.py migrate
    ```
9. Create a superuser.
    ```
    python manage.py createsuperuser
    ```
10. Install Data from Data Fixture.
    ```
    python manage.py loaddata data/polls-no-vote.json     
    python manage.py loaddata data/users.json
    ```
    
   
## Running the Application
1. Change directory to the repository.
    ```
    cd ku-polls
    ```
2. Activate the virtual environment.
    
    For Windows:
    ```
    venv\Scripts\activate
    ```
    For Linux/Mac:
    ```
    source venv/bin/activate
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
The application is now installed and configured. You will see the polls questions on index page.

## Run Tests
1. Change directory to the repository.
    ```
    cd ku-polls
    ```
2. Activate the virtual environment.
3. Run tests.
    ```
    python manage.py test
    ```
4. To deactivate the virtual environment, run `deactivate` in the terminal window where it is running.
    ```
    deactivate
    ```
   
