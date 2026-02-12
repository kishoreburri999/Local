from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')

# 🔥 ADD THIS
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
