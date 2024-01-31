from aspose.page.xps import *
from util import Util

class XPStoXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_merging()
        # Initialize XPS output stream
        with open(data_dir + "mergedXPSfiles.xps", "wb") as out_stream:
            # Initialize XPS input stream
            with open(data_dir + "input.xps", "rb") as in_stream:
                # Load XPS document from the stream
                document = XpsDocument(in_stream, XpsLoadOptions())
                # or load XPS document directly from file. No xpsStream is needed then.
                # XpsDocument document = new XpsDocument(inputFileName, new XpsLoadOptions());
                
                # Create an array of XPS files that will be merged with the first one
                files_to_merge = [ data_dir + "Demo.xps", data_dir + "sample.xps" ]
                
                # Merge XPS files to output PDF document
                document.merge(files_to_merge, out_stream)
        # ExEnd:1
