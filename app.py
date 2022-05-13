from flask import Flask

app=Flask(__name__)

@app.route('/')
def error():
    return f'<br><br><br><body style="text-align:center" BGCOLOR="Gainsboro"> <font Size="7">Error'

@app.route('/<ping>')
def pong(ping):
    if ping == 'ping':
        return f'<br><br><br><body style="text-align:center" BGCOLOR="Gainsboro"> <font Size="7">pong'
    else:
        return f'<br><br><br><body style="text-align:center" BGCOLOR="Gainsboro"> <font Size="7">Error'


app.run()