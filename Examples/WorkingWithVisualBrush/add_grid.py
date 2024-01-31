from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddGrid:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_visual_brush()
        
        doc = XpsDocument()
        # Geometry for magenta grid VisualBrush
        path_geometry = doc.create_path_geometry()
        path_geometry.add_segment(doc.create_poly_line_segment(
        [ aspose.pydrawing.PointF(240, 5), aspose.pydrawing.PointF(240, 310), aspose.pydrawing.PointF(0, 310) ], True))
        path_geometry[0].start_point = aspose.pydrawing.PointF(0, 5)
        
        # Canvas for magenta grid VisualBrush
        visual_canvas = doc.create_canvas()
        
        visual_path = visual_canvas.add_path(
        doc.create_path_geometry("M 0,4 L 4,4 4,0 6,0 6,4 10,4 10,6 6,6 6,10 4,10 4,6 0,6 Z"))
        visual_path.fill = doc.create_solid_color_brush(doc.create_color(1, .61, 0.1, 0.61))
        
        grid_path = doc.create_path(path_geometry)
        #Create Visual Brush, it is specified by some XPS fragment (vector graphics and glyphs)
        visualBrush: XpsVisualBrush = doc.create_visual_brush(visual_canvas,
            aspose.pydrawing.RectangleF(0, 0, 10, 10), aspose.pydrawing.RectangleF(0, 0, 10, 10))
        grid_path.fill = visualBrush
        visualBrush.tile_mode = XpsTileMode.TILE
        # New canvas
        canvas = doc.add_canvas()
        canvas.render_transform = doc.create_matrix(1, 0, 0, 1, 268, 70)
        # Add grid
        canvas.add_path(path_geometry)
        # Red transparent rectangle in the middle top
        path = canvas.add_path(doc.create_path_geometry("M 30,20 l 258.24,0 0,56.64 -258.24,0 Z"))
        path = canvas.add_path(doc.create_path_geometry("M 10,10 L 228,10 228,100 10,100"))
        path.fill = doc.create_solid_color_brush(doc.create_color(1.0, 0.0, 0.0))
        path.opacity = 0.7
        # Save resultant XPS document
        doc.save(data_dir + "AddGrid_out.xps")
        # ExEnd:1
