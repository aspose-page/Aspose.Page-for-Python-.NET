from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class AddEllipsePS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_shapes()
        
        #Create output stream for PostScript document
        with open(data_dir + "AddEllipse_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            #Create graphics path from the first ellipse
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_ellipse(aspose.pydrawing.RectangleF(250, 100, 150, 100))
            #Set paint
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.orange))
            #Fill the ellipse
            document.fill(path)
            
            #Create graphics path from the second ellipse
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_ellipse(aspose.pydrawing.RectangleF(250, 300, 150, 100))
            #Set stroke
            document.set_stroke(GraphicsFactory.create_pen_by_brush_and_width(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.red), 3))
            #Stroke (outline) the ellipse
            document.draw(path)
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
