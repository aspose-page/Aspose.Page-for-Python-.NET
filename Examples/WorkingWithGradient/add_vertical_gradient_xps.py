from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class AddVerticalGradientXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_gradient()
        # Create new XPS Document
        doc = XpsDocument()
        # Initialize List of XpsGradentStop
        stops = []
        stops.append(doc.create_gradient_stop(doc.create_color(253, 255, 12, 0), 0))
        stops.append(doc.create_gradient_stop(doc.create_color(252, 255, 154, 0), 0.359375))
        stops.append(doc.create_gradient_stop(doc.create_color(252, 255, 56, 0), 0.424805))
        stops.append(doc.create_gradient_stop(doc.create_color(253, 255, 229, 0), 0.879883))
        stops.append(doc.create_gradient_stop(doc.create_color(252, 255, 255, 234), 1))
        # Create new path by defining geometery in abbreviation form
        path = doc.add_path(doc.create_path_geometry("M 10,110 L 228,110 228,200 10,200"))
        path.render_transform = doc.create_matrix(1, 0, 0, 1, 20, 70)
        gradient: XpsLinearGradientBrush = doc.create_linear_gradient_brush(aspose.pydrawing.PointF(10, 110), aspose.pydrawing.PointF(10, 200))
        path.fill = gradient
        gradient.gradient_stops.extend(stops)
        # Save resultant XPS document
        doc.save(data_dir + "AddVerticalGradient_outXPS.xps")
        # ExEnd:1
