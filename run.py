# the run.py file calls the run() method for the instance of the Flask module (that was created in the __init__.py file
from project import app

# run app
if __name__ == "__main__":
    app.run(host='0.0.0.0')