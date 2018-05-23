This is a basic flask APP which will read value from database and show it in web browser in form of table.

To run, activate the virtualenv.

source venv/bin/activate

export FLASK_APP=hello.py

export FLASK_DEBUG=true

python hello.py --port=5000

curl https://localhost:5000

curl https://localhost:5000/home - This will fetch data from the database (RDS)


***In the attached code I have included below things:

•	Created a EC2 instances. 

•	Selected Ubuntu as the image, reference ami Ubuntu id: ami-b5ed9ccd

•	Assuming there is a key already created, it will be asked for input when the stack is created.

•	The availability zone selected in this is “us-west-2”.

•	Database used is RDS – Mysql – 5.6.39 version.

•	Create RDS instance in multi availability zone. 

•	Mentioned pre-requisite in steps.txt which is been taken care in userdata, under cloud formation template.

•	“mysql -uroot -p -h'<RDS DB Endpoint Address>' reports < dump.sql” – this is required to do manually as RDS endpoint should be taken and data should be imported.
                                                                    
•	As we are using self signed certificate to run in to secure mode(https), we have created a key using createcert.sh script using openssl.

•	We have used flask framework for webapp.

•	We have used the image according to the image available in this region, in case you change then change the image id accordingly. 

