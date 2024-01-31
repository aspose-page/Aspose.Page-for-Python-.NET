from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util


class ShowPseudoTransparencyPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_transparency()
        
        #Create output stream for PostScript document
        with open(data_dir + "ShowPseudoTransparency_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            offset_x = 50.
            offset_y = 100.
            width = 200.
            height = 100.
            
            ################################ Create rectangle with opaque gradient fill /////////////////////////////////////////////////////////
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_rectangle(aspose.pydrawing.RectangleF(offset_x, offset_y, width, height))
            
            opaque_brush: aspose.pydrawing.drawing2d.LinearGradientBrush = \
                GraphicsFactory.create_linear_gradient_brush_by_rect_and_angle(aspose.pydrawing.RectangleF(0, 0, 200, 100), aspose.pydrawing.Color.from_argb(0, 0, 0),
            aspose.pydrawing.Color.from_argb(40, 128, 70), 0)
            brush_transform = aspose.pydrawing.drawing2d.Matrix(width, 0., 0., height, offset_x, offset_y)
            opaque_brush.transform = brush_transform
            gradient_brush = GradientBrush(opaque_brush)
            gradient_brush.wrap_mode = aspose.pydrawing.drawing2d.WrapMode.CLAMP
            
            document.set_paint(gradient_brush)
            document.fill(path)
            ####################################################################################################################################
            
            offset_x = 350.
            
            ################################ Create rectangle with translucent gradient fill ///////////////////////////////////////////////////
            #Create graphics path from the first rectangle
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_rectangle(aspose.pydrawing.RectangleF(offset_x, offset_y, width, height))
            
            #Create linear gradient brush colors which transparency are not 255, but 150 and 50. So it are translucent.
            translucent_brush: aspose.pydrawing.drawing2d.LinearGradientBrush = \
                GraphicsFactory.create_linear_gradient_brush_by_rect_and_angle(aspose.pydrawing.RectangleF(0, 0, width, height),
                                                                               aspose.pydrawing.Color.from_argb(150, 0, 0, 0),
            aspose.pydrawing.Color.from_argb(50, 40, 128, 70), 0)
            #Create a transform for brush.
            brush_transform = aspose.pydrawing.drawing2d.Matrix(width, 0., 0., height, offset_x, offset_y)
            #Set transform
            translucent_brush.transform = brush_transform
            #Create GradientBrush object containing the linear gradient brush
            gradient_brush = GradientBrush(translucent_brush)
            gradient_brush.wrap_mode = aspose.pydrawing.drawing2d.WrapMode.CLAMP
            #Set paint
            document.set_paint(gradient_brush)
            #Fill the rectangle
            document.fill(path)
            ####################################################################################################################################
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
