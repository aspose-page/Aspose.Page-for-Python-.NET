import aspose
from aspose.page.eps import *
from aspose.page.eps.device import *
import io
from util import Util

class ClippingPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_canvas()
        
        #Create output stream for PostScript document
        with open(data_dir + "Clipping_outPS.ps", "wb") as out_ps_stream:
            #Create save options with default values
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            #Create graphics path from the rectangle
            rectange_path = aspose.pydrawing.drawing2d.GraphicsPath()
            rectange_path.add_rectangle(aspose.pydrawing.RectangleF(0, 0, 300, 200))
            
            ##################################### Clipping by shape //////////////////////////////////////////////////////////////////////
            
            #Save graphics state in order to return back to this state after transformation
            document.write_graphics_save()
            
            #Displace current graphics state on 100 points to the right and 100 points to the bottom.
            document.translate(100, 100)
            
            #Create graphics path from the circle
            circle_path = aspose.pydrawing.drawing2d.GraphicsPath()
            circle_path.add_ellipse(aspose.pydrawing.RectangleF(50, 0, 200, 200))
            
            #Add clipping by circle to the current graphics state
            document.clip(circle_path)
            
            #Set paint in the current graphics state
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue))
            
            #Fill the rectangle in the current graphics state (with clipping)
            document.fill(rectange_path)
            
            #Restore graphics state to the previus (upper) level
            document.write_graphics_restore()
            
            #Displace upper level graphics state on 100 points to the right and 100 points to the bottom.
            document.translate(100, 100)
            
            pen = aspose.pydrawing.Pen(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue))
            pen.width = float(2)
            pen.dash_style = aspose.pydrawing.drawing2d.DashStyle.DASH
            
            document.set_stroke(pen)
            
            #Draw the rectangle in the current graphics state (has no clipping) above clipped rectngle
            document.draw(rectange_path)
            
            ########################################################################################################################
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
