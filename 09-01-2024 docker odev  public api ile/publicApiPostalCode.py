### Ödev - 2 Public Api ###

from flask import Flask
from flask_restful import Api, Resource
import requests
import json

app = Flask(__name__)
api = Api(app)

class PostalInfo(Resource):
    def get(self):
        country = request.args.get('country')
        postal_code = request.args.get('postal_code')

        if not country or not postal_code:
            return '{"error": "Ülke kodu ve posta kodu gerekli"}', 400

        url = f"https://api.zippopotam.us/{country}/{postal_code}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return json.dumps(data)
        else:
            return '{"error": "API isteği başarısız oldu"}', 500

api.add_resource(PostalInfo, '/api/postal_info')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
