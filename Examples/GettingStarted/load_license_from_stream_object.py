from aspose.page import *
import io
import aspose.page
from util import Util

class LoadLicenseFromStreamObject:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_getting_started()
        # Initialize license object
        license = License()
        # Load license in FileStream
        my_stream = open("Aspose.Total.NET.lic", "rb")
        # Set license
        license.set_license(my_stream)
        print("License set successfully.")
        # ExEnd:1
