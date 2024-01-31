from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
import aspose.pycore
from util import Util

class AddGlyphCloneAndChangeColor:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_cross_package_operations()
        
        # Create the first XPS Document
        doc1 = XpsDocument()
        
        # Add glyphs to the first document
        glyphs = doc1.add_glyphs("Times New Roman", 200, aspose.pydrawing.FontStyle.BOLD, 50, 250, "Test")
        
        # Fill glyphs in the first document with one color
        glyphs.fill = doc1.create_solid_color_brush(aspose.pydrawing.Color.green)
        
        # Create the second XPS Document
        doc2 = XpsDocument()
        
        # Add glyphs cloned from the one's from the first document
        glyphs = doc2.add_glyphs(glyphs.clone())
        
        # Fill glyphs in the second document with another color
        glyphs.fill = doc2.create_solid_color_brush(aspose.pydrawing.Color.red)
        
        # Save the first XPS document
        doc1.save(data_dir + "out1.xps")
        
        # Save the second XPS document
        doc2.save(data_dir + "out2.xps")
        # ExEnd:1
