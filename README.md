# XPS & Postscript File Manipulation Python API

[Aspose.Page for Python via .NET](https://products.aspose.com/page/python-net) is an on premise Python API that allows you to add XPS manipulation features to your own applications. The API also supports to convert XPS, EPS & PS documents to other formats.

<p align="center">

  <a title="Download complete Aspose.Page for Python source code" href="https://github.com/aspose-page/Aspose.Page-for-Python-.NET/archive/master.zip">
	<img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" />
  </a>
</p>

Directory | Description
--------- | -----------
[Demos](Demos)  | Source code for live demos hosted at https://products.aspose.app/page/family.
[Examples](Examples)  | A collection of Python examples that help you learn the product features.

## XPS, EPS & PS Processing Features

- Creation & edition of documents via API.
- Manipulation with pages.
- Manipulation with graphics objects and graphics states.
- Support for various types of painting and colorspaces.
- Manipulation with print tickets in XPS documents.
- Support for cross-package operations in XPS document.
- Convert XPS, PS & EPS documents to other popular formats.
- Merge documents to PDF.
- Resize and crop EPS files.
- Convert raster images to EPS files.
- Conversion of XPS, PS & EPS documents to other popular formats.
- Supports PostScript language levels 1-3 with an exception of font types: Type2 (CFF), Type14 (Chameleon), Types 9, 10, 11).
- Supports XPS and OXPS formats in the latest versions.

## Read & Write XPS Format

**Fixed Layout:** XPS

## Save XPS, PS & EPS Documents As

**Fixed Layout:** PDF\
**Images:** PNG, JPEG, TIFF, BMP

## Save PS & EPS Documents As

**Metafiles:** EMF, WMF\

## Platform Independence

Aspose.Page for Python can be integrated with 32-bit and 64-bit Python web or console applications fro Windows where Python 3.6 or later is installed. Packages for Linux and MacOS will be released in the nearest future.

## Get Started with Aspose.Page for Python

Run ```pip install aspose-page``` to fetch the package. If you already have **Aspose.Page for Python** and want to get the latest version, please run ```pip install --upgrade aspose-page```.

### Create a PostScript file from scratch in Python

In the next code snippet, we are creating a PS document from scratch containing the text “Hello from Aspose!”. After installing **Aspose.Page for Python** in your environment, you can execute below code sample to see how Aspose.Page API works.

Below code snippet follows these steps:

1. Instantiate a `PsSaveOptions` object.
1. Create PostScript file output stream.
1. Instantiate a `PsDocument` object.
1. Create `aspose.pydrawing.Font` using `aspose.page.ExternalFontCache`.
1. Fill text with solid brush.
1. Save the resultant PostScript file.

The following code snippet is a "Hello, World!" program to show main technique of **Aspose.Page for Python** in PS files:

```python
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing *

#Create save options
options = PsSaveOptions()
#Create output stream for PS document
out_ps_stream = open(dir + "document.ps", "wb")
#Create PS document
document = PsDocument(out_ps_stream, options, false)
#Create aspose.pydrawing.Font
font = aspose.page.ExternalFontCache.create_font_by_family_name("Times New Roman", font_size, aspose.pydrawing.FontStyle.BOLD)
# Add text fragment to new page at point (50, 150)
document.fill_text("Hello from Aspose!", font, 50, 150, aspose.pydrawing.SolidBrush(aspose.pydrawing.Color.blue))
#Close current page
document.close_page()

#Save the document
document.save()
```

### Create an XPS file from scratch in Python

In the next code snippet, we are creating an empty XPS document containing the text ?Hello from Aspose!?.

Below code snippet follows these steps:

1. Instantiate a `XpsDocument` object.
1. Create 'XpsGlyphs` object with using the insatnce of `XpsDocument`.
1. Set painting for the glyphs object.
1. Create `aspose.pydrawing.Font` using `aspose.page.ExternalFontCache`.
1. Save the resultant XPS document.

The following code snippet is a "Hello, World!" program to show main technique of **Aspose.Page for Python** in PS files:

```python
from aspose.page.xps import *
import aspose.pydrawing *
#Create new XPS Document
x_docs = XpsDocument()

#Add glyph to the document
glyphs = x_docs.add_glyphs("Arial", 12, aspose.pydrawing.FontStyle.REGULAR, 300, 450, "Hello World!")
#Set painting for glyphs
glyphs.fill = x_docs.create_solid_color_brush(aspose.pydrawing.Color.black)
#Save result
x_docs.save(dir + "output.xps")
```

### Example of converting EPS to JPEG

**Aspose.Page for Python** is a PS/EPS and XPS manipulation API that lets you convert any existing EPS file to JPEG or other raster image formats.

Below code snippet follows these steps:

1. Create EPS file input stream.
1. Initialize `PsDocument` object.
1. Create `ImageSaveOptions` object.
1. Initialize `ImageDevice` object with JPEG `aspose.pydrawing.imaging.ImageFormat`.
1. Save the document.

```python
import os
import aspose
from aspose.page.eps import *
from aspose.page.eps.device import *
import aspose.pydrawing.imaging *

#Initialize EPS input stream
eps_stream = open(data_dir + "input.eps", "rb")
#Create PsDocument
document = PsDocument(ps_stream)
#If you want to convert Postscript file despite of minor errors set this flag
suppress_errors = True
#Initialize options object with necessary parameters.
options = ImageSaveOptions(suppress_errors)
#Default image format is PNG and it is not mandatory to set it in ImageDevice
#Default image size is 595x842 and it is not mandatory to set it in ImageDevice
device = ImageDevice(aspose.pydrawing.imaging.ImageFormat.jpeg)
#Save document to JPEG image
document.save(device, options)
```

### Example of converting XPS to PDF

**Aspose.Page for Python** supports the feature to convert XPS documents to PDF format. To accomplish this requirement, the PdfSaveOptions class has been introduced into the aspose.page.xps.presentation.pdf namespace. Instantiate an object of PdfSaveOptions and pass it as a second argument to the XpsDocument.save(..) method.

Below code snippet follows these steps:

1. Create a PDF file output stream.
1. Create an XPS document input stream.
1. Instantiate `XpsDocument` class with the XPS input stream.
1. Create `PdfSaveOptions` object with needed settings.
1. Initialize `PdfDevice` with PDF ouputStream
1. Call the `XpsDocument.save()` method and pass it PdfDevice and PdfSaveOptions objects convert the XPS document to PDF.

```python
from aspose.page.xps import *
from aspose.page.xps.presentation.pdf import *

#Initialize PDF output stream
pdf_stream = open(data_dir + "XPStoPDF_out.pdf", "wb")
#Initialize XPS input stream
xps_stream = open(data_dir + "input.xps", "rb")
#Load XPS document form the stream
document = XpsDocument(xps_stream, XpsLoadOptions())
#or load XPS document directly from file. No xpsStream is needed then.
#XpsDocument document = new XpsDocument(inputFileName, new XpsLoadOptions());
#Initialize options object with necessary parameters.
options = PdfSaveOptions()                
options.jpeg_quality_level = 100
options.image_compression = PdfImageCompression.JPEG
options.text_compression = PdfTextCompression.FLATE
options.page_numbers = [ 1, 2, 6 ]
#Create rendering device for PDF format
device = PdfDevice(pdf_stream)
#Save XPS document as PDF
document.save(device, options)
```

### Merge XPS Files

Merge multiple XPS into single file in Python with Aspose.Page programmatically. XPS files are merged such that the first one is joined at the end of the other document.

Below code snippet follows these steps:

1. Create a XPS file output stream.
1. Create the first XPS document input stream.
1. Instantiate `XpsDocument` class with the XPS input stream.
1. Call the `XpsDocument.merge()` method and pass it files to merge and the output XPS stream.

```python
from aspose.page.xps import *

#Initialize XPS output stream
out_stream = data_dir + "mergedXPSfiles.xps", "wb")
#Initialize XPS input stream
out_stream = open(data_dir + "input.xps", "rb")
#Load XPS document from the stream
document = XpsDocument(in_stream, XpsLoadOptions())
#or load XPS document directly from file. No xpsStream is needed then.
#XpsDocument document = new XpsDocument(inputFileName, new XpsLoadOptions());
#Create an array of XPS files that will be merged with the first one
files_to_merge = [ data_dir + "Demo.xps", data_dir + "sample.xps" ]
# Merge XPS files to output PDF document
document.merge(files_to_merge, out_stream)
```

### Crop EPS image

Crop EPS image without using specialized software. EPS file doesn't loss initial content. It just have bounding box changed.

Below code snippet follows these steps:

1. Create EPS file input stream.
1. Initialize `PsDocument` object.
1. Create output EPS stream.
1. Call `PsDocument.crop_eps()` method and pass it the output stream and new bounding box, defined by for numbers.

```python
from aspose.page.eps import *

#Create an input stream for EPS file
input_eps_stream = open(data_dir + "input.eps", "rb")
#Initialize PsDocument object with input stream
doc = PsDocument(input_eps_stream)
#If someone whants to know initial bounding box, get initial bounding box of EPS image
#initial_bounding_box = doc.extract_eps_bounding_box()
#Create an output stream for resized EPS
input_eps_stream = open(data_dir + "output_crop.eps", "wb")
#Create new bounding box
#Bounding box is represented by 4 numbers: x0, y0, x, y, where x0 - left margin, y0 - top margin, x - (x0 + width), y - (y0 + height)
new_bounding_box = [ 260, 300, 480, 432 ]
#Crop EPS image and save it to the output stream.
doc.crop_eps(output_eps_stream, new_bounding_box)
```

[Home](https://www.aspose.com/) | [Product Page](https://products.aspose.com/page/python-net) | [Docs](https://docs.aspose.com/page/python-net/) | [Demos](https://products.aspose.app/page/family) | [API Reference](https://apireference.aspose.com/page/python-net) | [Examples](https://github.com/aspose-page/Aspose.Page-for-Python-.NET) | [Blog](https://blog.aspose.com/category/page/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/page) |  [Temporary License](https://purchase.aspose.com/temporary-license)

