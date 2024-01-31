from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class AddPageXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_pages()
        # Create new XPS Document
        doc = XpsDocument(data_dir + "Sample1.xps")
        
        # Insert an empty page at beginning of pages list
        doc.insert_page(1, True)
        
        # Save resultant XPS document
        doc.save(data_dir + "AddPages_out.xps")
        # ExEnd:1
