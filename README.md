# whuritgo-api

### Description
whuritgo helps you keep track of your expenses. Enter your purchase information and itll keep this history of everything you purchased.

### Technologies Used
- Python
- Django
- Heroku

### Development Process
The goal of the application is to be able to perform the following:
- POST /sign-up (sign up new user)
- POST /sign-in (sign in existing user)
- PATCH /change-password (change users password)
- DELETE /sign-out (sign out user)
- POST /expenses (add a new expense)
- GET /expenses (view all expense)
- PATCH /expenses (update specific expense)
- DELETE /expenses (delete specific expense)

The application also has a client side. Below is my developement process for the front end:
- Have a new user sign up and create hashed password on backend
- Have an existing user sign in and generate new randomized token
- Have user be able to add a new expense/purchase with required authentication token
- Have user be able to view all purchases that they own with required authentication token
- Have user be able to update a expense that they own with required authentication token
- Have a user be able to delete a expense that they own with required authentication token
- User must be able to sign out with required authentication token
- Unauthenticated user can not have access to authenticated functions such as change password, add a new expense, view all expenses, update expense, or delete an expense
- Have all forms clear on submit success

### Unsolved Problems
- Displaying running total of expenses
- Choose how many purchases to show at once

### ERD
![Imgur](https://i.imgur.com/eJ0fCe9.png "ERD for Project 4")

### Links to Repo for Client Side of App and the Deployed Sites of Client and API
whuritgo-client deployed site:
https://senoralikz.github.io/whuritgo-client/

whuritgo-client repo:
https://github.com/senoralikz/whuritgo-client

whuritgo-api deployed site:
https://dashboard.heroku.com/apps/whuritgo
