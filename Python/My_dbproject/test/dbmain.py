import unittest
import sys

import connect
from src import dbpython

sys.path.append('C:\\Users\\Sri Athishya\\Desktop\\Python\\4-4.30\\My_dbproject\\src\\dbpython.py')
#import dbpython
sys.path.append('C:\\Users\\Sri Athishya\\Desktop\\Python\\4-4.30\\My_dbproject\\connect.py')
#import connect


class test_defs(unittest.TestCase):
    def test_insertdb(self):
        obj=connect.Connect()
        c, conn = obj.connection()

        with open("../dept_emp.txt", 'r') as a:
            b=a.read()
            obj1=dbpython.Db()
            d= obj1.mycode(c)
            self.assertEqual(d,b)
    
    def test_connection(self):
        obj1=connect.Connect()
        c=obj1.connection()
        self.assertNotEqual((c,c),("False,False"))
    
if __name__ == '__main__':
    #loader=unittest.TestLoader()
    #k=loader.loadTestsFromTestCase(test_defs)
    k1=unittest.TestSuite(test_defs)
    k2=unittest.TextTestRunner()
    k2.run(k1)

    #unittest.main()