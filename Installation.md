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
The application is now installed and running. In the index page you should see 
the list of poll questions.