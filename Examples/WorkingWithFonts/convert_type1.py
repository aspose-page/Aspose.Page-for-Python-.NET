from aspose.page.eps import *
from util import Util

class ConvertType1Font:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_fonts()
        
        #Create PsDocument object
        doc = PsDocument()

        #Convert Type1 font from the file 'Type1_Arial_Bold.ps' to TTF font in dataDir folder.
        #Exstension of file can be ".pfa", ".pfb", ".ps" or something else. The main thing is that there is a font Type1 inside.
        doc.convert_type_1_font_to_ttf(data_dir + "Type1_Arial_Bold.ps", data_dir);

        # ExEnd:1

