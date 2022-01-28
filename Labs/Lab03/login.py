#!/usr/bin/env python3
import cgi
import cgitb
import secret
import os
from http.cookies import BaseCookie
from templates import login_page, secret_page, after_login_incorrect

cgitb.enable()
form = cgi.FieldStorage()
username = form.getfirst("username")
password = form.getfirst("password")
cookie = BaseCookie(os.environ["HTTP_COOKIE"])

try:
    cookie_username = cookie.get("username").value
    cookie_password = cookie.get("password").value
    
    if cookie_username == secret.username and cookie_password == secret.password:
        username = cookie_username
        password = cookie_password
except:
    pass

is_auth = username == secret.username and password == secret.password

print("Content-Type: text/html")
if is_auth:
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")
print()

if not username and not password:
    print(login_page())
elif is_auth:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())