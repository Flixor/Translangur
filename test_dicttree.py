from genericpath import exists
import os

import dicttree



xmlname = 'dicttree.xml'
if exists(xmlname):
    os.remove(xmlname)

d = dicttree.DictTree(xmlname)

def test_init():
    assert exists(xmlname)

