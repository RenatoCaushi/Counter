from flask import Flask, render_template, redirect, session, request # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'dsasdasdasdasdsdfa'


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index(): 
    if 'name' not in session:
        session['name']= 'Renato'

    if 'count' not in session:
        session['count']= 0
       
        return render_template('index.html')
    
    else:
        session['count'] += 1
        return render_template('index.html')

@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.