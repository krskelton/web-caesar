from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head>
        <style> 
                form {{ 
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
                .error {{ 
                    color: red; 
                }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form method='POST'>
            <label>Rotate by:
                <input type="text" name="rot" value="0"/>
            </label>
            <p class="error">{rot_errors}</p>
            <textarea name="text">{encrypt_string}</textarea>
            <input type="submit" />          
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(rot_errors='', encrypt_string='')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rot_errors = ''
    encrypt_string = ''

    if not is_integer(rot):
        rot_errors = 'Not a valid integer'
        rot=''
    else:
        rot = int(rot)
    
    if not rot_errors:
        encrypt_string = rotate_string(text, rot)
        return form.format(rot_errors='', encrypt_string=encrypt_string)
    else:
        return form.format(rot_errors=rot_errors, encrypt_string='')

app.run()