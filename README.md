# My_samplesite

This project allows you to place discounts and sales on fishing equipment.

## Getting Started

These instructions will get you a copy of the project up and run on your local machine for development and testing purposes.

### Prerequisites

The Python 3.8 should be installed on your local machine.

### Installing

To run locally, do the usual:
1. Create a Python 3.8 venv in project directory and activate it.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set your SECRET_KEY in my_samplesite/settings.py:

```
SECRET_KEY = 'YOUR_KEY'
```

4. Set your own parameters for database in my_samplesite/settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': '...'
        ...
    }
}
```

5. Apply migrations:

```
python manage.py migrate
```

6. Create a superuser:

```
python manage.py createsuperuser
```

7. Run the server:

```
python manage.py runserver
```

## Built With

* [Django](https://docs.djangoproject.com/en/4.0/) - The web framework used


## Author

* **Danil Dvorchuk** 



