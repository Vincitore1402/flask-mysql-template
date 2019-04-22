from flask import Blueprint, jsonify

from services.mysql_service import MySQLService

index_page = Blueprint('index_page', __name__, template_folder='templates')

db = MySQLService()


@index_page.route('/')
def index():
	data = db.execute_query()
	return jsonify(data)
