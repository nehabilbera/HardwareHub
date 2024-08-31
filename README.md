# HardwareHub

An E-commerce site designed in **Django** for shopping hardware online.

This is a college project and not any actual e-commerce website!


<br/><hr/><br/>


## Table of Contents
1. [How to run Project](#how-to-run-the-project)
2. [Advanced Database Operation](#advanced-database-operations)


<hr/><br/>



## How to run the project?

### 1. Get the project

**Follow any one of the two methods listed below**
    

  * Download the **.zip** of **master** branch, and extract it into a folder in your desktop, *__or__*,

  * Clone the **master** branch in your desktop.


<br/>

### 2. Installations

1. Install **Python 3** onto your computer (_python_version_>=**3.6**)
2. Install **dependencies** by running :-

    ```
    python -m pip install -r requirements.txt
    ```

<br/>


### 3. Running the project

Run the following command in the terminal with __project__ folder as the working directory.

  ```
  python manage.py runserver
  ```

<br/><hr/><br/>


## Advanced Database Operations

_**Note: Stay away if you don't know what is happening!**_

<br/>

### Current admin details
route: `/admin`
username: `admin`
password: `admin`

<br/>

### Changed any field in Database?

```
  python manage.py makemigrations
  python manage.py migrate
```

### Reset Database

```
  python manage.py flush
```

### Recreate database

```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
```

<br/><hr/><br/>