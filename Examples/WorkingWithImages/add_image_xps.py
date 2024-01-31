from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddImageXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_images()
        # Create new XPS Document
        doc = XpsDocument()
        # Add Image
        path = doc.add_path(doc.create_path_geometry("M 30,20 l 258.24,0 0,56.64 -258.24,0 Z"))
        #Creating a matrix is optional, it can be used for proper positioning
        path.render_transform = doc.create_matrix(0.7, 0, 0, 0.7, 0, 20)
        #Create Image Brush
        path.fill = doc.create_image_brush(data_dir + "QL_logo_color.tif", aspose.pydrawing.RectangleF(0, 0, 258.24, 56.64),
        aspose.pydrawing.RectangleF(50, 20, 193.68, 42.48))
        # Save resultant XPS document
        doc.save(data_dir + "AddImage_outXPS.xps")
        # ExEnd:1
