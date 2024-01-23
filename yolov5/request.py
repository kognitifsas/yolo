import requests
from db import GestionnaireBaseDeDonnees

gestionnaire_bd = GestionnaireBaseDeDonnees()
gestionnaire_bd.ouvrir_connexion()
class BackendRequest:
    def __init__(self, url='http://localhost:5000/backend.php', headers={'User-Agent': 'my-app'}, data={'action': 'stop_program', 'key2': 'value2'}, auth=('username', 'password')):
        self.url = url
        self.headers = headers
        self.data = data
        self.auth = auth
    
    def send_request(self):
        response = requests.post(self.url, headers=self.headers, data=self.data, auth=self.auth)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            gestionnaire_bd.update_state(1);
            gestionnaire_bd.fermer_connexion()
            print("Request successful")
            print("Response content:", response.text)
        else:
            print(f"Request failed with status code {response.status_code}")
        return response

