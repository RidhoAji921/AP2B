from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def halo_flask():
    return 'Halo flask'

@app.route('/python/')
def halo_python():
    return 'Halo python'

if __name__ == '__main__':
    app.run()