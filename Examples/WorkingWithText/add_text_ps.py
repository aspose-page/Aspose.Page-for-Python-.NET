from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.font import *
import aspose.pydrawing
import io
from util import Util

class AddTextPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_text()
        
        fonts_folder = Util.get_data_dir_data() + """necessary_fonts/"""
        
        #Create output stream for PostScript document
        with open(data_dir + "AddText_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            # Set custom fonts folder. It will be added to system fonts folders for finding needed font.
            options.additional_fonts_folders = [ fonts_folder ]
            #A text to write to PS file
            str = "ABCDEFGHIJKLMNO"
            font_size: float = 48
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            ##################################### Using sysem font (located in system fonts folders) for filling text //////////////////
            font = aspose.page.ExternalFontCache.create_font_by_family_name("Times New Roman", font_size, aspose.pydrawing.FontStyle.BOLD)
            #Fill text with default or already defined color. In given case it is black.
            document.fill_text(str, font, 50, 100)
            #Fill text with Blue color.
            document.fill_text(str, font, 50, 150, aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue))
            ############################################################################################################################
            
            ##################################### Using custom font (located in custom fonts folders) for filling text /////////////////
            dr_font = aspose.page.ExternalFontCache.fetch_dr_font("Palatino Linotype", font_size, aspose.pydrawing.FontStyle.REGULAR)
            #Fill text with default or already defined color. In given case it is black.
            document.fill_text(str, dr_font, 50, 200)
            #Fill text with Blue color.
            document.fill_text(str, dr_font, 50, 250, aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue))
            ############################################################################################################################
            
            ##################################### Using sysem font (located in system fonts folders) for outlining text ////////////////
            #Outline text with default or already defined aspose.pydrawing.Pen. In given case it is black colored 1-points width aspose.pydrawing.Pen.
            document.outline_text(str, font, 50, 300)
            #Outline text with blue-violet colored 2-points width aspose.pydrawing.Pen.
            pen = GraphicsFactory.create_pen_by_brush_and_width(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue_violet), 2)
            document.outline_text(str, font, 50, 350, pen)
            #Fill text with orange color and stroke with blue colored 2-points width aspose.pydrawing.Pen.
            document.fill_and_stroke_text(str, font, 50, 400, aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.yellow),
             GraphicsFactory.create_pen_by_brush_and_width(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue_violet), 2))
            ############################################################################################################################
            
            ##################################### Using custom font (located in custom fonts folders) for outlining text /////////////////
            #Outline text with default or already defined aspose.pydrawing.Pen. In given case it is black colored 1-points width aspose.pydrawing.Pen.
            document.outline_text(str, dr_font, 50, 450)
            #Outline text with blue-violet colored 2-points width aspose.pydrawing.Pen.
            document.outline_text(str, dr_font, 50, 500,
                GraphicsFactory.create_pen_by_brush_and_width(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue_violet), 2))
            #Fill text with orange color and stroke with blue colored 2-points width aspose.pydrawing.Pen.
            document.fill_and_stroke_text(str, dr_font, 50, 550, aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.orange),
                GraphicsFactory.create_pen_by_brush_and_width(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue), 2))
            ##############################################################################################################################
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
