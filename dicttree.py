import os


class DictTree (object):

    def __init__(self, xmlname):
        if not os.path.isfile(xmlname):
            with open(xmlname, 'w') as f:
                pass
        

    def add_phrase(self, source, tlation):
        """
        Adds a phrase and its translation to the dictionary.

        Parameters:
            source (str): The source phrase.
            tl (str): The translations of the phrase.

        """
        pass
    

    def check_text(self, text):
        pass

