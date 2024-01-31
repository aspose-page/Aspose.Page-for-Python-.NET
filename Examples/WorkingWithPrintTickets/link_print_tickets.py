from aspose.page.xps import *
from aspose.page.xps.xpsmetadata import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class LinkPrintTickets:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        dir = Util.get_data_dir_working_with_print_tickets()
        
        # Create new XPS document
        x_docs1 = XpsDocument()
        
        # Open XPS Document with print tickets
        x_docs2 = XpsDocument(dir + "input2.xps")
        
        # Link job print ticket
        x_docs1.job_print_ticket = x_docs2.job_print_ticket
        
        # Link document print ticket
        x_docs1.set_document_print_ticket(1, x_docs2.get_document_print_ticket(2))
        
        # Link page print ticket
        x_docs1.set_page_print_ticket(1, 1, x_docs2.get_page_print_ticket(3, 2))
        
        
        # Save the document with linked print tickets.
        x_docs1.save(dir + "output1.xps")
        
        # ExEnd:1
