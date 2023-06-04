# config                    
from flask import Flask
app = Flask(__name__)


from petfax import create_app

app = create_app()
