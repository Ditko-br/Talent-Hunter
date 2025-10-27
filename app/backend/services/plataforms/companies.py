from flask import request, jsonify

class Enterprises:
    def __init__(self):
        pass

@app.route('/filter_companies', methods=['POST'])
def filter_companies():
    data = request.get_json()
    names = data.get('names', [])
    results = Enterprises.query.filter(Enterprises.name.in_(names)).all()
    return jsonify([company.to_dict() for company in results])
