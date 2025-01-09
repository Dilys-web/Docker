from flask import Flask, request, render_template_string, jsonify
from flask_wtf import CSRFProtect
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default_fallback_key")

csrf = CSRFProtect()
csrf.init_app(app)

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

def validate_request_method(methods):
    """Decorator to validate HTTP methods"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if request.method not in methods:
                return "Method not allowed", 405
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/register', methods=['GET', 'POST'])
@validate_request_method(['GET', 'POST'])
def register():
    """Secure registration endpoint"""
    if request.method == 'POST':

        # Get and validate the name
        name = request.form.get('name', '').strip()
        
        # Input validation
        if not name:
            return "Name is required!", 400
        if len(name) > 100:  # Prevent extremely long names
            return "Name is too long!", 400
        if not name.replace(' ', '').isalnum():  # Basic name validation
            return "Invalid name format!", 400
            
        # Sanitize output to prevent XSS
        from markupsafe import escape
        return f"Registration successful! Welcome, {escape(name)}!"

    # GET request - render registration form
    html_content = """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Register</title>
            <!-- Add Content Security Policy -->
            <meta http-equiv="Content-Security-Policy" 
                  content="default-src 'self'; 
                          script-src 'self' 'nonce-{{csrf_token()}}'; 
                          style-src 'self';">
        </head>
        <body>
            <h1>Register</h1>
            <form method="POST">
                <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
                <div>
                    <label for="name">Name:</label>
                    <input type="text" 
                           id="name" 
                           name="name" 
                           required 
                           maxlength="100" 
                           pattern="[A-Za-z0-9 ]+"
                           title="Please enter a valid name using letters, numbers and spaces only">
                </div>
                <button type="submit">Register</button>
            </form>
            <a href="/">Go back to Home</a>
        </body>
        </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)