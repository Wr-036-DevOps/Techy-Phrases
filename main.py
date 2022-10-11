import requests
import yaml
import json
from flask import Flask, render_template

api_link = "https://techy-api.vercel.app/api/json"
app = Flask(__name__)

def get_response():
    request = requests.get(api_link)
    json_response = request.json()
    return(json_response)

def json_to_yaml():
    yaml_file = open('response.yaml', 'w')
    yaml.dump(get_response(), yaml_file, default_flow_style=False)
    yaml_response = open('response.yaml', mode='r')
    yaml_reponse = (yaml_response.read())
    return(yaml_reponse)

@app.route('/')
def index():
    return render_template(f'index.html', variable=json_to_yaml() )
    
if __name__ == "__main__":
    app.run(debug=True)
