from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class AddPage2PS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_pages()
        
        #Create output stream for PostScript document
        with open(data_dir + "document2.ps", "wb") as out_ps_stream:
            #Create save options with A4 size
            options = PsSaveOptions()
            
            #Set variable that indicates if resulting PostScript document will be multipaged
            multi_paged = True
            
            # Create new multipaged PS Document with one page opened
            document = PsDocument(out_ps_stream, options, multi_paged)
            
            #Add content
            
            #Close the first page
            document.close_page()
            
            #Add the second page with different size
            document.open_page(500, 300)
            
            #Add content
            
            #Close the second page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
