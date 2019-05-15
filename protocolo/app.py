import os
from flask import Flask, jsonify, make_response, request
from selenium import webdriver
import time
import re

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

URL_PROTOCOLO = "http://www1.uea.edu.br/modulo/login/protocolo.php"

def get_status(num_protocolo, senha_protocolo):
    fp = webdriver.FirefoxProfile()
    drive = webdriver.Firefox(firefox_profile = fp)
    try:
        drive.set_page_load_timeout(15)
        drive.get(URL_PROTOCOLO)
        drive.find_element_by_id("procId").send_keys(num_protocolo)
        drive.find_element_by_id("password").send_keys(senha_protocolo)
        drive.find_element_by_class_name("btn").click()
        time.sleep(3)
        info_proc = drive.find_element_by_class_name("panel")
        info = info_proc.text
        status = re.findall("Status: (.*)", info)
        drive.quit()
    except:
        status = False
        drive.quit()    
    
    return status

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/protocolo', methods=['POST'])
def protocolo():
    if request.method == 'POST':
        num_protocolo = request.form['num_protocolo']
        senha_protocolo = request.form['senha_protocolo']
        status = get_status(num_protocolo, senha_protocolo)
        if status == False:
            return make_response(jsonify({'status':'não foi possível verificar status', 'status_code':500}), 500)
    return jsonify({'status_code': 200, 'status': status})
