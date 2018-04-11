from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args['username']
    return render_template('welcome.html', username = username) 

@app.route("/", methods=['POST', 'GET'])   
def index():
    username1 = ""
    email = ""
    U_error = ""
    pass_error = ""
    vrfy_error = ""
    error = ""
   
    if request.method == 'POST':
        username1 = request.form['username']
        pass_wrd = request.form['password']
        vrfy_pswrd = request.form['verify-password']
        email = request.form['email']
   
        if username1.strip() == "":
            U_error = "Please enter a valid username"
            username1 = ""

        if pass_wrd.strip() == "": 
            pass_error = "Please enter a valid password"
            pass_wrd = ""
        
        else:
            if " " in pass_wrd or len(pass_wrd) < 3 or len(pass_wrd) > 20:
                pass_error = "Please enter a valid password"
                pass_wrd = ""

        if pass_wrd != vrfy_pswrd:
            vrfy_error = "Passwords do not match"
            vrfy_pswrd = ""
            pass_wrd = ""  
        
        if len(email) > 0:
            if ("@" not in email) or ("." not in email):
                error = "Not a valid email"
                email = ""
        
        
        if (not U_error) and (not pass_error) and (not vrfy_error) and (not error):
            return redirect('/welcome?username=' + username1)

        else:    
            return render_template('base.html', username=username1, email=email, error1=U_error, error2=pass_error, error3=vrfy_error, error4=error ) 
    
    else:
        return render_template('base.html', username=username1, email=email, error1=U_error, error2=pass_error, error3=vrfy_error, error4=error ) 


app.run()