import unittest
import day2defs

class check_palindrome(unittest.TestCase):
  def test_palin(self):
    str1="abba"
    status=day2defs.palin(str1)
    self.assertEqual(status,"Palindrome")
  
  def test_matrix_mul(self):
    m1=[[2,2],
        [1,1]]
    m2=[[3,3],
        [1,1]]
    m3=[[0,0],
        [0,0]]
    st=day2defs.matrix_mul(m1,m2)
    self.assertEqual(st,[[8,8],[4,4]])

  def test_matrix_add(self):
    m1=[[2,2],
        [1,1]]
    m2=[[3,3],
        [1,1]]
    st=day2defs.matrix_add(m1,m2)
    self.assertEqual(st,[[5,5],[2,2]])

  def test_string(self):
    str10="string"
    str20=day2defs.stringee(str10)
    self.assertEqual(str20,"ng")

if __name__ == '__main__':
    unittest.main()
