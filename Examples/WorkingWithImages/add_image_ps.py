from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class AddImagePS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_images()
        
        #Create output stream for PostScript document
        with open(data_dir + "AddImage_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            
            document.write_graphics_save()
            document.translate(100, 100)
            
            #Create a Bitmap object from image file
            with aspose.pydrawing.Bitmap(data_dir + "TestImage Format24bppRgb.jpg") as image:
                #Create image transform
                transform = aspose.pydrawing.drawing2d.Matrix()
                transform.translate(float(35), float(300))
                transform.scale(float(3), float(3))
                transform.rotate(float(-45))
                
                #Add image to document
                document.draw_image(image, transform, aspose.pydrawing.Color())
            
            document.write_graphics_restore()
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
