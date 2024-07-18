from aspose.page import *
from util import Util

class LoadLicenseFromFile:

    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_getting_started()
        # Initialize license object
        license = License()
        # Set license
        license.set_license("D:\\Aspose.Page.Python.via.NET.lic")
        print("License set successfully.")
        # ExEnd:1
