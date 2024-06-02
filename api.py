from flask import Flask, request, jsonify
from flask_caching import Cache
from external_api import get_city_info
from middleware import requires_auth
from flask_cors import CORS

app = Flask(__name__)
cache_config = {
    'CACHE_TYPE': 'SimpleCache', 
    'CACHE_DEFAULT_TIMEOUT': 300
    }
cache = Cache(app, config = cache_config)
CORS(app)

@app.route("/status", methods = ['GET'])
def status():
    return  {
        "status": "running'"
    }

@app.route("/city", methods = ['GET'])
@requires_auth
@cache.cached(timeout=300, query_string=True)
def city():
    query = request.args.get('city')
    if query:
        city_info, status_code = get_city_info(query)
        return jsonify(city_info), status_code
    else:
        return jsonify({'error': 'No query parameter provided'}), 400
    
if __name__ == "__main__":
    app.run(debug=True)