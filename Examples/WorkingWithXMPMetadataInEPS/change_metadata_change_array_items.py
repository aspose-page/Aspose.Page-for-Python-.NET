from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
from util import Util

class ChangeMetadata_ChangeArrayItems:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_xmp_metadata_in_eps()
        # Initialize EPS file input stream
        ps_stream = open(data_dir + "add_simple_props_input.eps", "rb",)
        # Create PsDocument instance from stream
        document = PsDocument(ps_stream)
        
        try:
            # Get XMP metadata. If EPS file doesn't contain XMP metadata we get new one filled with values from PS metadata comments (%%Creator, %%CreateDate, %%Title etc)
            xmp = document.get_xmp_metadata()
            
            #Change XMP metadata values
            
            # Change title item at index 0
            xmp.set_array_item("dc:title", 0, XmpValue("NewTitle"))
            
            # Change creator item at index 0
            xmp.set_array_item("dc:creator", 0, XmpValue("NewCreator"))
            
            # Save EPS file with changed XMP metadata
            
            # Create ouput stream
            with open(data_dir + "change_array_items_output.eps", "wb") as out_ps_stream:
                # Save EPS file
                document.save(out_ps_stream)
            
        finally:
            ps_stream.close()
        
        # ExEnd:1
