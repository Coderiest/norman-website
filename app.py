from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    

if __name__ == '__main__':
    # Configure Flask to work with Replit's proxy environment
    # Allow all hosts since user sees a proxy in an iframe
    app.run(host='0.0.0.0', port=5000, debug=True)