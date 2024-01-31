from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class ApplyDifferentColorSpacesXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_shapes()
        
        # Create new XPS Document
        doc = XpsDocument()
        
        # ARGB solid color filled rectangle
        rect1 = doc.add_path(doc.create_path_geometry("M 20,10 L 220,10 220,100 20,100 Z"))
        rect1.fill = doc.create_solid_color_brush(doc.create_color(aspose.pydrawing.Color.from_argb(222, 12, 15, 159)))
        
        # ARGB solid color filled rectangle, another way
        rect2 = doc.add_path(doc.create_path_geometry("M 20,210 L 220,210 220,300 20,300 Z"))
        rect2.fill = doc.create_solid_color_brush(doc.create_color(222, 12, 15, 159))
        
        # sRGB solid color filled rectangle
        rect3 = doc.add_path(doc.create_path_geometry("M 20,410 L 220,410 220,500 20,500 Z"))
        rect3.fill = doc.create_solid_color_brush(doc.create_color(12, 15, 159))
        
        # scRGB solid color filled rectangle
        rect4 = doc.add_path(doc.create_path_geometry("M 20,610 L 220,610 220,700 20,700 Z"))
        rect4.fill = doc.create_solid_color_brush(doc.create_color(0.08706, 0.04706, 0.05882, 0.62353))
        
        # CMYK (blue) solid color filled rectangle
        rect5 = doc.add_path(doc.create_path_geometry("M 20,810 L 220,810 220,900 20,900 Z"))
        rect5.fill = doc.create_solid_color_brush(
        doc.create_color(data_dir + "uswebuncoated.icc", [1.0, 1.000, 0.000, 0.000, 0.000]))
        
        # Save resultant XPS document
        doc.save(data_dir + "ApplyDifferentColorSpaces_outXPS.xps")
        # ExEnd:1
