from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class AddHatchPatternPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_hatches()
        
        #Create output stream for PostScript document
        with open(data_dir + "AddHatchPattern_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            x0 = 20.
            y0 = 100.
            square_side = 32.
            width = 500.
            sum_x = 0.
            
            #Restore graphics state
            document.write_graphics_save()
            
            #Translate to initial point
            document.translate(x0, y0)
            
            #Create rectngle path for every pattern square
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_rectangle(aspose.pydrawing.RectangleF(0, 0, square_side, square_side))
            
            #Create pen for outlining pattern square
            pen = GraphicsFactory.create_pen_by_color_and_width(aspose.pydrawing.Color.black, 2)
            
            #For every hatch pattern style 
            hatch_style = 0
            while hatch_style <= 52:
                #Set paint with current hatch brush style
                document.set_paint(aspose.pydrawing.drawing2d.HatchBrush(aspose.pydrawing.drawing2d.HatchStyle(hatch_style),
                    aspose.pydrawing.Color.black, aspose.pydrawing.Color.white))
                
                #Calculate displacement in order to don't go beyond the page bounds
                x = square_side
                y = 0
                if sum_x >= width:
                    x = -(sum_x - square_side)
                    y += square_side
                #Translate current graphics state
                document.translate(x, y)
                #Fill pattern square
                document.fill(path)
                #Set stroke
                document.set_stroke(pen)
                #Draw square outline
                document.draw(path)
                
                #Calculate distance from X0
                if sum_x >= width:
                    sum_x = square_side
                else:
                    sum_x += x
                hatch_style += 1
            
            #Restore graphics state
            document.write_graphics_restore()
            
            #Fill text with hatch pattern
            brush = aspose.pydrawing.drawing2d.HatchBrush(aspose.pydrawing.drawing2d.HatchStyle.DIAGONAL_CROSS,
            aspose.pydrawing.Color.red, aspose.pydrawing.Color.yellow)
            font = ExternalFontCache.fetch_dr_font("Arial", 96, aspose.pydrawing.FontStyle.BOLD)
            document.fill_and_stroke_text("ABC", font, 200, 300, brush, pen)
            
            #Outline text with hatch pattern
            brush = aspose.pydrawing.drawing2d.HatchBrush(aspose.pydrawing.drawing2d.HatchStyle.PERCENT50,
            aspose.pydrawing.Color.blue, aspose.pydrawing.Color.white)
            document.outline_text("ABC", font, 200, 400, GraphicsFactory.create_pen_by_brush_and_width(brush, 5))
            
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        
        
        
        # ExEnd:1
