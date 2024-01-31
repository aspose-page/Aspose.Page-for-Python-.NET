from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
from util import Util

class SaveImageAsEPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_image_conversion()
        
        # Create default options
        options = PsSaveOptions()
        
        # Save JPEG image to EPS file
        PsDocument.save_image_as_eps(data_dir + "input1.jpg", data_dir + "output1.eps", options)
        
        # ExEnd:1
