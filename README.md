## WELCOME TO MY FIRST DJANGO PROJECT 
### FIRST CREATE THE ENV 
```
-> To create the env - python -m venv environment_name 
-> To Activate the env - env_name\Scripts\activate
-> pip install psycopg2 
```
### Commmad to create the dajango project 
```
django admin startproject projectname
```
### manage.py 
```
manage.py file used to interact with the django application. 
```
### __init__.py 
```
This file is used to indicate the given file is the package.
```
### How to run the project on the server 
```
-> python manage.py runserver 
```
## HOW DJANGO WORKS  
```
What is an app ?

In Django, an "app" is a self-contained module that represents a single feature or functionality within a larger Django project, allowing for modular and reusable code organization 
```
### HOW DJANGO LOOK LIKE 
```
myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── __init__.py
    ├── templates/
    │   └── myapp/
    │       └── ...
    └── static/
        └── myapp/
            └── ...
```
Here's a brief explanation of each part:

* `__init__.py`: an empty file that tells Python this is a package
* `admin.py`: defines the admin interface for the app's models
* `apps.py`: defines the app's configuration
* `models.py`: defines the app's database models
* `tests.py`: contains tests for the app
* `urls.py`: defines the app's URL patterns
* `views.py`: defines the app's views (functions that handle HTTP requests)
* `migrations/`: contains database migration files
* `templates/`: contains HTML templates for the app
* `static/`: contains static files (e.g. images, CSS, JavaScript) for the app

```
What is view.py file ?

views.py : A file in Django where you define functions (views) that handle HTTP requests and return HTTP responses, typically rendering HTML templates or returning data in a specific format.
```
### BEFORE APPLYING MIGRATION 
```
We have to tell the django that we have made changes in the models.py file 
--> Use this --> python3 manage.py makemigrations appname 
```

### Basic View Function

```python
# views.py
from django.shortcuts import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

**Explanation**

This view function, `hello_world`, takes an HTTP request and returns a simple "Hello, World!" message as an HTTP response.
You can copy and paste this into your README file to display the code and explanation in a nice format.

### HOW TO CREATE APP IN DJANGO 
```
-> Use this command - python3 manage.py startapp appname
```
### **Django URL Routing & Request Handling Workflow**  

1️⃣ **User Request:** A user accesses `http://127.0.0.1:8000/food/` in the browser.  
2️⃣ **Project `urls.py`:** Django checks `EncubatorDemo/urls.py` and finds `path('food/', include('food.urls'))`.  
3️⃣ **App `urls.py`:** The request is forwarded to `food/urls.py`, where `path('', views.index, name='index')` maps it to the `index` view.  
4️⃣ **View Processing:** `food/views.py` runs the `index` function, which returns `HttpResponse("Welcome to the Food App!")`.  
5️⃣ **Response Sent:** Django sends this response back to the browser, displaying the message.  

---

### **Diagram (Add to README)**
Here's an ASCII diagram for your documentation:

```
User Request (http://127.0.0.1:8000/food/)
           │
           ▼
Project-Level URL Routing (EncubatorDemo/urls.py)
           │
           ▼
App-Level URL Routing (food/urls.py)
           │
           ▼
View Function Execution (food/views.py)
           │
           ▼
Response Sent to Browser (HTML/Text Output)
```

You can also create a **visual diagram** using tools like **draw.io** or **Excalidraw** and add it to your README file as an image (`.png` or `.svg`). 🚀

### Databases in Django

Django provides a high-level Python Web framework that encourages rapid development and clean, pragmatic design. One of its core features is the Object-Relational Mapping (ORM) system, which allows developers to interact with databases using Python code instead of SQL.

#### Setting Up the Database

1. **Configure the Database in `settings.py`**:
    ```python
    DATABASES = {
         'default': {
              'ENGINE': 'django.db.backends.postgresql',  # Use 'django.db.backends.sqlite3' for SQLite
              'NAME': 'your_db_name',
              'USER': 'your_db_user',
              'PASSWORD': 'your_db_password',
              'HOST': 'localhost',  # Set to empty string for localhost.
              'PORT': '5432',  # Set to empty string for default.
         }
    }
    ```

2. **Install the Database Adapter**:
    For PostgreSQL:
    ```sh
    pip install psycopg2
    ```

#### Creating Models

Models are Python classes that represent database tables. Each attribute of the model represents a database field.

```python
# models.py
from django.db import models

class Author(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()

class Book(models.Model):
     title = models.CharField(max_length=200)
     author = models.ForeignKey(Author, on_delete=models.CASCADE)
     published_date = models.DateField()
```

#### Making Migrations

1. **Create Migrations**:
    ```sh
    python manage.py makemigrations
    ```

2. **Apply Migrations**:
    ```sh
    python manage.py migrate
    ```

#### Querying the Database

Django ORM provides a powerful and intuitive way to query the database.

1. **Creating Records**:
    ```python
    author = Author(name='John Doe', email='john@example.com')
    author.save()
    ```

2. **Reading Records**:
    ```python
    authors = Author.objects.all()
    author = Author.objects.get(id=1)
    ```

3. **Updating Records**:
    ```python
    author = Author.objects.get(id=1)
    author.email = 'newemail@example.com'
    author.save()
    ```

4. **Deleting Records**:
    ```python
    author = Author.objects.get(id=1)
    author.delete()
    ```

#### Using the Django Admin Interface

Django comes with a built-in admin interface that allows you to manage your models.

1. **Register Models in `admin.py`**:
    ```python
    # admin.py
    from django.contrib import admin
    from .models import Author, Book

    admin.site.register(Author)
    admin.site.register(Book)
    ```

2. **Create a Superuser**:
    ```sh
    python manage.py createsuperuser
    ```

3. **Access the Admin Interface**:
    Run the server and navigate to `http://127.0.0.1:8000/admin/`.

This section provides a comprehensive overview of how to set up and use databases in Django, from configuration to querying and using the admin interface.

### What are Models in Django?

In Django, models are Python classes that represent database tables. Each attribute of the model represents a database field. Models are defined in the `models.py` file of a Django application. They provide a high-level abstraction for database operations and allow developers to interact with the database using Python code instead of SQL.

#### Defining a Model

Here's an example of how to define a model in Django:

```python
# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
```

In this example:
- `Author` and `Book` are models.
- `name` and `email` are fields of the `Author` model.
- `title`, `author`, and `published_date` are fields of the `Book` model.
- `ForeignKey` is used to create a many-to-one relationship between `Book` and `Author`.

#### Creating and Applying Migrations

After defining models, you need to create and apply migrations to create the corresponding database tables.

1. **Create Migrations**:
    ```sh
    python manage.py makemigrations
    ```

2. **Apply Migrations**:
    ```sh
    python manage.py migrate
    ```

#### Using Models

You can use Django's ORM to create, read, update, and delete records in the database.

1. **Creating Records**:
    ```python
    author = Author(name='John Doe', email='john@example.com')
    author.save()
    ```

2. **Reading Records**:
    ```python
    authors = Author.objects.all()
    author = Author.objects.get(id=1)
    ```

3. **Updating Records**:
    ```python
    author = Author.objects.get(id=1)
    author.email = 'newemail@example.com'
    author.save()
    ```

4. **Deleting Records**:
    ```python
    author = Author.objects.get(id=1)
    author.delete()
    ```

Models are a fundamental part of Django's ORM and provide a powerful and intuitive way to interact with the database.

### What is `python3 manage.py migrate`?

The `python3 manage.py migrate` command is a crucial part of Django's migration system. It is used to apply migrations to your database, ensuring that the database schema is up-to-date with your current models.

#### Detailed Explanation

1. **Migrations**:
    - Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.
    - They are stored as files on disk and are designed to be committed to your version control system and shared with your team.

2. **Creating Migrations**:
    - Before running `migrate`, you need to create migration files using the `python3 manage.py makemigrations` command.
    - This command scans your models and creates new migration files based on the changes detected.

3. **Applying Migrations**:
    - The `python3 manage.py migrate` command applies these migration files to your database.
    - It runs the SQL commands necessary to bring your database schema in line with your current set of models and migrations.

#### Workflow

1. **Make Changes to Models**:
    - Modify your models in `models.py`.

2. **Create Migrations**:
    ```sh
    python3 manage.py makemigrations
    ```
    - This generates migration files in the `migrations` directory of your app.

3. **Apply Migrations**:
    ```sh
    python3 manage.py migrate
    ```
    - This applies the migrations to your database, updating the schema.

#### Example

Suppose you add a new field to an existing model:

```python
# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)  # New field added
```

1. **Create Migrations**:
    ```sh
    python3 manage.py makemigrations
    ```
    - This generates a migration file like `0002_auto_20231010_1234.py`.

2. **Apply Migrations**:
    ```sh
    python3 manage.py migrate
    ```
    - This updates the database schema to include the new `bio` field in the `Author` table.

#### Benefits

- **Version Control**: Migrations can be committed to version control, allowing you to track changes to your database schema over time.
- **Collaboration**: Team members can share migration files, ensuring everyone has a consistent database schema.
- **Automation**: Migrations automate the process of updating the database schema, reducing the risk of errors.

By using `python3 manage.py migrate`, you ensure that your database schema is always in sync with your Django models, facilitating smooth development and deployment processes.
