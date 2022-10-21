App for querying apis
this repo contains files and instructions for deploying the app both locally and on the cloud (public)

How To Run

To Run Locally: 
assuming you have mysql server installed 
1. In your virtenv
2. Run "$ pip install -r requirements.txt"
3. Run the mysql_connection_init.py to create a database (edit variables.py to match your db configuraton)
4. Run "$ python main.py"



To Run Publicly (Cloud, AWS) (Monolith setup):
1. Assuming the cloud infrastructure has been setup already (VPC, SUBNETS and internet gateways etc)
2. Install  mysql server
3. Create and activate a python environment and install all dependables using "$ pip install -r requirements.txt"
4. install gunicorn "$ pip install gunicorn"
5. Run "$ gunicorn -b 0.0.0.0:8000 main:app" and exit gunicorn 
6. move the flaskapp.service unit file to the folder /etc/systemd/system/
7. enable the service 
8. Install Nginx webserver to act as a reverse proxy accepting requests and routing to gunicorn "$ sudo apt-get nginx" 
9. start and enable nginx with these commands "$ sudo systemctl start nginx" "$ sudo systemctl enable nginx"  the instance public IP should return nginx home page at this point 
10. replace or edit the nginx default config file with the "default" file in the repo
11. restart nginx "$ sudo systemctl restart nginx"
12. instance IP should return flask application
