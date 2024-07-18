from aspose.page.eps import *
from aspose.page.eps.device import *
from util import Util

class PostScriptToPdf:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_conversion()

        # Initialize PsDocument with the input PostScript file.
        document = PsDocument(data_dir + "inputForImage.ps")
        
        # If you want to convert Postscript file despite of minor errors set this flag
        suppress_errors = True
        
        #Initialize options object with necessary parameters.
        options = PdfSaveOptions(suppress_errors)
        # If you want to add special folder where fonts are stored. Default fonts folder in OS is always included.
        options.additional_fonts_folders = [ """{FONT_FOLDER}""" ]
        # Default page size is 595x842 and it is not mandatory to set it in PdfSaveOptions
        # But if you need to specify sizeuse following line
        # PdfSaveOptions options = new PdfSaveOptions(suppressErrors, new Aspose.Page.Drawing.Size(595x842));
        # or
        # saveOptions.Size = new Aspose.Page.Drawing.Size(595, 842);

        # Save document as PDF
        document.save_as_pdf(data_dir + "outputPDF_out.pdf", options)
        # ExEnd:1
