"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""

    return render_template('form.html')

@app.route('/results')
def show_results():
    """Show resulting message."""

    return render_template('results.html')

@app.route('/save_name')
def set_session():
    """Set value for session['name']"""
    # session['name'] = request.args.get("user_name")
    # name = session['name']
    name = request.args.get('user-name')
    session['name'] = name

    return render_template('homepage.html', name=name)

# @app.route('/get-session')
# def get_session():
#     """Gets name value from session"""
#     name = session['name']

#     return render_template('homepage.html', name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
