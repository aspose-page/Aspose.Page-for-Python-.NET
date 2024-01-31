from aspose.page import *
from util import Util

class SetLicenseUsingEmbeddedResource:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_getting_started()
        # Initialize license object
        license = License()
        # Set license
        license.set_license("MergedAPI.Aspose.Total.NET.lic")
        # Set the value to indicate that license will be embedded in the application
        license.embedded = True
        print("License set successfully.")
        # ExEnd:1
