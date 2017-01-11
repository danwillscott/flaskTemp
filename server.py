from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
          # The "@" symbol designates a "decorator" which attaches the following # function to the '/' route. This means that whenever we send a request to
app.secret_key = "SKEY12345"                     
                      
@app.route('/')
def index():		# localhost:5000/ for index.html
	return render_template('index.html')


















app.run(debug=True)      # Run the app in debug mode if debug is set to True.