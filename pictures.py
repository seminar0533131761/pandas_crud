from flask import Flask, send_file,make_response
from imgs import get_imgs
app = Flask(__name__)



@app.route('/picture')
def display_picture():
    picture_path = get_imgs.get_first_picture()
    response=make_response (send_file(picture_path, mimetype='image/jpeg',as_attachment=True))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

app.run(debug=True)
