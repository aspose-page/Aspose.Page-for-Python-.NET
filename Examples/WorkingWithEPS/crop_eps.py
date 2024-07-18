from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
import aspose.pydrawing
import io
from util import Util

class CropEPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_eps()
        
        #Initialize PsDocument object with EPS file
        doc = PsDocument(data_dir + "input.eps")

        #Get initial bounding box of EPS image
        initial_bounding_box = doc.extract_eps_bounding_box()

        #Create new bounding box
        #Bounding box is represented by 4 numbers: x0, y0, x, y, where x0 - left margin, y0 - top margin, x - (x0 + width), y - (y0 + height)
        new_bounding_box = [ 260, 300, 480, 432 ]

        #Crop EPS image and save to the output EPS file
        #Croping of image is changing of its bounding box so that new values of bounding box will be within initial bounding box, that is
        #initialBoundingBox[0] <= newBoundingBox[0] <= initialBoundingBox[2]
        #initialBoundingBox[1] <= newBoundingBox[1] <= initialBoundingBox[3]
        #initialBoundingBox[0] <= newBoundingBox[2] <= initialBoundingBox[2]
        #initialBoundingBox[1] <= newBoundingBox[3] <= initialBoundingBox[3]
        doc.crop_eps(data_dir + "output_crop.eps", new_bounding_box)
        # ExEnd:1

