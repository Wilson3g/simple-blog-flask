# simple-blog-flask(#development)
A simple CRUD API blog with python(Flask)

Registration of users and comments using mysql

# Resources
- Creation of users
- Creation of posts
- Search by post names and posts content
- Creation of tags


# Requirements
You need to use pipenv to run the project:
```pip install pipenv```
python 3.6 ^


Create a virtual env with:
```pipenv shell``` and
```pipenv install```

Database:
- This project run with MySQL
- Create a database named ```simple_blog``` or rename the databases config in the ```__init__``` file
- Run the migrations with: ```flask db migrate```
- Create the tables with: ```flask db upgrade```

Run project:
```flask run```
