from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class SetOpacityMaskXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_transparency()
        # Create new XPS Document
        doc = XpsDocument()
        #Add Canvas to XpsDocument instance
        canvas = doc.add_canvas()
        # Rectangle with opacity masked by ImageBrush
        path = canvas.add_path(doc.create_path_geometry("M 10,180 L 228,180 228,285 10,285"))
        path.fill = doc.create_solid_color_brush(doc.create_color(1.0, 0.0, 0.0))
        imageBrush: XpsImageBrush = doc.create_image_brush(data_dir + "R08SY_NN.tif", aspose.pydrawing.RectangleF(0, 0, 128, 192),
                aspose.pydrawing.RectangleF(0, 0, 64, 96))
        path.opacity_mask = imageBrush
        imageBrush.tile_mode = XpsTileMode.TILE
        # Save resultant XPS document
        doc.save(data_dir + "OpacityMask_out.xps")
        # ExEnd:1
