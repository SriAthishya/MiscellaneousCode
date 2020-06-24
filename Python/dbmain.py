import dbpython
import unittest
import sqlite3

class test_defs(unittest.TestCase):
  def test_insertdb(self):
    a=open("dept_emp.txt",'r')
    b=a.read()
    conn = sqlite3.connect(r'C:\Users\Sri Athishya\Desktop\Python\4-4.30\mymodel.db')
    c = conn.cursor() 
    d=dbpython.mycode(c)
    print(b)
    print(d)
    self.assertEqual(d,b)
    
if __name__ == '__main__': 
    unittest.main()