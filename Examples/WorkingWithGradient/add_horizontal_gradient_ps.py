from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util


class AddHorizontalGradientPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_gradient()
        
        #Create output stream for PostScript document
        with open(data_dir + "HorizontalGradient_outPS.ps", "wb") as out_ps_stream:
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
                aspose.pydrawing.Color.from_argb(150, 0, 0, 0), aspose.pydrawing.Color.from_argb(50, 40, 128, 70), 0)
            #Create a transform for brush. X and Y scale component must be equal to width and height of the rectangle correspondingly.
            #Translation components are offsets of the rectangle
            brush_transform = aspose.pydrawing.drawing2d.Matrix(width, 0., 0., height, offset_x, offset_y)
            #Set transform
            brush.transform = brush_transform
            
            #Set paint
            document.set_paint(brush)
            
            #Fill the rectangle
            document.fill(path)
            
            #Fill text with gradient
            font = ExternalFontCache.fetch_dr_font("Arial", 96, aspose.pydrawing.FontStyle.BOLD)
            document.fill_and_stroke_text("ABC", font, 200, 300, brush,
            GraphicsFactory.create_pen_by_brush_and_width(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.black), 2))
            
            #Set current stroke
            document.set_stroke(GraphicsFactory.create_pen_by_brush_and_width(brush, 5))
            #Outline text with gradient
            document.outline_text("ABC", font, 200, 400)
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
