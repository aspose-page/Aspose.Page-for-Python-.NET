from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.font import *
import aspose.pydrawing
import io
from util import Util

class AddTextUsingUnicodeStringPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_text()
        
        fonts_folder = Util.get_data_dir_data() + """necessary_fonts/"""
        
        #Create output stream for PostScript document
        with open(data_dir + "AddTextUsingUnocodeString_outPS.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            # Set custom fonts folder. It will be added to system fonts folders for finding needed font.
            options.additional_fonts_folders = [ fonts_folder ]
            #A text to write to PS file
            str = "試してみます。"
            font_size = 48
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            ##################################### Using custom font (located in custom fonts folders) for filling text /////////////////
            dr_font = aspose.page.ExternalFontCache.fetch_dr_font("Arial Unicode MS", font_size, aspose.pydrawing.FontStyle.REGULAR)
            #Fill text with default or already defined color. In given case it is black.
            document.fill_text(str, dr_font, 50, 200)
            #Fill text with Blue color.
            document.fill_text(str, dr_font, 50, 250, aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue))
            ############################################################################################################################
            
            ##################################### Using custom font (located in custom fonts folders) for outlining text /////////////////
            #Outline text with default or already defined aspose.pydrawing.Pen. In given case it is black colored 1-points width aspose.pydrawing.Pen.
            #   document.OutlineText(str, drFont, 50, 450);
            # //Outline text with blue-violet colored 2-points width aspose.pydrawing.Pen.
            # document.OutlineText(str, drFont, 50, 500, new aspose.pydrawing.Pen(new SolidBrush(aspose.pydrawing.Color.BlueViolet), 2));
            # //Fill text with orange color and stroke with blue colored 2-points width aspose.pydrawing.Pen.
            # document.FillAndStrokeText(str, drFont, 50, 550, new SolidBrush(aspose.pydrawing.Color.Orange), new aspose.pydrawing.Pen(new SolidBrush(aspose.pydrawing.Color.Blue), 2));
            
            ##############################################################################################################################
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
