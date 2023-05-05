from flask import Flask
app = Flask(__name__)

@app.route('/halo/<nama>')
def hello_nama(nama):
    return 'halo, %s!' % nama

if __name__ == '__main__':
    app.run()