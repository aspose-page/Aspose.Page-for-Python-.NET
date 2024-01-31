from aspose.page import *
from aspose.page.eps import *
from aspose.page.eps.device import *
from aspose.page.eps.xmp import *
import aspose.pydrawing
import io
from util import Util

class ResizeEPS:
    @staticmethod
    def run_points():
        # ExStart:1
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_eps()
        
        #Create an input stream for EPS file
        with open(data_dir + "input.eps", "rb",) as input_eps_stream:
            #Initialize PsDocument object with input stream
            doc = PsDocument(input_eps_stream)
            
            #Get size of EPS image
            old_size = doc.extract_eps_size()
            
            #Create an output stream for resized EPS
            with open(data_dir + "output_resize_points.eps", "wb") as output_eps_stream:
                #Increase EPS size in 2 times and save to the output stream
                doc.resize_eps(output_eps_stream, aspose.pydrawing.SizeF(old_size.width * 2, old_size.height * 2), aspose.page.Units.POINTS)
        # ExEnd:1
    
    @staticmethod
    def run_inches():
        # ExStart:2
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_eps()
        
        #Create an input stream for EPS file
        with open(data_dir + "input.eps", "rb",) as input_eps_stream:
            #Initialize PsDocument object with input stream
            doc = PsDocument(input_eps_stream)
            
            #Get size of EPS image
            old_size = doc.extract_eps_size()
            
            #Create an output stream for resized EPS
            with open(data_dir + "output_resize_inches.eps", "wb") as output_eps_stream:
                #Save EPS to the output stream with new size assigned in inches
                doc.resize_eps(output_eps_stream, aspose.pydrawing.SizeF(5.791, 3.625), aspose.page.Units.INCHES)
        # ExEnd:2
    
    @staticmethod
    def run_mms():
        # ExStart:3
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_eps()
        
        #Create an input stream for EPS file
        with open(data_dir + "input.eps", "rb",) as input_eps_stream:
            #Initialize PsDocument object with input stream
            doc = PsDocument(input_eps_stream)
            
            #Get size of EPS image
            old_size = doc.extract_eps_size()
            
            #Create an output stream for resized EPS
            with open(data_dir + "output_resize_mms.eps", "wb") as output_eps_stream:
                #Save EPS to the output stream with new size assigned in millimeters
                doc.resize_eps(output_eps_stream, aspose.pydrawing.SizeF(196, 123), aspose.page.Units.MILLIMETERS)
        # ExEnd:3
    
    @staticmethod
    def run_percents():
        # ExStart:3
        # The path to the documents directory.
        data_dir = Util.get_data_dir_working_with_eps()
        
        #Create an input stream for EPS file
        with open(data_dir + "input.eps", "rb",) as input_eps_stream:
            #Initialize PsDocument object with input stream
            doc = PsDocument(input_eps_stream)
            
            #Get size of EPS image
            old_size = doc.extract_eps_size()
            
            #Create an output stream for resized EPS
            with open(data_dir + "output_resize_percents.eps", "wb") as output_eps_stream:
                #Save EPS to the output stream with new size assigned in percents
                doc.resize_eps(output_eps_stream, aspose.pydrawing.SizeF(200, 200), aspose.page.Units.PERCENTS)
        # ExEnd:3
