from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
import math
from util import Util


class AddDiagonalGradientPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_gradient()
        
        #Create output stream for PostScript document
        with open(data_dir + "DiagonaGradient_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            offset_x = 200.
            offset_y = 100.
            width = 200.
            height = 100.
            
            #Create graphics path from the first rectangle
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_rectangle(aspose.pydrawing.RectangleF(offset_x, offset_y, width, height))
            
            #Create linear gradient brush with rectangle as a bounds, start and end colors
            brush = GraphicsFactory.create_linear_gradient_brush_by_rect_and_angle(aspose.pydrawing.RectangleF(0, 0, width, height),
            aspose.pydrawing.Color.from_argb(255, 255, 0, 0), aspose.pydrawing.Color.from_argb(255, 0, 0, 255), 0)
            
            #Create a transform for brush. X and Y scale component must be equal to width and height of the rectangle correspondingly.
            #Translation components are offsets of the rectangle                
            brush_transform = aspose.pydrawing.drawing2d.Matrix(width, 0., 0., height, offset_x, offset_y)
            #Rotate gradient, than scale and translate to get visible color transition in required rectangle
            brush_transform.rotate(-45.)
            hypotenuse = float(math.sqrt(200. * 200. + 100. * 100.))
            ratio = hypotenuse / 200.
            brush_transform.scale(-ratio, 1.)
            brush_transform.translate(100. / brush_transform.elements[0], 0.)
            
            #Set transform
            brush.transform = brush_transform
            
            #Set paint
            document.set_paint(brush)
            
            #Fill the rectangle
            document.fill(path)
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
