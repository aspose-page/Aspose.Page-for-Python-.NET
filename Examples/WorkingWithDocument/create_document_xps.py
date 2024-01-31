from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class CreateDocumentXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        dir = Util.get_data_dir_working_with_document()
        # Create new XPS Document
        x_docs = XpsDocument()
        
        # add glyph to the document
        glyphs = x_docs.add_glyphs("Arial", 12, aspose.pydrawing.FontStyle.REGULAR, 300, 450, "Hello World!")
        
        glyphs.fill = x_docs.create_solid_color_brush(aspose.pydrawing.Color.black)
        
        # save result
        x_docs.save(dir + "output.xps")
        # ExEnd:1
