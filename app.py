from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Skills Route
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Experience Route
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Education Route
@app.route('/education')
def education():
    return render_template('education.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')
# Work Route
@app.route('/work')
def work():
    return render_template('work.html')

if __name__ == '__main__':
    app.run(debug=True)