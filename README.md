# django-menu

# Environment
`$ virtualenv --python=python2.7  --no-site-packages ENV

$ source ENV/bin/activate

$ pip install -r requirements.txt
`

# How to testing
`$ cd menu
`
# prepare the db
`$ ./manage.py makemigrations

$ ./manage.py migrate
`
# create admin user and start the dev server
`$ ./manage.py createsuperuser

$ ./manage.py runserver
`
* Now, open a browser, and go to http://localhost:8000/admin
* Then add some menu items.
# Notices
* Notice 1: if you want the demo code show the menu you added, please use 'example' as the menu_name
* Notice 2: use absolute path as link, to make testing simpler. for example:
`          /category/coders`
* Notice 3: the order_weight field is for ordering the menu items

# Ready to go
After inserting some menu items in admin, you can display it by visiting: http://localhost:8000/

# How to use the template tag?
To use the tag in your app, you can write template like this:


`{% load menu %}

{% draw_menu 'example' %}
`

