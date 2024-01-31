from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing
import io
from util import Util

class TransformationsPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_canvas()
        
        #Create output stream for PostScript document
        with open(data_dir + "Transformations_outPS.ps", "wb") as out_ps_stream:
            #Create save options with default values
            options = PsSaveOptions()
            
            # Create new 1-paged PS Document
            document = PsDocument(out_ps_stream, options, False)
            
            document.translate(100, 100)
            
            #Create graphics path from the rectangle
            path = aspose.pydrawing.drawing2d.GraphicsPath()
            path.add_rectangle(aspose.pydrawing.RectangleF(0, 0, 150, 100))
            
            ##################################### No transformations ///////////////////////////////////////////////////////////////
            #Set paint in graphics state on upper level
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.orange))
            
            #Fill the first rectangle that is on on upper level graphics state and that is without any transformations.
            document.fill(path)
            ########################################################################################################################
            
            
            
            ##################################### Translation //////////////////////////////////////////////////////////////////////
            
            #Save graphics state in order to return back to this state after transformation
            document.write_graphics_save()
            
            #Displace current graphics state on 250 to the right. So we add translation component to the current transformation.
            document.translate(250., 0.)
            
            #Set paint in the current graphics state
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue))
            
            #Fill the second rectangle in the current graphics state (has translation transformation)
            document.fill(path)
            
            #Restore graphics state to the previus (upper) level
            document.write_graphics_restore()
            ########################################################################################################################
            
            
            #Displace on 200 to the bottom.
            document.translate(0., 200.)
            
            ##################################### Scaling //////////////////////////////////////////////////////////////////////////
            #Save graphics state in order to return back to this state after transformation
            document.write_graphics_save()
            
            #Scale current graphics state on 0.5 in X axis and on 0.75f in Y axis. So we add scale component to the current transformation.
            document.scale(0.5, 0.75)
            
            #Set paint in the current graphics state
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.red))
            
            #Fill the third rectangle in the current graphics state (has scale transformation)
            document.fill(path)
            
            #Restore graphics state to the previus (upper) level
            document.write_graphics_restore()
            #####################################################################################################################
            
            
            #Displace upper level graphics state on 250 to the right.
            document.translate(250., 0.)
            
            
            ##################################### Rotation //////////////////////////////////////////////////////////////////////
            #Save graphics state in order to return back to this state after transformation
            document.write_graphics_save()
            
            #Rotate current graphics state on 45 degrees around origin of current graphics state (350, 300). So we add rotation component to the current transformation.
            document.rotate(float(45))
            
            #Set paint in the current graphics state
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.green))
            
            #Fill the fourth rectangle in the current graphics state (has rotation transformation)
            document.fill(path)
            
            #Restore graphics state to the previus (upper) level
            document.write_graphics_restore()
            #####################################################################################################################
            
            
            #Returns upper level graphics state back to the left and displace on 200 to the bottom.
            document.translate(-250., 200.)
            
            
            ##################################### Shearing //////////////////////////////////////////////////////////////////////
            #Save graphics state in order to return back to this state after transformation
            document.write_graphics_save()
            
            #Shear current graphics state. So we add shear component to the current transformation.
            document.shear(0.1, 0.2)
            
            #Set paint in the current graphics state
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.pink))
            
            #Fill the fifth rectangle in the current graphics state (has shear transformation)
            document.fill(path)
            
            #Restore graphics state to the previus (upper) level
            document.write_graphics_restore()
            #####################################################################################################################
            
            
            #Displace upper level graphics state on 250 to the right.
            document.translate(250., 0.)
            
            
            ##################################### Complex transformation ////////////////////////////////////////////////////////
            #Save graphics state in order to return back to this state after transformation
            document.write_graphics_save()
            
            #Transform current graphics state with complex transformation. So we add translation, scale and rotation components to the current transformation.
            document.transform(aspose.pydrawing.drawing2d.Matrix(1.2, -0.965925, 0.258819, 1.5, 0., 50.))
            
            #Set paint in the current graphics state
            document.set_paint(aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.aquamarine))
            
            #Fill the sixth rectangle in the current graphics state (has complex transformation)
            document.fill(path)
            
            #Restore graphics state to the previus (upper) level
            document.write_graphics_restore()
            #####################################################################################################################
            
            
            #Returns upper level graphics state back to the left and displace on 200 to the bottom.
            document.translate(-250., 200.)
            
            
            ##################################### Again no transformation ////////////////////////////////////////////////////////
            # Demonstrates that current graphics state's color is orange that was set up at the beginning of the code. 
            #Fill the seventh rectangle in the current graphics state (has no transformation)
            document.fill(path)
            #####################################################################################################################
            
            #Close current page
            document.close_page()
            
            #Save the document
            document.save()
        # ExEnd:1
