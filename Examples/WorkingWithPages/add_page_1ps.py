from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class AddPage1PS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_pages()
        
        #Create output stream for PostScript document
        with open(data_dir + "document1.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            # Create new 2-paged PS Document
            document = PsDocument(out_ps_stream, options, 2)
            
            #Add the first page
            document.open_page(None)
            
            #Add content
            
            #Close the first page
            document.close_page()
            
            #Add the second page with different size
            document.open_page(400, 700)
            
            #Add content
            
            #Close the second page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
