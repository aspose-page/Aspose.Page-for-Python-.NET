from aspose.page.eps import *
from aspose.page.eps.device import *
from util import Util

class MergePostScriptToPdf:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_merging()

        # Initialize PS document with the first PostScript file
        document = PsDocument(data_dir + "input.ps")
        
        # Create an array of PostScript files that will be merged with the first one
        files_for_merge = [ data_dir + "input2.ps", data_dir + "input3.ps" ]
        
        # If you want to convert Postscript file despite of minor errors set this flag
        suppress_errors = True
        
        #Initialize options object with necessary parameters.
        options = PdfSaveOptions(suppress_errors)
        # If you want to add special folder where fonts are stored. Default fonts folder in OS is always included.
        options.additional_fonts_folders = [ """{FONT_FOLDER}""" ]
        # Default page size is 595x842 and it is not mandatory to set it in SaveOptions
        # But if you need to specify the page size following line
        # options = PdfSaveOptions(suppressErrors, Size(595, 842));

        # Merge PS files to PDF document
        document.merge_to_pdf(data_dir + "outputPDF_out.pdf", files_for_merge, options)
        
        # ExEnd:1
