from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class AddTextureTilingPatternPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_textures()
        
        #Create output stream for PostScript document
        with open(data_dir + "AddTextureTilingPattern_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            
            document.write_graphics_save()
            document.translate(200, 100)
            
            #Create a Bitmap object from image file
            with aspose.pydrawing.Bitmap(data_dir + "TestTexture.bmp") as image:
                #Create texture brush from the image
                brush = aspose.pydrawing.TextureBrush(image, aspose.pydrawing.drawing2d.WrapMode.TILE)
                
                #Add scaling in X direction to the mattern
                transform = aspose.pydrawing.drawing2d.Matrix(float(2), float(0), float(0), float(1), float(0), float(0))
                brush.transform = transform
                
                #Set this texture brush as current paint
                document.set_paint(brush)
            
            #Create rectangle path
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_rectangle(aspose.pydrawing.RectangleF(0, 0, 200, 100))
            
            #Fill rectangle
            document.fill(path)
            
            #Get current paint
            paint = document.get_paint()
            
            #Set red stroke
            pen1 = aspose.pydrawing.Pen(aspose.pydrawing.Color.red)
            pen1.width = float(2)
            document.set_stroke(pen1)
            #Stroke the rectangle
            document.draw(path)
            
            document.write_graphics_restore()
            
            #Fill text with texture pattern                
            font = aspose.page.ExternalFontCache.create_font_by_family_name("Arial", 96, aspose.pydrawing.FontStyle.BOLD)
            pen2 = aspose.pydrawing.Pen(aspose.pydrawing.Color.black)
            pen2.width = float(2)
            document.fill_and_stroke_text("ABC", font, 200, 300, paint, pen2)
            
            #Outline text with texture pattern
            pen3 = aspose.pydrawing.Pen(aspose.pydrawing.Color.black)
            pen3.brush = paint
            pen3.width = float(5)
            document.outline_text("ABC", font, 200, 400, pen3)
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
