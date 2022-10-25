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
4. Run the mysql_connection_init.py to create a database (edit variables.py to match your db configuraton)
5. install gunicorn "$ pip install gunicorn"
6. Run "$ gunicorn -b 0.0.0.0:8000 main:app" and exit gunicorn 
7. move the flaskapp.service unit file to the folder /etc/systemd/system/
8. enable the service 
9. Install Nginx webserver to act as a reverse proxy accepting requests and routing to gunicorn "$ sudo apt-get nginx" 
10. start and enable nginx with these commands "$ sudo systemctl start nginx" "$ sudo systemctl enable nginx"  the instance public IP should return nginx home page at this point 
11. replace or edit the nginx default config file with the "default" file in the repo
12. restart nginx "$ sudo systemctl restart nginx"
13. instance IP should return flask application

To Run Publicly (Cloud, AWS) (multi tier setup):
Assuming all infrastructure for a three tier architecture is already setup which includes a vpc with public and private subnets, ec2 server and database instance both in their respective subnets (pub and priv), and proper security groups and rules to enable communitction between both resources.
Basically the previous steps as aboove only change is;
1. Changing the value of your host in the variables.py file to the endpoint of your rds database
2. restarting the flaskapp.service using "$ systemctl restart flaskapp.service"
3. to check the records of your rds datatbase, using mysql command line use 
"mysql -h RDS_DATABASE_ENDPOINT -P 3306 -u USERNAME -p"
4. Query the database as normal using sql commands 