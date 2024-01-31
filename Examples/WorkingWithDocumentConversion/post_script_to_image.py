import aspose.pydrawing.imaging
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
        #image_format = aspose.pydrawing.Imaging.ImageFormat.png
        # Initialize PostScript input stream
        ps_stream = open(data_dir + "inputForImage.ps", "rb")
        
        document = PsDocument(ps_stream)
        
        # If you want to convert Postscript file despite of minor errors set this flag
        suppress_errors = True
        
        #Initialize options object with necessary parameters.
        options = ImageSaveOptions(suppress_errors)
        
        # If you want to add special folder where fonts are stored. Default fonts folder in OS is always included.
        options.additional_fonts_folders = [ """{FONT_FOLDER}""" ]
        
        # Default image format is PNG and it is not mandatory to set it in ImageDevice
        # Default image size is 595x842 and it is not mandatory to set it in ImageDevice
        device = ImageDevice(aspose.pydrawing.imaging.ImageFormat.png)
        # But if you need to specify size and image format use constructor with parameters
        #ImageDevice device = new ImageDevice(new aspose.pydrawing.Size(595, 842), aspose.pydrawing.imaging.ImageFormat.Jpeg);
        
        try:
            document.save(device, options)
        finally:
            ps_stream.close()
        
        images_bytes = device.images_bytes
        
        i = 0
        
        for image_bytes in images_bytes:
            image_path = os.path.abspath(data_dir + "out_image" + str(i) + ".png")
            with open(image_path, "wb") as fs:
                fs.write(image_bytes[0:0+len(image_bytes)])
            i += 1
        
        # ExEnd:1
