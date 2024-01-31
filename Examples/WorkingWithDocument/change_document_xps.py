from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
import io
from util import Util

class ChangeDocumentXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        dir = Util.get_data_dir_working_with_document()
        # Open a stream of XPS file
        with open(dir + "input1.xps", "rb") as xps_stream:
            # Create PS document from stream
            document = XpsDocument(xps_stream, XpsLoadOptions())
            
            # Create fill of the signature text
            text_fill = document.create_solid_color_brush(aspose.pydrawing.Color.blue_violet)
            
            # Define pages where signature will be set
            page_numbers = [1, 2, 3]
            
            # For every defined page set signature "Confirmed" at coordinates x=650 and y=950
            for i in range(len(page_numbers)):
                # Define active page
                document.select_active_page(page_numbers[i])
                
                # Create glyphs object
                glyphs = document.add_glyphs("Arial", 24, aspose.pydrawing.FontStyle.BOLD, 650, 900, "Confirmed")
                
                # define fill for glyphs
                glyphs.fill = text_fill
            
            # save changed XPS document
            document.save(dir + "input1_out.xps")
        # ExEnd:1
