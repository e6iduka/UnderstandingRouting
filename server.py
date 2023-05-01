from flask import Flask
app = Flask (__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "DOJO!"

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi " + name  


@app.route('/repeat/<times_repeat>/<repeat_str>')
def repstr(times_repeat,repeat_str):
    post_repeat = ""
    for i in range(int(times_repeat)):
        post_repeat += repeat_str + " "
    return post_repeat

if __name__=="__main__":
    app.run(debug = True)