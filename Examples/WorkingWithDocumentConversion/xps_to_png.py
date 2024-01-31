import aspose
from aspose.page.xps import *
from aspose.page.xps.presentation.image import *
import io
import os
from util import Util

class XPStoPNG:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_conversion()
        # Input file
        input_file_name = data_dir + "input.xps"
        #Outut file 
        output_file_name = data_dir + "XPStoImage_out.png"
        # Initialize XPS input stream
        with open(input_file_name, "rb",) as xps_stream:
            # Load XPS document form the stream
            document = XpsDocument(xps_stream, XpsLoadOptions())
            # or load XPS document directly from file. No xpsStream is needed then.
            # XpsDocument document = new XpsDocument(inputFileName, new XpsLoadOptions());
            
            # Initialize options object with necessary parameters.
            options = PngSaveOptions()
            
            options.smoothing_mode = aspose.pydrawing.drawing2d.SmoothingMode.HIGH_QUALITY
            options.resolution = 300
            options.page_numbers = [ 1, 2, 6 ]
            
            # Create rendering device for PDF format
            device = ImageDevice()
            
            document.save(device, options)
            
            # Iterate through document partitions (fixed documents, in XPS terms)
            for i in range(len(device.result)):
                # Iterate through partition pages
                for j in range(len(device.result[i])):
                    # Initialize image output stream
                    with open(os.path.splitext(output_file_name)[0] + "_" + str(i + 1) + "_" + str(j + 1) +
                              os.path.splitext(output_file_name)[1], "wb") as image_stream:
                        # Write image
                        image_stream.write(device.result[i][j][0:0+len(device.result[i][j])])
        # ExEnd:1
