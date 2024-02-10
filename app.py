
from flask import Flask, request, jsonify, render_template,send_file
from utils.data_processing import load_data, map_vendors, map_pincodes
from utils.matrix_operations import convert_to_csr, check_pincode_serviceability_helper
import json

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('./static/index.html')

@app.route('/script.js')
def script():
    return send_file('./static/script.js')
@app.route('/style.css')
def style():
    return send_file('./static/style.css')


@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    file = file.read()
    data = json.loads(file)
    global vendor_map
    global pincode_map
    global csr
    vendor_map = map_vendors(data)
    pincode_map = map_pincodes(data)
    csr = convert_to_csr(data)
    return jsonify({'message': 'File uploaded successfully'})


@app.route('/pincode_serviceability', methods=['POST'])
def check_pincode_serviceability():
    pincode = request.form.get('pincode', type=str)
    result = check_pincode_serviceability_helper(pincode, csr, vendor_map, pincode_map)
    if len(result) == 0:
        return jsonify({'message':'Service not available in this area'})
    else:
        return jsonify({'message':'Service available in this area','vendors':result})


if __name__ == '__main__':
    app.run(debug=True)






