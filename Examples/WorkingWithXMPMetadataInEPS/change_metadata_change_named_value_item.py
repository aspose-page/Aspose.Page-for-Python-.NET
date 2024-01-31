from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
from util import Util

class ChangeMetadata_ChangeNamedValueItem:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_xmp_metadata_in_eps()
        # Initialize EPS file input stream
        ps_stream = open(data_dir + "add_named_value_input.eps", "rb",)
        # Create PsDocument instance from stream
        document = PsDocument(ps_stream)
        
        try:
            # Get XMP metadata. If EPS file doesn't contain XMP metadata we get new one filled with values from PS metadata comments (%%Creator, %%CreateDate, %%Title etc)
            xmp = document.get_xmp_metadata()
            
            #Change XMP metadata values
            
            # Change named value "stDim:unit" in "xmpTPg:MaxPageSize" structure.
            xmp.set_named_value("xmpTPg:MaxPageSize", "stDim:unit", XmpValue("Inches"))
            
            # Add named value "stDim:newKey" in "xmpTPg:MaxPageSize" structure.
            xmp.set_named_value("xmpTPg:MaxPageSize", "stDim:newKey", XmpValue("NewValue"))
            
            # Save EPS file with changed XMP metadata
            
            # Create ouput stream
            with open(data_dir + "change_named_value_output.eps", "wb") as out_ps_stream:
                # Save EPS file
                document.save(out_ps_stream)
            
        finally:
            ps_stream.close()
        
        # ExEnd:1
