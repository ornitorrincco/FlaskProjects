from flask import Flask,request,abort, redirect, url_for,render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath
#
# @app.route('/about')
# def about():
#     return 'The about page'
#
# @app.route('/canonical/')
# def canonical():
#     return 'The page'
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         try:
#             return request.form['username']
#         except KeyError:
#             return 'not key value in the dictonary, HTTP 400 Bad request error'
#     else:
#         return 'show_the_login_form()'
#
#
# # To access parameters submitted in the URL (?key=value) you can use the args attribute:
# #
# # searchword = request.args.get('key', '')
#
# # Upload file
# # you need to put in youe front-end enctype="multipart/form-data"
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')
#
# # Save the file in the server with the name of user put in the file
# @app.route('/uploadSecure', methods=['GET', 'POST'])
# def upload_file_secure():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/' + secure_filename(f.filename))
#
# # Access to a cookies atribute
# # Reading
# @app.route('/getCookie')
# def getCookie():
#     username = request.cookies.get('username')
#     # use cookies.get(key) instead of cookies[key] to not get a
#     # KeyError if the cookie is missing.
#
#
# # Writing
# @app.route('/setCookie')
# def setCookie():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
    
if __name__ == "__main__":
    app.run(debug=True)
