from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddTiledImageXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_images()
        # Create new XPS Document
        doc = XpsDocument()
        # Tile image
        # ImageBrush filled rectangle in the right top bellow
        path = doc.add_path(doc.create_path_geometry("M 10,160 L 228,160 228,305 10,305"))
        imageBrush: XpsImageBrush = doc.create_image_brush(data_dir + "R08LN_NN.jpg", aspose.pydrawing.RectangleF(0, 0, 128, 96),
            aspose.pydrawing.RectangleF(0, 0, 64, 48))
        path.fill = imageBrush
        imageBrush.tile_mode = XpsTileMode.TILE
        path.fill.opacity = 0.5
        # Save resultant XPS document
        doc.save(data_dir + "AddTiledImage_outXPS.xps")
        # ExEnd:1
