'''from aspose.page.xps import *
from aspose.page.xps.xpsmetadata import *
from aspose.page.xps.xpsmodel import *
import aspose.pydrawing
from util import Util

class CreateCustomPrintTicket:
    class PageDevModeSnaphot(ParameterInit, IJobPrintTicketItem):
        def __init__(self, value):
            pass
    
    class Borders(Feature, NUp.INUpItem):
        def __init__(self, option, items):
            pass
        class BordersOption(Option):
            def __init__(self, name):
                pass
            on = BordersOption("ns0000:On")
            off = BordersOption("ns0000:Off")
            
        
    
    
    @staticmethod
    def run():
        # ExStart:1
        # The path to the documents directory.
        dir = Util.get_data_dir_working_with_print_tickets()
        
        # Create new XPS document
        x_docs = XpsDocument()
        
        # Add custom job print ticket
        x_docs.job_print_ticket = JobPrintTicket(
        PageDevModeSnaphot("SABlAGwAbABvACEAAAA="),             # Custom page parameter initializer
        DocumentCollate(Collate.CollateOption.Collated),
        JobCopiesAllDocuments(1),
        PageICMRenderingIntent(PageICMRenderingIntent.PageICMRenderingIntentOption.Photographs),
        PageColorManagement(PageColorManagement.PageColorManagementOption.None),
        JobNUpAllDocumentsContiguously(
        NUp.PresentationDirection(NUp.PresentationDirection.PresentationDirectionOption.RightBottom),
        Borders(Borders.BordersOption.on) #    Custom nested feature
        ).add_pages_per_sheet_option(1),
        PageMediaSize(PageMediaSize.PageMediaSizeOption.NorthAmericaLetter),
        JobInputBin(InputBin.InputBinOption.AutoSelect),
        JobDuplexAllDocumentsContiguously(Duplex.DuplexOption.OneSided),
        PageOrientation(PageOrientation.PageOrientationOption.Portrait),
        PageResolution(
        PageResolution.PageResolutionOption("ns0000:ESDL300x300")             # Custom page resolution option
        .SetResolutionX(300).SetResolutionY(300)),
        PageMediaType(PageMediaType.PageMediaTypeOption.Plain),
        PageOutputColor(PageOutputColor.PageOutputColorOption.Color.Clone().SetDeviceBitsPerPixel(0).SetDriverBitsPerPixel(24)))
        
        
        # Save the document with custom job print ticket.
        x_docs.save(dir + "output1.xps")
'''
        # ExEnd:1
