from aspose.page.xps import *
from aspose.page.xps.xpsmetadata import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class EditPrintTicket:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        dir = Util.get_data_dir_working_with_print_tickets()
        
        # Open XPS Document with print tickets
        x_docs = XpsDocument(dir + "input3.xps")
        
        pt = x_docs.job_print_ticket
        
        # Remove some parameters from job print ticket
        pt.remove(
        ["ns0000:PageDevmodeSnapshot",
        "ns0000:JobInterleaving",
        "ns0000:JobImageType"])
        
        # Add some parameters to job print ticket
        pt.add([JobCopiesAllDocuments(2),
        PageMediaSize([PageMediaSize.PageMediaSizeOption.isoa4])])
        
        # Save the document with changed job print ticket.
        x_docs.save(dir + "output3.xps")
        
        # ExEnd:1
