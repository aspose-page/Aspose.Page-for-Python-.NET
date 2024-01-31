from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddHorizontalGradientXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_gradient()
        # Create new XPS Document
        doc = XpsDocument()
        # Initialize List of XpsGradentStop
        stops = []
        stops.append(doc.create_gradient_stop(doc.create_color(255, 244, 253, 225), 0.0673828))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 251, 240, 23), 0.314453))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 252, 209, 0), 0.482422))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 241, 254, 161), 0.634766))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 53, 253, 255), 0.915039))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 12, 91, 248), 1))
        # Create new path by defining geometery in abbreviation form
        path = doc.add_path(doc.create_path_geometry("M 10,210 L 228,210 228,300 10,300"))
        path.render_transform = doc.create_matrix(1, 0, 0, 1, 20, 70)
        gradient: XpsLinearGradientBrush = doc.create_linear_gradient_brush(aspose.pydrawing.PointF(10, 0), aspose.pydrawing.PointF(228, 0))
        path.fill = gradient
        gradient.gradient_stops.extend(stops)
        # Save resultant XPS document
        doc.save(data_dir + "AddHorizontalGradient_outXPS.xps")
        # ExEnd:1
