from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
import io
from util import Util

class ApplyMeteredLicense:
    @staticmethod
    def run():
        # ExStart:1
        # set metered public and private keys
        metered = Metered()
        # Access the setMeteredKey property and pass public and private keys as parameters
        metered.set_metered_key(
        "<type public key here>",
        "<type private key here>")
        
        # The path to the documents directory.
        data_dir = Util.get_data_dir_getting_started()
        #Create file stream for EPS file
        ps_stream = open(data_dir + "input.eps", "rb")
        #Create an instance of PostScript document from PS/EPS file
        document = PsDocument(data_dir + "input.eps")
        #Save EPS file as images bytes. One bytes array for one page. In our case we have one page.
        images_bytes = document.save_as_image(ImageSaveOptions())
        #Save image bytes to file
        with open(data_dir + "eps_out.png", "wb") as fos:
            fos.write(images_bytes[0][0:0+len(images_bytes[0])])
        
        #Now we can check visually if Metered License is applied.
        #If resulting image doesn't contain red evaluation message It means Metered License is applied successfully.
        # ExEnd:1
