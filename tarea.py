from flask import Flask, request, jsonify

app = Flask(__name__)

areas = []
empleados = []


def get_area_by_id(area_id):
    for area in areas:
        if area['id'] == area_id:
            return area
    return None

def get_empleados_by_params(email=None, nombre=None):
    filtered_empleados = empleados
    if email:
        filtered_empleados = [empleado for empleado in filtered_empleados if empleado['email'] == email]
    if nombre:
        filtered_empleados = [empleado for empleado in filtered_empleados if empleado['nombre'] == nombre]
    return filtered_empleados


@app.route('/areas', methods=['GET'])
def get_areas():
    return jsonify(areas)

@app.route('/area', methods=['POST'])
def create_area():
    data = request.get_json()
    if not data.get('id') or not data.get('nombre') or not data.get('piso'):
        return jsonify({'message': 'Falta información para crear el área'}), 400

    new_area = {
        'id': data['id'],
        'nombre': data['nombre'],
        'piso': data['piso']
    }
    areas.append(new_area)
    return jsonify(new_area), 201

@app.route('/area/<int:area_id>', methods=['GET'])
def get_area(area_id):
    area = get_area_by_id(area_id)
    if not area:
        return jsonify({'message': 'El área no existe'}), 404
    return jsonify(area)

@app.route('/empleado', methods=['POST'])
def create_empleado():
    data = request.get_json()
    if not data.get('id') or not data.get('nombre') or not data.get('apellido') or not data.get('email') or not data.get('area_id'):
        return jsonify({'message': 'Falta información para crear el empleado'}), 400

    new_empleado = {
        'id': data['id'],
        'nombre': data['nombre'],
        'apellido': data['apellido'],
        'email': data['email'],
        'area_id': data['area_id']
    }
    empleados.append(new_empleado)
    return jsonify(new_empleado), 201

@app.route('/empleados', methods=['GET'])
def get_empleados():
    email = request.args.get('email')
    nombre = request.args.get('nombre')
    filtered_empleados = get_empleados_by_params(email, nombre)
    return jsonify(filtered_empleados)

if __name__ == '__main__':
    app.run(debug=True)
