# DjangoShare
Django project to upload and share photos online!

## Installation

First, clone the repository.
Then, move to this directory. (Windows only)

```git clone
git clone https://github.com/JoonasHeinonen/DjangoShare

cd DjangoShare
```

Installing virtualenvironment will require these steps:

```venv
virtualenv venv
```

Then, activate the virtual environment:

```
venv\Scripts\activate
```

Next, move to the folder itself:

```
cd djangoshare
```

Install requirements from requirements.txt-file:

```
pip install -r requirements.txt
```

Run database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

And now, run the software itself.

```
python manage.py runserver
```

Congrats! You're ready to run the software!