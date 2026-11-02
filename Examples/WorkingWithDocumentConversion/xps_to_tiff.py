import aspose
from aspose.page.xps import *
from aspose.page.xps.presentation.image import *
from util import Util

class XPStoTIFF:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_conversion()
        # Load XPS document from the file
        document = XpsDocument(data_dir + "input.xps", XpsLoadOptions())
        # or load XPS document directly from file. No xpsStream is needed then.
        # XpsDocument document = new XpsDocument(inputFileName, new XpsLoadOptions());

        # Initialize options object with necessary parameters.
        options = TiffSaveOptions()

        options.smoothing_mode = aspose.pydrawing.drawing2d.SmoothingMode.HIGH_QUALITY
        options.resolution = 300
        options.page_numbers = [ 1, 2, 6 ]

        # Save XPS document to image files.
        document.save_as_image(options, data_dir, "XPStoImage_out")
        # ExEnd:1
