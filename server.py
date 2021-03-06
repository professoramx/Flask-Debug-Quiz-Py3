from flask import Flask, request, redirect, render_template, session, flash
app = Flask(__name__)
app.secret_key = "unicorns"

####################
#Welcome to the Flask Debug Quiz
#Fix all errors, and fix the commented instructions within the index route
#Good Luck Hackers!
####################

@app.route('/') 
def index(): 
    


    if "info" not in session:
        session['info'] = ""
    
    ##########################
    #Important!
    #Session['info'] appears as an Array on the front page. 
    #Add the a loop on index.html to display each index of the array on a separate line
    #########################
    
    return render_template("index.html", info = session['info'])


@app.route("/form", methods=['POST'])
def form():
    
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
    else:
        session['info'] = {
            'First Name': request.form["FirstName"], 
            'Last Name': request.form['LastName'], 
            'Favorite Snack (hidden)': request.form['FaveSnack']
        }


    return redirect('/')



app.run(debug=True)