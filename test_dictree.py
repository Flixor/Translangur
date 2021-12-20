from genericpath import exists
import dicttree


xmlname = 'dicttree.xml'
d = dicttree.DictTree(xmlname)

def test_init():
    assert exists(xmlname+'f')

