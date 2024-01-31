from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
from util import Util

class ChangeMetadata_AddArrayItems:
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
            
            # Add one more title. I will be added at the end of array by default.
            xmp.add_array_item("dc:title", XmpValue("NewTitle"))
            
            # Add one more creator. It will be added in the array by an index (0).
            xmp.add_array_item("dc:creator", 0, XmpValue("NewCreator"))
            
            # Save EPS file with changed XMP metadata
            
            # Create ouput stream
            with open(data_dir + "add_array_items_output.eps", "wb") as out_ps_stream:
                # Save EPS file
                document.save(out_ps_stream)
            
        finally:
            ps_stream.close()
        
        # ExEnd:1
