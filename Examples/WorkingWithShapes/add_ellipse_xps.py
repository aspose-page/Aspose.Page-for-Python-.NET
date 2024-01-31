from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddEllipseXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_shapes()
        # Create new XPS Document
        doc = XpsDocument()
        # Radial gradient stroked ellipse in the lower left
        stops = []
        stops.append(doc.create_gradient_stop(doc.create_color(0, 0, 255), 0))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 0, 0), .25))
        stops.append(doc.create_gradient_stop(doc.create_color(0, 255, 0), .5))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 255, 0), .75))
        stops.append(doc.create_gradient_stop(doc.create_color(255, 0, 0), 1))
        
        path = doc.add_path(doc.create_path_geometry("M 20,250 A 100,50 0 1 1 220,250 100,50 0 1 1 20,250"))
        stroke: XpsRadialGradientBrush = doc.create_radial_gradient_brush(aspose.pydrawing.PointF(575, 125), aspose.pydrawing.PointF(575, 100), 75, 50)
        path.stroke = stroke
        stroke.spread_method = XpsSpreadMethod.REFLECT
        stroke.gradient_stops.extend(stops)
        stops.clear()
        path.stroke_thickness = 12
        # Save resultant XPS document
        doc.save(data_dir + "AddEllipse_outXPS.xps")
        # ExEnd:1
