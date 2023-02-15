from flask import Flask
app=__name__
@app.route('/')
def hello():
    return "HELLO MY NAME IS VIKASH"