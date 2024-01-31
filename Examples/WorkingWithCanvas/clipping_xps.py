from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class ClippingXPS:
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
        rect_geom = doc.create_path_geometry("M 0,0 L 500,0 500,300 0,300 Z")
        
        # Create a fill for rectangles
        fill = doc.create_solid_color_brush(doc.create_color(12, 15, 159))
        
        # Add another canvas with clip to the main canvas
        canvas2 = canvas1.add_canvas()
        
        # Create circle geometry for clip
        clip_geom = doc.create_path_geometry("M250,250 A100,100 0 1 1 250,50 100,100 0 1 1 250,250")
        canvas2.clip = clip_geom
        
        # Create rectangle in this canvas and fill it
        rect = canvas2.add_path(rect_geom)
        rect.fill = fill
        
        # Add the second canvas with stroked rectangle to the main canvas
        canvas3 = canvas1.add_canvas()
        
        # Create rectangle in this canvas and stroke it
        rect = canvas3.add_path(rect_geom)
        rect.stroke = fill
        rect.stroke_thickness = 2
        
        # Save resultant XPS document
        doc.save(data_dir + "output2.xps")
        # ExEnd:1
