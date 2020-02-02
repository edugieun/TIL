# Django Social Login

[ https://django-allauth.readthedocs.io/en/latest/installation.html ]

- pip install django-allauth
- Settings.py

```python
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.kakao',
```

- SITE_ID = 1

```python
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
)
```

- LOGIN_REDIRECT_URL = 'movies:index'

- project/urls.py
  - path('accounts/', include('allauth.urls')),
- 