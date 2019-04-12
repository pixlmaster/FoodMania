# FoodMania
**FoodMania** is a **web-app** which is part of our project in Software Engineering Lab under Dr. Debasis Samanta.

## Prerequisite/libraries used
1. **Python3(3.6 +)** needs to be installed, if it is not, you can simply google how to do it(it's fairly easy).
2. **Django(2.1 +)** needs to be installed, if it is not, open terminal and type `pip3 install Django`.
3. **Pillow(1.1+)** needs to be installed.
4. This code was written using **Python 3.6.7** and **Django 2.1.7**.

## Usage(Tested on ubuntu 18.04)
1. Clone or Fetch this repo to your local machine.
2. To start the server go to the repo directory in terminal and type `python3 manage.py runserver`. Note:Keep this running as long as you are using the website.
3. Now open browser and visit `127.0.0.1:8000/`(or something similar that appeared on terminal when previous command was run). This is the home-page of this web-site.(locally).
4. Navigate like a normal web-site.
5. If you want to see database/user info, you can add your own super-user by running `python3 manage.py createsuperuser` in the repo's directory. After creating superuser, use the credentials on `127.0.0.1/8000:admin/`(or whatever your machine's local host is) to log-in and view the database.
