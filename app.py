from flask import Flask
app=Flask(__name__)

#route
@app.route("/")
def hello_world():
    return "Hello my name is vikash and i am biggest fan of mia khalifa and rajshree verma"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
