from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class AddTransparentImagePS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_transparency()
        
        #Create output stream for PostScript document
        with open(data_dir + "AddTransparentImage_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            #Set page's background color to see white image on it's own transparent background
            options.background_color = aspose.page.drawing.Color.from_argb(211, 8, 48)
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            
            document.write_graphics_save()
            document.translate(20, 100)
            
            #Create bitmap from translucent image file
            with aspose.pydrawing.Bitmap(data_dir + "mask1.png") as image:
                #Add this image to document as usual opaque RGB image
                document.draw_image(image, aspose.pydrawing.drawing2d.Matrix(1., 0., 0., 1., 100., 0.), aspose.pydrawing.Color())
            
            #Again create bitmap from the same image file
            with aspose.pydrawing.Bitmap(data_dir + "mask1.png") as image:
                #Add this image to document as transparent image image
                document.draw_transparent_image(image, aspose.pydrawing.drawing2d.Matrix(1., 0., 0., 1., 350., 0.), 255)
            
            document.write_graphics_restore()
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
