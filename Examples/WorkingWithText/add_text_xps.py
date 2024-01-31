from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class AddTextXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_text()
        # Create new XPS Document
        doc = XpsDocument()
        #Create a brush 
        text_fill = doc.create_solid_color_brush(aspose.pydrawing.Color.black)
        #Add glyph to the document
        glyphs = doc.add_glyphs("Arial", 12, aspose.pydrawing.FontStyle.REGULAR, 300, 450, "Hello World!")
        glyphs.fill = text_fill
        # Save resultant XPS document
        doc.save(data_dir + "AddText_out.xps")
        # ExEnd:1
