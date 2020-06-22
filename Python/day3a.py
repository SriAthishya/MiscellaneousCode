
import unittest
import day3b

class day3(unittest.TestCase):
  def test_is_abecedarian(self):
    a=day3b.is_abecedarian("abcaklmnoeeffd")
    self.assertEqual(a,5)
  
  def test_anagram(self):
    b=day3b.anagram(["eat","tea","fariy","far","arf","apple"])
    self.assertEqual(b,["eat","tea","far","arf"])

  def test_subinary(self):
    c=day3b.subinary("100110110")
    self.assertEqual(c,"14")

  def test_vowels(self):
    d=day3b.vowels("I am walking")
    self.assertEqual(d,["walking","am","I"])

  def test_spring_mat(self):
    m1=[[2,2],
        [1,1]]
    m2=[[3,3],
        [1,1]]

    e=day3b.spring_mat(m1,m2)
    self.assertEqual(e,"8844")

  def test_mid_palin(self):
    f=day3b.mid_palin("cabbaz")
    self.assertEqual(f,4)

if __name__ == '__main__': 
    unittest.main()
