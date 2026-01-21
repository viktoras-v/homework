from flask import Flask, jsonify, render_template, request
import requests
from typing import Optional, Dict, Any

app = Flask(__name__)

# Configuration
API_BASE_URL = "https://petstore.swagger.io/v2"
API_KEY = "special-key"

class PetStoreAPI:
    """Client for interacting with the Petstore API"""
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'accept': 'application/json',
            'api_key': self.api_key
        }
    
    def get_pet_by_id(self, pet_id: int) -> Dict[str, Any]:
        """Get pet details by ID"""
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def find_pets_by_status(self, status: str = "available") -> list:
        """Find pets by status (available, pending, sold)"""
        url = f"{self.base_url}/pet/findByStatus"
        params = {'status': status}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    #-------------NEW----------------------
    # Delete pet by ID
    def delete_pet_by_id(self, pet_id: int) -> Dict[str, Any]:
        url = f"{self.base_url}/pet/{pet_id}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    # Add pet
    def add_pet(self, pet: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/pet"
        response = requests.post(url, headers=self.headers, json=pet)
        response.raise_for_status()
        return response.json()
    #--------------------------------------
    
    

# Initialize API client
pet_api = PetStoreAPI(API_BASE_URL, API_KEY)

@app.route('/')
def index():
    """Home page with API documentation"""
    return render_template('index.html')
# /api/v1/
# /api/
@app.route('/api/pet/<int:pet_id>')
def get_pet(pet_id: int):
    """Endpoint to get pet by ID"""
    try:
        pet_data = pet_api.get_pet_by_id(pet_id)
        return jsonify({
            'success': True,
            'data': pet_data
        })
    except requests.exceptions.HTTPError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'status_code': e.response.status_code
        }), e.response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/pets/status/<status>')
def get_pets_by_status(status: str):
    """Endpoint to find pets by status"""
    try:
        pets = pet_api.find_pets_by_status(status)
        return jsonify({
            'success': True,
            'count': len(pets),
            'data': pets
        })
    except requests.exceptions.HTTPError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'status_code': e.response.status_code
        }), e.response.status_code
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/test')
def test_api():
    """Test endpoint to verify API connectivity"""
    try:
        pet_data = pet_api.get_pet_by_id(1)
        return jsonify({
            'success': True,
            'message': 'API connection successful',
            'sample_data': pet_data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'API connection failed',
            'error': str(e)
        }), 500


  #-------------NEW----------------------  
 # Delete pet
@app.route("/pet/delete/<int:pet_id>")
def delete_pet_browser(pet_id):
    return jsonify(pet_api.delete_pet_by_id(pet_id))

# Add pet
from flask import request, jsonify

@app.route("/pet/add", methods=["POST"])
def add_pet_form():
    pet_data = request.get_json()  # JSON из fetch
    try:
        result = pet_api.add_pet(pet_data)
        return jsonify(result), 201
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": str(e)}), 500

# Add post
#@app.route("/pet/add_barsik")
#def add_barsik():
#    pet_data = {
#        "id": 123,
#        "name": "Barsik",
#        "status": "available"
#    }
#    result = pet_api.add_pet(pet_data)
#    return jsonify(result)
#-------------------------------------- 


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
