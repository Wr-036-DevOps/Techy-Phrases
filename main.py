import requests
import yaml
import json
from flask import Flask, render_template
import mysql.connector
import variables




api_link = "https://techy-api.vercel.app/api/json"
app = Flask(__name__)



def get_response():
    request = requests.get(api_link)
    json_response = request.json()
    yaml_response = yaml.dump(json_response, default_flow_style=False)
    return(yaml_response)



@app.route('/')
def index():
    mydb = mysql.connector.connect(
        host=variables.host,
        user=variables.user,
        password=variables.password,
        database=variables.database
        )   
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS tech_phrases (ID INT AUTO_INCREMENT PRIMARY KEY, CREATED TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, CONTENT TEXT NOT NULL)")
    content = (get_response())
    

    def data_entry():
        sql = "INSERT INTO tech_phrases (content) VALUES(%s)"
        val = [(content)]
        mycursor.execute(sql, val)
        mydb.commit()
    data_entry()
    mydb.close()
    return render_template(f'index.html', variable=(content))
    
if __name__ == "__main__":
    app.run(debug=True)