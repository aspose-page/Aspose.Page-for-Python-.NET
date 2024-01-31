from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddDiagonalGradientXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_gradient()
        # Create new XPS Document
        doc = XpsDocument()
        # Initialize List of XpsGradentStop
        stops = []
        # Add Colors to Gradient
        stops.append(doc.create_gradient_stop(doc.create_color(0, 142, 4), 0))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 202, 0), 0.144531))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 250, 0), 0.264648))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 0, 0), 0.414063))
        stops.append(doc.create_gradient_stop(doc.create_color(233, 0, 255), 0.544922))
        stops.append(doc.create_gradient_stop(doc.create_color(107, 27, 190), 0.694336))
        stops.append(doc.create_gradient_stop(doc.create_color(63, 0, 255), 0.844727))
        stops.append(doc.create_gradient_stop(doc.create_color(0, 199, 80), 1))
        # Create new path by defining geometery in abbreviation form
        path = doc.add_path(doc.create_path_geometry("M 10,10 L 228,10 228,100 10,100"))
        path.render_transform = doc.create_matrix(1, 0, 0, 1, 20, 70)
        gradient: XpsLinearGradientBrush = doc.create_linear_gradient_brush(aspose.pydrawing.PointF(10, 10), aspose.pydrawing.PointF(228, 100))
        path.fill = gradient
        gradient.gradient_stops.extend(stops)
        # Save resultant XPS document
        doc.save(data_dir + "AddDiagonalGradient_outXPS.xps")
        # ExEnd:1
