from flask import Flask


from app.config import Config


mln= Flask(__name__)
mln.config.from_object(Config)

from app import routes