from aspose.page.eps import *
from util import Util


class ConvertType3Font:

    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_fonts()

        # Create PsDocument object
        doc = PsDocument()

        #Convert outline Type3 font from the file 'Type3_outline.ps' to TTF font in dataDir folder.
        #Exstension of file can be ".ps" or something else. The main thing is that there is a font Type3 inside.
        doc.convert_type_3_font_to_ttf(data_dir + "Type3_outline.ps", data_dir);

        #Convert bitmap Type3 font from the file 'Type3_bitmap.ps' to TTF font in dataDir folder.
        doc.convert_type_3_font_to_ttf(data_dir + "Type3_bitmap.ps", data_dir);

        # ExEnd:1

