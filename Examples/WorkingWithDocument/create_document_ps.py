from aspose.page.eps import *
from aspose.page.eps.device import *
import io
from util import Util

class CreateDocumentPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        dir = Util.get_data_dir_working_with_document()
        
        #Create output stream for PostScript document
        with open(dir + "document.ps", "wb") as out_ps_stream:
            #Create save options
            options = PsSaveOptions()
            #If you want to aassign page size other than A4, set page size in options
            options.page_size = PageConstants.get_size(PageConstants.SIZE_A4, PageConstants.ORIENTATION_PORTRAIT)
            #If you want to assign page margins other empty, set page margins in options
            options.margins = PageConstants.get_margins(PageConstants.MARGINS_ZERO)
            #If you plan to use fonts that located in non system folders, set additional fonts folders in options
            options.additional_fonts_folders = [ dir ]
            
            #Set variable that indicates if resulting PostScript document will be multipaged
            multi_paged = False
            
            # Create new multipaged PS Document with one page opened
            document = PsDocument(out_ps_stream, options, multi_paged)
            
            #Close current page
            document.close_page()
            #Save the document
            document.save()
        # ExEnd:1
