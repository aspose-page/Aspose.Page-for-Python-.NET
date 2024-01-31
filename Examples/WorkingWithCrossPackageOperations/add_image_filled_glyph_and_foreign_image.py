from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class AddImageFilledGlyphAndForeignImage:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_cross_package_operations()
        
        # Create the first XPS Document
        doc1 = XpsDocument()
        
        # Add glyphs to the first document
        glyphs1 = doc1.add_glyphs("Times New Roman", 200, aspose.pydrawing.FontStyle.BOLD, 50, 250, "Test")
        
        # Fill the glyphs with an image brush
        imageBrush: XpsImageBrush = doc1.create_image_brush(data_dir + "R08SY_NN.tif", aspose.pydrawing.RectangleF(0, 0, 128, 192),
        aspose.pydrawing.RectangleF(0, 0, 64, 96))
        imageBrush.tile_mode = XpsTileMode.TILE
        glyphs1.fill = imageBrush
        
        # Create the second XPS Document
        doc2 = XpsDocument()
        
        # Add glyphs with the font from the first document to the second document
        glyphs2 = doc2.add_glyphs(glyphs1.font, 200, 50, 250, "Test")
        
        # Create an image brush from the fill of the the first document and fill glyphs in the second document
        imageBrush2: XpsImageBrush = doc2.create_image_brush(imageBrush.image, aspose.pydrawing.RectangleF(0, 0, 128, 192),
        aspose.pydrawing.RectangleF(0, 0, 128, 192))
        glyphs2.fill = imageBrush2
        imageBrush2.tile_mode = XpsTileMode.TILE
        
        # Save the first XPS document
        doc1.save(data_dir + "out1.xps")
        
        # Save the second XPS document
        doc2.save(data_dir + "out2.xps")
        # ExEnd:1
