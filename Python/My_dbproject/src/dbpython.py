import connect
import sys
sys.path.append('C:\\Users\\Sri Athishya\\Desktop\\Python\\4-4.30\\My_dbproject\\config')
import log_file


class Db():
    def __init__(self):
        obj=connect.Connect()
        c,conn = obj.connection()
        self.c= c
        self.conn=conn

    def mycode(self,cb):
        str1=""
        x=connect.Connect()
        c, conn=x.connection()
        c=cb
        try:
            cb.execute('SELECT * FROM dept_emp')
            for row in cb:
                p=','.join(row)
                str1=str1+p+'\n'
            l = log_file.Log()
            l.logging.info("Data selected from the Table")
            return(str1)
        except Exception as e:
            print("Error:", e)
            return False
    def fun(self):
        return self.c,self.conn

if __name__ == '__main__': 
    obj=Db()
    c,conn=obj.fun()
    #c,conn=connect.Connect.connection(self)
    c.execute(f'Delete from dept_emp')
    l=log_file.Log()
    l.logging.info("Data deleted inside the Table")
    c.execute(f'CREATE TABLE IF NOT EXISTS dept_emp(emp_no char, dept_no varchar,from_date date,to_date date)')
    l.logging.info("New table is created since there is no such table already exists")
    try:
        with open('../dept_emp.txt', 'r+') as fr:
            for line in fr.readlines():
                fields = line.replace('\n', '').split(',')
                try:
                    c.execute(f'INSERT INTO dept_emp (emp_no,dept_no,from_date,to_date)'\
                    f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}')")
                    l.logging.info("Data are inserted successfully into the Table")
                except Exception as e:
                    print("Error:",e)
    except FileNotFoundError as e:
        print("Error:",e)
    
    conn.commit()
    obj.mycode(c)
    conn.close()
    