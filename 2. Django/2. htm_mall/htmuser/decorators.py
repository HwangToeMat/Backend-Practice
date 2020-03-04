from django.shortcuts import redirect
from .models import HTMuser


def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)
    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = HTMuser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/login')

        return function(request, *args, **kwargs)
    return wrap
