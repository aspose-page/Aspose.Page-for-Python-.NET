from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddRectangleXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_shapes()
        # Create new XPS Document
        doc = XpsDocument()
        # CMYK (blue) solid color stroked rectangle in the lower left
        path = doc.add_path(doc.create_path_geometry("M 20,10 L 220,10 220,100 20,100 Z"))
        path.stroke = doc.create_solid_color_brush(
        doc.create_color(data_dir + "uswebuncoated.icc", [1.0, 1.000, 0.000, 0.000, 0.000]))
        path.stroke_thickness = 12
        # Save resultant XPS document
        doc.save(data_dir + "AddRectangleXPS_out.xps")
        # ExEnd:1
