from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
from util import Util

class GetMetadata:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_xmp_metadata_in_eps()
        # Initialize EPS file input stream
        ps_stream = open(data_dir + "get_input.eps", "rb",)
        # Create PsDocument instance from stream
        document = PsDocument(ps_stream)
        
        try:
            # Get XMP metadata. If EPS file doesn't contain XMP metadata we get new one filled with values from PS metadata comments (%%Creator, %%CreateDate, %%Title etc)
            xmp = document.get_xmp_metadata()
            
            # Get "CreatorTool" value
            if xmp.contains("xmp:CreatorTool"):
                print("CreatorTool: " + xmp.get_value("xmp:CreatorTool").to_string_value())
            
            # Get "CreateDate" value
            if xmp.contains("xmp:CreateDate"):
                print("CreateDate: " + xmp.get_value("xmp:CreateDate").to_string_value())
            
            # Get a width of a thumbnail image if exists
            # Dictionaries are not supported by Cs2PythonWrapper now
            '''if xmp.contains("xmp:Thumbnails") and xmp.get_value("xmp:Thumbnails").is_array:
                val = xmp.get_value("xmp:Thumbnails").to_array()[0]
                if val.is_named_values and val.ToDictionary().contains("xmpGImg:width"):
                    print(f"Thumbnail Width: {val.ToDictionary().get('xmpGImg:width').to_integer()}")
            '''

            # Get "format" value
            if xmp.contains("dc:format"):
                print("Format: " + xmp.get_value("dc:format").to_string_value())
            
            # Get "DocumentID" value
            if xmp.contains("xmpMM:DocumentID"):
                print("DocumentID: " + xmp.get_value("xmpMM:DocumentID").to_string_value())
            
        finally:
            ps_stream.close()

        # ExEnd:1
