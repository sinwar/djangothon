# djangothon
django extensions for model schema and CSRF


# Django upper

1. `CSRF_REFERER_CHECK`: Created a new csrf middleware which allows request to pass without checking referer check. Currently django rejects the requests without referer header. However, some users may prevent their browsers from sending the Referer header, due to privacy concerns. These users are unable to submit 'non-safe' requests (e.g. POST requests) on HTTPS-enabled Django-powered website that use CSRF protection.

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
