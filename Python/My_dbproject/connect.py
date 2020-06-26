import sqlite3
import sys
sys.path.append("C:\\Users\\Sri Athishya\\Desktop\\Python\\4-4.30\\My_dbproject\\config")
import devconfig
import log_file


class Connect():
    def connection(self):
        try:
            conn = sqlite3.connect(devconfig.config('dev'))
            c = conn.cursor()
            log=log_file.Log()
            log.logging.info("Database Connected Successfully")
            return c, conn
        except Exception as e:
            print("Error:", e)
            return (False, False)
#obj=Connect()
#obj.connection()