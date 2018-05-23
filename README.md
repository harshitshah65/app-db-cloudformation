This is a basic flask APP which will read value from database and show it in web browser in form of table.

To run, activate the virtualenv.

source venv/bin/activate

export FLASK_APP=hello.py

export FLASK_DEBUG=true

python -m flask run --host=0.0.0.0 --port=5000


curl https://localhost:5000

curl https://localhost:5000/home
