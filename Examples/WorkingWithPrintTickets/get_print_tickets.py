from aspose.page.xps import *
from aspose.page.xps.xpsmetadata import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class GetPrintTickets:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        dir = Util.get_data_dir_working_with_print_tickets()
        
        # Open XPS Document without print tickets
        x_docs = XpsDocument(dir + "input1.xps")
        
        # Get job print ticket
        job_print_ticket = x_docs.job_print_ticket
        
        # Get document print ticket
        doc_print_ticket = x_docs.get_document_print_ticket(1)
        
        # Get page print ticket
        page_print_ticket = x_docs.get_page_print_ticket(1, 1)
        
        
        # Save the document. Default print tickets are automatically added to document while saving.
        x_docs.save(dir + "output1.xps")
        
        # Open saved earlier XPS Document with print tickets
        x_docs2 = XpsDocument(dir + "output1.xps")
        
        # Print tickets must not be null
        
        print(x_docs2.job_print_ticket)
        
        print(x_docs2.get_document_print_ticket(1))
        
        print(x_docs2.get_page_print_ticket(1, 1))
        
        # ExEnd:1
