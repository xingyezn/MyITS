from flask import session,redirect,url_for,g
from functools import wraps



def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if 'user_id' in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('/'))
    return inner




