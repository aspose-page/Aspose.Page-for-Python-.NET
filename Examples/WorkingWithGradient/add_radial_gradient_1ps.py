from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util


class AddRadialGradient1PS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_gradient()
        
        #Create output stream for PostScript document
        with open(data_dir + "RadialGradient1_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            offset_x = 200.
            offset_y = 100.
            width = 200.
            height = 200.
            
            #Create graphics path from the rectangle bounds
            bounds = aspose.pydrawing.RectangleF(offset_x, offset_y, width, height)
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_ellipse(bounds)
            
            #Create and fill color blend object
            colors = [ aspose.pydrawing.Color.white, aspose.pydrawing.Color.white, aspose.pydrawing.Color.blue ]
            positions = [ 0.0, 0.2, 1.0 ]
            color_blend = aspose.pydrawing.drawing2d.ColorBlend()
            color_blend.colors = colors
            color_blend.positions = positions
            
            brush_rect = aspose.pydrawing.drawing2d.GraphicsPath()
            brush_rect.add_rectangle(aspose.pydrawing.RectangleF(0, 0, width, height))
            
            #Create path gradient brush with rectangle as a bounds
            brush = GraphicsFactory.create_path_gradient_brush_by_path(brush_rect)
            #Set interpolation colors
            brush.interpolation_colors = color_blend
            #Create a transform for brush. X and Y scale component must be equal to width and height of the rectangle correspondingly.
            #Translation components are offsets of the rectangle
            brush_transform = aspose.pydrawing.drawing2d.Matrix(width, 0., 0., height, offset_x, offset_y)
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
