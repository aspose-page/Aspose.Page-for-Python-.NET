from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class RemovePageXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_pages()
        
        # Create new XPS Document
        doc = XpsDocument(data_dir + "Sample2.xps")
        
        # Remove the first page (at index 1).
        doc.remove_page_at(1)
        
        # Save resultant XPS document
        doc.save(data_dir + "Sample2_out.xps")
        # ExEnd:1
