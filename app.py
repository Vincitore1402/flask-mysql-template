from flask import Flask

from routers.default_router import index_page

app = Flask(__name__)

app.register_blueprint(index_page)

if __name__ == '__main__':
  from config import config
  app.secret_key = config.SECRET_KEY
  app.run(debug=True)
