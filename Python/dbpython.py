
import sqlite3

 
# create database and initialize cursor
def connection():
    try:
        conn = sqlite3.connect(r'C:\Users\Sri Athishya\Desktop\Python\4-4.30\mymodel.db')
        c = conn.cursor() 
        return c,conn
    except Exception as e:
        print("Error:",e)
    
def mycode(c):
    str1=""
    a=c.execute('SELECT * FROM dept_emp')
    for row in a:
        p=','.join(row)
        str1=str1+p+'\n'
        
    return(str1)

if __name__ == '__main__': 
    c,conn=connection()
    c.execute(f'Delete from dept_emp')
    c.execute(f'CREATE TABLE IF NOT EXISTS dept_emp(emp_no char, dept_no varchar,from_date date,to_date date)')

    with open('dept_emp.txt', 'r+') as fr:
        for line in fr.readlines():
        # parse the results.txt, create a list of comma separated values
            fields = line.replace('\n', '').split(',')
            try:
                
                    c.execute(f'INSERT INTO dept_emp (emp_no,dept_no,from_date,to_date)'\
                    f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}','{fields[3]}')") 
                
            except Exception as e:
                print("Error:",e)
       

    conn.commit()
    mycode(c)
    conn.close()