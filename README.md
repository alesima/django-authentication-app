Django Authentication App
============

`django-authentation-app` provides authentication forms to register and login into the system.

Instructions
------------

1. Add `django-authentication-app` to your INSTALLED_APPS setting like this:
   
   INSTALLED APPS = [
       ...,
       'django-authentication-app',
   ]

2. Include `urls.py` from `django-authentication-app` module in your `urls.py` like this:
  
   url(r'^api/', include('django_authentication_app.urls')),



 
