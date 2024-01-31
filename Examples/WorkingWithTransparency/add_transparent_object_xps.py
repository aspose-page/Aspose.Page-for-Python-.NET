from aspose.page.xps import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util


class AddTransparentObjectXPS:
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_transparency()
        # Create new XPS Document
        doc = XpsDocument()
        
        # Just to demonstrate transparency
        doc.add_path(doc.create_path_geometry("M120,0 H400 v1000 H120")).fill = doc.create_solid_color_brush(aspose.pydrawing.Color.gray)
        doc.add_path(doc.create_path_geometry("M300,120 h600 V420 h-600")).fill = doc.create_solid_color_brush(aspose.pydrawing.Color.gray)
        
        # Create path with closed rectangle geometry
        path1: XpsPath = doc.create_path(doc.create_path_geometry("M20,20 h200 v200 h-200 z"))
        # Set blue solid brush to fill path1
        path1.fill = doc.create_solid_color_brush(aspose.pydrawing.Color.blue)
        # Add it to the current page
        path2: XpsPath = doc.add_path(path1)
        
        # path1 and path2 are the same as soon as path1 hasn't been placed inside any other element
        # (which means that path1 had no parent element).
        # Because of that rectangle's color on the page effectively turns to green
        path2.fill = doc.create_solid_color_brush(aspose.pydrawing.Color.green)
        
        # Now add path2 once again. Now path2 has parent. So path3 won't be the same as path2.
        # Thus a new rectangle is painted on the page ...
        path3: XpsPath = doc.add_path(path2)
        # ... and we shift it 300 units lower ...
        path3.render_transform = doc.create_matrix(1, 0, 0, 1, 0, 300)
        # ... and set red solid brush to fill it
        path3.fill = doc.create_solid_color_brush(aspose.pydrawing.Color.red)
        
        # Create new path4 with path2's geometry ...
        path4: XpsPath = doc.add_path(path2.data)
        # ... shift it 300 units to the right ...
        path4.render_transform = doc.create_matrix(1, 0, 0, 1, 300, 0)
        # ... and set blue solid fill
        path4.fill = doc.create_solid_color_brush(aspose.pydrawing.Color.blue)
        
        # Add path4 once again.
        path5: XpsPath = doc.add_path(path4)
        # path4 and path5 are not the same again ...
        # (move path5 300 units lower)
        path5.render_transform = path5.render_transform.clone() # to disconnect RenderTransform value from path4 (see next comment about Fill property)
        path5.render_transform.translate(0, 300)
        # ... but if we set the opacity of Fill property, it will take effect on both path5 and path4
        # because brush is a complex property value which remains the same for path5 and path4
        path5.fill.opacity = 0.8
        
        # Create new path6 with path2's geometry ...
        path6: XpsPath = doc.add_path(path2.data)
        # ... shift it 600 units to the right ...
        path6.render_transform = doc.create_matrix(1, 0, 0, 1, 600, 0)
        # ... and set yellow solid fill
        path6.fill = doc.create_solid_color_brush(aspose.pydrawing.Color.yellow)
        
        # Now add path6's clone ...
        path7: XpsPath = doc.add_path(path6.clone())
        # (move path5 300 units lower)
        path7.render_transform = path7.render_transform.clone()
        path7.render_transform.translate(0, 300)
        # ... and set opacity for path7
        path7.fill.opacity = 0.8
        # Now opacity effects independantly as soon as property values are cloned along with the element
        
        # The following code block is equivalent to the previous one.
        # Add path6 itself. path6 and path7 are not the same. Although their Fill property values are the same 
        #XpsPath path7 = doc.add_path(path6);
        #path7.RenderTransform = path7.RenderTransform.Clone();
        #path7.RenderTransform.Translate(0, 300);
        # To "disconnect" path7's Fill property from path6's Fill property reassign it to its clone (or path6's Fill clone)
        #path7.Fill = ((XpsSolidColorBrush)path7.Fill).Clone();
        #path7.Fill.Opacity = 0.8f;
        
        # Save resultant XPS document
        doc.save(data_dir + "WorkingWithTransparency_out.xps")
        # ExEnd:1
