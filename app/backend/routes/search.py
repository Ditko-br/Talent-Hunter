from flask import Blueprint, request, jsonify
from flask_login import login_required
from app.backend.services.jobs_areas import Jobs
from app.backend.services.nations import JobCountry

search_bp = Blueprint('search', __name__, url_prefix='/api/search')
jobs_service = Jobs()
country_service = JobCountry()

@search_bp.route('/jobs', methods=['GET'])
@login_required
def search_jobs():
    query = request.args.get('q', '')
    area = request.args.get('area', '')
    country = request.args.get('country', '')

    results = {
        "query": query,
        "area": area,
        "country": country,
        "jobs": [] 
    }
    
    return jsonify(results), 200

@search_bp.route('/areas', methods=['GET'])
def get_areas():
    return jsonify(jobs_service.get_areas()), 200

@search_bp.route('/countries', methods=['GET'])
def get_countries():
    return jsonify({
        "south_america": country_service.south_america,
        "central_america": country_service.central_america,
        "north_america": country_service.north_america,
        "europe": country_service.europe,
        "asia": country_service.asia
    }), 200

@search_bp.route('/filter', methods=['POST'])
@login_required
def filter_jobs():
    data = request.get_json()
    areas = data.get('areas', [])
    countries = data.get('countries', [])
    companies = data.get('companies', [])

    results = {
        "areas": areas,
        "countries": countries,
        "companies": companies,
        "jobs": []
    }
    
    return jsonify(results), 200