from flask import Flask, request, render_template_string

from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_fallback_key")

csrf = CSRFProtect(app)

# Home route
@app.route('/')
def home():
    return """
    <h1>Welcome to My Flask App!</h1>
    <p>This is a simple web application built with Flask.</p>
    <p>Use the following links to explore:</p>
    <ul>
        <li><a href="/greet/YourName">Greet Me!</a> - Replace <strong>YourName</strong> with your actual name in the URL.</li>
        <li><a href="/about">About This App</a></li>
        <li><a href="/register">Register</a></li>
    </ul>
    <p>For example, to greet Alice, change the link to <strong>/greet/Alice</strong>.</p>
    """

# Greet route
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the Flask app."

# Simple HTML page route
@app.route('/about')
def about():
    html_content = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>About</title>
      </head>
      <body>
        <h1>About This App</h1>
        <p>This is a simple Flask application to demonstrate routes and HTML rendering.</p>
        <a href="/">Go back to Home</a>
      </body>
    </html>
    """
    return render_template_string(html_content)

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get the name from the form
        name = request.form.get('name', '').strip()
        if not name:
            return "Name is required!", 400
        return f"Registration successful! Welcome, {name}!"

    # Render registration form
    html_content = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Register</title>
      </head>
      <body>
        <h1>Register</h1>
        <form method="POST">
          {{ csrf_token()}}
          <label for="name">Name:</label>
          <input type="text" id="name" name="name" required>
          <button type="submit">Register</button>
        </form>
        <a href="/">Go back to Home</a>
      </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)