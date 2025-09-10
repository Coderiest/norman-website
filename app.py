from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Norman's Website</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 40px 20px;
                line-height: 1.6;
                color: #333;
            }
            h1 {
                color: #2c3e50;
                text-align: center;
                margin-bottom: 30px;
            }
            .welcome {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Norman's Website</h1>
        <div class="welcome">
            <p>Hello! This is Norman's website, now running on Replit.</p>
            <p>The site is ready for further development and customization.</p>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Norman website is running'}

if __name__ == '__main__':
    # Configure Flask to work with Replit's proxy environment
    # Allow all hosts since user sees a proxy in an iframe
    app.run(host='0.0.0.0', port=5000, debug=True)