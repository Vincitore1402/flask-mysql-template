import MySQLdb
import MySQLdb.cursors as cursors

from config import config


class MySQLService:
  @staticmethod
  def get_connection():
    conn = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWORD, db=config.DB_NAME,
                           charset=config.DEFAULT_CHARSET, cursorclass=cursors.DictCursor)
    return conn

  def execute_query(self):
    conn = self.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM some_table;")
    data = cur.fetchall()
    conn.close()
    return data
