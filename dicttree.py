import os
from genericpath import exists


class DictTree (object):
    """
    The class defines a dictionary tree.
    It's called a dictionary because it is used to store 
    source phrases and their translations,
    but it also has a tree structure, in the form of an xml file.
    """


    def __init__(self, xmlname):
        """

        Parameters:
            xmlname (str): The name of the xml file to use, 
                and create if non-existent.

        """
        if not exists(xmlname):
            # create file without needing to call close()
            with open(xmlname, 'w') as f:
                pass
        

    def add(self, src, tl):
        """
        Adds a source phrase and its translation phrase to the dicttree.
        These phrases are assumed to be words (which format?),
        separated by whitespaces and/or punctuation marks. 

        The addition is destructive. Therefore, this method can also
        be used to modify previous entries.

        Parameters:
            src (str): The source phrase.
            tl (str): The translations of the phrase.

        """
        pass


    def remove(self, src):
        """
        Removes the translation of a source phrase from the dicttree.
        """
        pass
    

    def check_text(self, text):
        pass

