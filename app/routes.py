#connects sub-urls to their destinies

from app import app
from flask import render_template, send_from_directory, request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Start')

@app.route('/snapshots')
def snapshots():
    return render_template('snapshots.html', title='Snapshots')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
    
#def static_from_root():
#    return send_from_directory(app.static_folder, request.path[1:])