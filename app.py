from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
=======
@app.route('/about',methods=['GET','POST'])
def about():
    
    return render_template('about.html')
>>>>>>> a458b5765c520a345a5ce82179dbe9da440ab208

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)