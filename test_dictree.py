from genericpath import exists
import dicttree


xmlname = 'dicttree.xml'
d = dicttree.DictTree(xmlname)
try:
    assert(exists(xmlname))
except:
    print("DictTree init failed!")
