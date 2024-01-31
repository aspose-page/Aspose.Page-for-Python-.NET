from aspose.page.eps import *
from aspose.page.eps.device import *
from util import Util

class PostScriptToPdf:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_conversion()
        # Initialize PDF output stream
        pdf_stream = open(data_dir + "outputPDF_out.pdf", "wb")
        # Initialize PostScript input stream
        ps_stream = open(data_dir + "input.ps", "rb",)
        document = PsDocument(ps_stream)
        
        # If you want to convert Postscript file despite of minor errors set this flag
        suppress_errors = True
        
        #Initialize options object with necessary parameters.
        options = PdfSaveOptions(suppress_errors)
        # If you want to add special folder where fonts are stored. Default fonts folder in OS is always included.
        options.additional_fonts_folders = [ """{FONT_FOLDER}""" ]
        
        # Default page size is 595x842 and it is not mandatory to set it in PdfDevice
        device = PdfDevice(pdf_stream)
        # But if you need to specify size and image format use following line
        #Aspose.Page.EPS.Device.PdfDevice device = new Aspose.Page.EPS.Device.PdfDevice(pdfStream, new aspose.pydrawing.Size(595, 842));
        
        try:
            document.save(device, options)
        finally:
            ps_stream.close()
            pdf_stream.close()
        
        # ExEnd:1
