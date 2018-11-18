# djangothon
django extensions for model schema and CSRF


# Django upper
1. `Model_Graph_UI`: Created a UI system to show the real time updations, deletions and referencing of django models. A Graph diagram image has been created to facilitate developers to see and verify the model schema.

How to use :
Start djangoupper app using ``` python manage.py runserver ```
Go to graphmodel-fe and start server ``` node index.js ```


![Graph UI](djangoupper/Screenshot.png)

2. `CODE GENERATION` : In django rest if developer create a model then for CRUD opertion developer need to write lots of repetitive code for serializers and generic api views. This code will automatically generate the required code for each model of app.
Clone this app to your django project and run following command in project directory-
` python djangoupper/generate.py path/to/models.py`

3. `CSRF_REFERER_CHECK`: Created a new csrf middleware which allows request to pass without checking referer check. Currently django rejects the requests without referer header. However, some users may prevent their browsers from sending the Referer header, due to privacy concerns. These users are unable to submit 'non-safe' requests (e.g. POST requests) on HTTPS-enabled Django-powered website that use CSRF protection.

Clone this app to your django project and add following in the settings.py :

```

MIDDLEWARE_CLASSES = [
    ...
    'djangoupper.middleware.newcsrf.CsrfViewMiddleware',
    ...
]

INSTALLED_APPS = [
    ...
    'djangoupper',
]

# csrf referer check in user request
CSRF_REFERER_CHECK=True

```

4. `XOR query support` : This package provides support for XOR queries in django. Right now only and or are available in django.-
` Foobar.objects.filter(Q(blah=1) ^ Q(bar=2))`

