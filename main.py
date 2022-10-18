import requests
import yaml
import json
from flask import Flask, render_template
import sqlite3



api_link = "https://techy-api.vercel.app/api/json"
app = Flask(__name__)



def get_response():
    request = requests.get(api_link)
    json_response = request.json()
    yaml_response = yaml.dump(json_response, default_flow_style=False)
    return(yaml_response)





@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    content = (get_response())
    def create_table():
        cur.execute('CREATE TABLE IF NOT EXISTS tech_phrases (id INTEGER PRIMARY KEY AUTOINCREMENT, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, content TEXT NOT NULL);')

    def data_entry():
        
        cur.execute("INSERT INTO tech_phrases (content) VALUES(?)",
                                                        (content,))
        conn.commit()
    create_table()
    data_entry()
    cur.close()
    conn.close()
    return render_template(f'index.html', variable=(content))
    
if __name__ == "__main__":
    app.run(debug=True)
