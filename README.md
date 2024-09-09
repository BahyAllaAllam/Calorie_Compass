# Calorie Compass

## About
Calorie Compass is a platform where we share our thoughts, experiences, and inspiration to motivate you in your weight loss journey. We believe that with the right tools and support, anyone can achieve their goals.

## Installation

### Prerequisites
- Python 3.10 or higher (download from [here](https://www.python.org/downloads/))
- Virtualenv

### Steps
1. **Install Python 3.10 or higher**:  
   Download and install Python from [here](https://www.python.org/downloads/).

2. **Install Virtualenv** (if not already installed):  
   ```sh
   pip install virtualenv

3. **Create a Virtual Environment**:
   ```sh
   virtualenv src

4. **Activate the Virtual Environment**:
    - **On Windows**:
        ```sh
        src\Scripts\activate
    - **On macOS/Linux**:
        ```sh
        source src/bin/activate

5. **Install Required Packages**:
    ```sh
    pip install -r req.txt

6. **Create the Django Project**:
    ```sh
    django-admin startproject calorie_compass

7. **Create the Necessary Apps**:
    For example, to create the `users` app:
    ```sh
    django-admin startapp users
    ```

8. **Replace Project Files**:
    Replace your project files with the provided files.

9. **Migrate Changes to the Database**:
    ```sh
    python manage.py makemigrations
    python manage.py migrate

10. **Run the Project**:
    ```sh
    python manage.py runserver

# Enjoy!