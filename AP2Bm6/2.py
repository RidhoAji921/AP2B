from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    return 'halo, selamat datang di website kami'

if __name__ == '__main__':
    app.run()