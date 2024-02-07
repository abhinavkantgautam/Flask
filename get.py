from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('get.html')


@app.route('/login',methods=['GET'])
def login():
    username=request.args.get('uname')
    password=request.args.get('pass')
    if username=='Gautam' and password=='Ram@3320':
       return 'welcome %s' %username
    else:
        return "Wrong Credentials"


if __name__=="__main__":
    app.run(debug=True)