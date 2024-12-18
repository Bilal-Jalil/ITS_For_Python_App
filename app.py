from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import ontology  

app = Flask(__name__)
app.secret_key = 'secret1234'
# Dummy Database
users = {}
feedback_data = {}

# Index Route
def check_login():
    return 'username' in session

@app.route('/')
def index():
    return redirect(url_for('login'))

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Login!"
    return render_template('login.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'password': password, 'progress': 0}
            return redirect(url_for('login'))
        else:
            return "User already exists!"
    return render_template('register.html')

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if not check_login():
        return redirect(url_for('login'))
    progress = users[session['username']]['progress']
    suggestions = ontology.get_suggestions(progress)
    return render_template('dashboard.html', suggestions=suggestions)

# Feedback Route
@app.route('/feedback', methods=['POST'])
def feedback():
    if not check_login():
        return redirect(url_for('login'))
    feedback = request.form['feedback']
    username = session['username']
    feedback_data[username] = feedback
    return "Feedback submitted successfully!"


@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['query']
    response = ontology.chat_response(user_input)  
    return jsonify({'response': response})

# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
