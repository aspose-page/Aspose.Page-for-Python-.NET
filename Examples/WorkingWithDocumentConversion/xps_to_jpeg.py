import aspose
from aspose.page.xps import *
from aspose.page.xps.presentation.image import *
import io
import os
from util import Util

class XPStoJPEG:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_conversion()
        #Output file
        output_file_name = data_dir + "XPStoImage_out.jpeg"

        # Load XPS document form the file
        document = XpsDocument(data_dir + "input.xps", XpsLoadOptions())

        # Initialize options object with necessary parameters.
        options = JpegSaveOptions()

        options.smoothing_mode = aspose.pydrawing.drawing2d.SmoothingMode.HIGH_QUALITY
        options.resolution = 300
        options.page_numbers = [ 1, 2, 6 ]

        # Save XPS document to the images byte arrays. The first dimension is for inner documents
        # and the second one is for pages within inner documents.
        imagesBytes = document.save_as_image(options)

        # Iterate through document partitions (fixed documents, in XPS terms)
        for i in range(len(imagesBytes)):
            # Iterate through partition pages
            for j in range(len(imagesBytes[i])):
                # Initialize image output stream
                with open(os.path.splitext(output_file_name)[0] + "_" + str(i + 1) + "_" + str(j + 1) +
                          os.path.splitext(output_file_name)[1], "wb") as image_stream:
                    # Write image
                    image_stream.write(imagesBytes[i][j][0:0 + len(imagesBytes[i][j])])
        # ExEnd:1
