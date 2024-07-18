from aspose import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import io
import os
import aspose
from util import Util

class PostScriptToImage:

    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_document_conversion()
        # Initialize output image stream
        image_format = aspose.page.drawing.imaging.ImageFormat.PNG

        # Initialize PsDocument with the input PostScript file
        document = PsDocument(data_dir + "inputForImage.ps")
        
        #Initialize options object with necessary parameters.
        options = ImageSaveOptions()
        # set up image format
        options.image_format = image_format;
        # If you want to add special folder where fonts are stored. Default fonts folder in OS is always included.
        options.additional_fonts_folders = [ """{FONT_FOLDER}""" ]

        # Save PS document as array of image bytes, one bytes array for one page.
        images_bytes = document.save_as_image(options)

        # Save images bytes arrays as image files.

        i = 0

        for image_bytes in images_bytes:
            image_path = os.path.abspath(data_dir + "out_image" + str(i) + ".png")
            with open(image_path, "wb") as fs:
                fs.write(image_bytes[0:0+len(image_bytes)])
            i += 1
        
        # ExEnd:1
