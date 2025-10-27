from flask import Blueprint, request, jsonify
from flask_login import login_required

companies_bp = Blueprint('companies', __name__, url_prefix='/api/companies')

@companies_bp.route('/search', methods=['GET'])
def search_companies():
    query = request.args.get('q', '')
    results = {
        "query": query,
        "companies": [] 
    }
    
    return jsonify(results), 200

@companies_bp.route('/<int:company_id>', methods=['GET'])
def get_company(company_id):
    company = {
        "id": company_id,
        "name": "Empresa Exemplo",
        "description": "Descrição da empresa"
    }
    
    return jsonify(company), 200

@companies_bp.route('/filter', methods=['POST'])
@login_required
def filter_companies():
    data = request.get_json()
    names = data.get('names', [])
    
    results = {
        "names": names,
        "companies": []
    }
    
    return jsonify(results), 200