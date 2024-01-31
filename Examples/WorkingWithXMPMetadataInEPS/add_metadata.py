from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
from util import Util

class AddMetadata:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_xmp_metadata_in_eps()
        # Initialize EPS file input stream
        ps_stream = open(data_dir + "add_input.eps", "rb",)
        # Create PsDocument instance from stream
        document = PsDocument(ps_stream)
        
        try:
            # Get XMP metadata. If EPS file doesn't contain XMP metadata we get new one filled with values from PS metadata comments (%%Creator, %%CreateDate, %%Title etc)
            xmp = document.get_xmp_metadata()
            
            # Check metadata values extracted from PS metadata comments and set up in new XMP metadata
            
            # Get "CreatorTool" value
            if xmp.contains("xmp:CreatorTool"):
                print("CreatorTool: " + xmp.get_value("xmp:CreatorTool").to_string_value())
            
            # Get "CreateDate" value
            if xmp.contains("xmp:CreateDate"):
                print("CreateDate: " + xmp.get_value("xmp:CreateDate").to_string_value())
            
            # Get "format" value
            if xmp.contains("dc:format"):
                print("Format: " + xmp.get_value("dc:format").to_string_value())
            
            # Get "title" value
            if xmp.contains("dc:title"):
                print("Title: " + xmp.get_value("dc:title").to_array()[0].to_string_value())
            
            # Get "creator" value
            if xmp.contains("dc:creator"):
                print("Creator: " + xmp.get_value("dc:creator").to_array()[0].to_string_value())
            
            # Get "MetadataDate" value
            if xmp.contains("xmp:MetadataDate"):
                print("MetadataDate: " + xmp.get_value("xmp:MetadataDate").to_string_value())
            
            # Save EPS file with new XMP metadata
            
            # Create ouput stream
            with open(data_dir + "add_output.eps", "wb") as out_ps_stream:
                # Save EPS file
                document.save(out_ps_stream)
            
        finally:
            ps_stream.close()
        
        # ExEnd:1
