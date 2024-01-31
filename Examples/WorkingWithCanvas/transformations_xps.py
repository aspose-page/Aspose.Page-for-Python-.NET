from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class TransformationsXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_canvas()
        
        # Create new XPS Document
        doc = XpsDocument()
        
        # Create main canvas, common for all page elemnts
        canvas1 = doc.add_canvas()
        
        # Make left and top offsets in the main canvas
        canvas1.render_transform = doc.create_matrix(1, 0, 0, 1, 20, 10)
        
        # Create rectangle path geometry
        rect_geom = doc.create_path_geometry("M 0,0 L 200,0 200,100 0,100 Z")
        
        # Create a fill for rectangles
        fill = doc.create_solid_color_brush(doc.create_color(12, 15, 159))
        
        # Add new canvas without any transformations to the main canvas
        canvas2 = canvas1.add_canvas()
        # Create rectangle in this canvas and fill it
        rect = canvas2.add_path(rect_geom)
        rect.fill = fill
        
        # Add new canvas with translate transformation to the main canvas
        canvas3 = canvas1.add_canvas()
        # Translate this canvas to position new rectangle below previous rectnagle
        canvas3.render_transform = doc.create_matrix(1, 0, 0, 1, 0, 200)
        # Translate this canvas to right side of page
        canvas3.render_transform.translate(500, 0)
        # Create rectangle in this canvas and fill it
        rect = canvas3.add_path(rect_geom)
        rect.fill = fill
        
        # Add new canvas with double scale transformation to the main canvas
        canvas4 = canvas1.add_canvas()
        # Translate this canvas to position new rectangle below previous rectnagle
        canvas4.render_transform = doc.create_matrix(1, 0, 0, 1, 0, 400)
        # Scale this canvas
        canvas4.render_transform.scale(2, 2)
        # Create rectangle in this canvas and fill it
        rect = canvas4.add_path(rect_geom)
        rect.fill = fill
        
        # Add new canvas with rotation around a point transformation to the main canvas
        canvas5 = canvas1.add_canvas()
        # Translate this canvas to position new rectangle below previous rectnagle
        canvas5.render_transform = doc.create_matrix(1, 0, 0, 1, 0, 800)
        # Rotate this canvas aroud a point on 45 degrees
        canvas5.render_transform.rotate_around(45, aspose.pydrawing.PointF(100, 50))
        rect = canvas5.add_path(rect_geom)
        rect.fill = fill
        
        # Save resultant XPS document
        doc.save(data_dir + "output1.xps")
        # ExEnd:1
