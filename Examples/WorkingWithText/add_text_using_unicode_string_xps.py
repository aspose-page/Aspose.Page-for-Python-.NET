from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class AddTextUsingUnicodeStringXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_text()
        # Create new XPS Document
        doc = XpsDocument()
        # Add Text
        text_fill = doc.create_solid_color_brush(aspose.pydrawing.Color.black)
        glyphs = doc.add_glyphs("Arial", 20, aspose.pydrawing.FontStyle.REGULAR, 400, 200, "TEN. rof SPX.esopsA")
        glyphs.bidi_level = 1
        glyphs.fill = text_fill
        # Save resultant XPS document
        doc.save(data_dir + "AddTextRTL_out.xps")
        # ExEnd:1
