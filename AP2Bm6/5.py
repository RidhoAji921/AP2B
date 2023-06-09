from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog number: %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'revision number: %d' % revNo

if __name__ == '__main__':
    app.run()