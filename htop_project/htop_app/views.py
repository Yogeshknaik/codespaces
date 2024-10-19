from django.http import HttpResponse
import os
import datetime
import pytz
import subprocess

def htop(request):
    full_name = "YOGESH K N" 
    username = os.getlogin()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    top_output = subprocess.check_output(['tasklist']).decode('utf-8')
    return HttpResponse(f'''
    <h1>System Information</h1>
    <p>Name: {full_name}</p>
    <p>Username: {username}</p>
    <p>Server Time in IST: {server_time}</p>
    <pre>{top_output}</pre>
    ''')