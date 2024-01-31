from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class ManipulatePages:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_cross_package_operations()
        
        # Create the first XPS Document
        doc1 = XpsDocument(data_dir + "input1.xps")
        
        # Create the second XPS Document
        doc2 = XpsDocument(data_dir + "input2.xps")
        
        # Create the third XPS Document
        doc3 = XpsDocument(data_dir + "input3.xps")
        
        # Create the fourth XPS Document
        doc4 = XpsDocument()
        
        # Insert active page (1 in this case) from the second document to the beginning of the fourth document
        doc4.insert_page(1, doc2.page, False)
        
        # Insert active page (1 in this case) from the third document to the end of the fourth document
        doc4.add_page(doc3.page, False)
        
        # Remove page 2 from the fourth document. This is an empty page that was created when document has been created.
        doc4.remove_page_at(2)
        
        # Insert page 3 from the first document to the second postion of the fourth document
        doc4.insert_page(2, doc1.select_active_page(3), False)
        
        # Save the fourth XPS document
        doc4.save(data_dir + "out.xps")
        # ExEnd:1
