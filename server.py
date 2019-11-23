from flask import Flask, flash, request, redirect, url_for, abort, make_response
from werkzeug import secure_filename
import cv2
import os
import app as comparacao
import os.path 
from os import path

UPLOAD_FOLDER = './database'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        name = request.form.get('name')
        email = request.form.get('email')
        level = request.form.get('level')
        filename = secure_filename(email + '.png')
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if (name != '' and email != '' and level != ''):
            return name + ' - ' + email + ' - ' + str(level)
        else:
            return 'Algum campo não foi preenchido corretamente, por favor revise os mesmos e envie o formulário novamente!'
    else:
        abort(403)

@app.route('/compare', methods=['GET', 'POST'])
def compare_file():
    email = request.form.get('email')
    file = request.files['file']
    if (email != '' and file != ''):
        email2 = email.replace('@', '')
        if (cv2.imread('database/'+ email2 + '.png') is not None):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'comparacao.png'))
            comp = comparacao.main(email2)
            if(comp == True):
                return 'Biometria confirmada!' + ' - Email:' + email
            return 'Biometria negada!'
        else:
            return 'Email não cadastrado'
    else:
        return 'Algum campo não foi preenchido corretamente, por favor revise os mesmos e envie o formulário novamente!'


@app.route('/edit', methods=['GET', 'POST'])
def edit_finger():
    email = request.form.get('email')
    email2 = email.replace('@', '')
    email2 = email2 + '.png'
    file = request.files['file']
    comp = str(path.exists('./database/' + email2))
    if(comp != False):
        filename = secure_filename(email2)
        if (cv2.imread('database/'+ email2) is not None):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'Biometria Atualizada com sucesso'
        else:
            return 'Este e-mail não existe'

if __name__ == "__main__":
    app.run()