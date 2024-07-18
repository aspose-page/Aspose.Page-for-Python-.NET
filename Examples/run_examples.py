import sys
from GettingStarted.load_license_from_file import *
from GettingStarted.load_license_from_stream_object import *
from WorkingWithGradient.add_horizontal_gradient_ps import *
from WorkingWithGradient.add_horizontal_gradient_xps import *
from WorkingWithGradient.add_vertical_gradient_ps import *
from WorkingWithGradient.add_vertical_gradient_xps import *
from WorkingWithGradient.add_diagonal_gradient_ps import *
from WorkingWithGradient.add_diagonal_gradient_xps import *
from WorkingWithGradient.add_radial_gradient_1ps import *
from WorkingWithGradient.add_radial_gradient_2ps import *
from WorkingWithImages.add_image_ps import *
from WorkingWithImages.add_image_xps import *
from WorkingWithImages.add_tiled_image_xps import *
from WorkingWithShapes.add_rectangle_ps import *
from WorkingWithShapes.add_rectangle_xps import *
from WorkingWithShapes.add_ellipse_ps import *
from WorkingWithShapes.add_ellipse_xps import *
from WorkingWithShapes.apply_different_color_spaces_xps import *
from WorkingWithText.add_text_ps import *
from WorkingWithText.add_text_xps import *
from WorkingWithText.add_text_using_unicode_string_ps import *
from WorkingWithText.add_text_using_unicode_string_xps import *
from WorkingWithPages.add_page_1ps import *
from WorkingWithPages.add_page_2ps import *
from WorkingWithPages.add_page_xps import *
from WorkingWithPages.remove_page_xps import *
from WorkingWithTransparency.add_transparent_image_ps import *
from WorkingWithTransparency.add_transparent_object_xps import *
from WorkingWithTransparency.show_pseudo_transparency_ps import *
from WorkingWithTransparency.set_opacity_mask_xps import *
from WorkingWithVisualBrush.add_grid import *
from WorkingWithTexture.add_texture_tiling_pattern_ps import *
from  WorkingWithHatches.add_hatch_pattern_ps import *
from WorkingWithDocument.create_document_ps import *
from WorkingWithDocument.create_document_xps import *
from WorkingWithDocument.change_document_xps import *
from WorkingWithDocumentConversion.post_script_to_image import *
from WorkingWithDocumentConversion.post_script_to_pdf import *
from WorkingWithDocumentConversion.xps_to_bmp import *
from WorkingWithDocumentConversion.xps_to_jpeg import *
from WorkingWithDocumentConversion.xps_to_pdf import *
from WorkingWithDocumentConversion.xps_to_png import *
from WorkingWithDocumentConversion.xps_to_tiff import *
from WorkingWithDocumentMerging.post_script_to_pdf import *
from WorkingWithDocumentMerging.xps_to_pdf import *
from WorkingWithDocumentMerging.xps_to_xps import *
from WorkingWithPrintTickets.get_print_tickets import *
from WorkingWithPrintTickets.edit_print_ticket import *
from WorkingWithPrintTickets.link_print_tickets import *
from WorkingWithPrintTickets.create_custom_print_ticket import *
from WorkingWithCrossPackageOperations.add_image_filled_glyph_and_foreign_image import *
from WorkingWithCrossPackageOperations.manipulate_pages import *
from WorkingWithCrossPackageOperations.add_glyph_clone_and_change_color import *
from WorkingWithImageConversion.save_image_as_eps import *
from WorkingWithCanvas.clipping_ps import *
from WorkingWithCanvas.clipping_xps import *
from WorkingWithCanvas.transformations_ps import *
from WorkingWithCanvas.transformations_xps import *
from WorkingWithEPS.resize_eps import *
from WorkingWithEPS.crop_eps import *
from WorkingWithXMPMetadataInEPS.add_metadata import *
from WorkingWithXMPMetadataInEPS.change_metadata_add_array_items import *
from WorkingWithXMPMetadataInEPS.change_metadata_add_named_value_item import *
from WorkingWithXMPMetadataInEPS.change_metadata_add_namespace import *
from WorkingWithXMPMetadataInEPS.change_metadata_add_simple_properties import *
from WorkingWithXMPMetadataInEPS.change_metadata_change_array_items import *
from WorkingWithXMPMetadataInEPS.change_metadata_change_named_value_item import *
from WorkingWithXMPMetadataInEPS.change_metadata_change_values import *
from WorkingWithXMPMetadataInEPS.get_metadata import *
#from GettingStarted.load_license_from_file import LoadLicenseFromFile
import os

#class RunExamples:

    #@staticmethod
def main():
    print("Open RunExamples.cs. \nIn Main() method uncomment the example that you want to run.")
    print("=====================================================")
    # Uncomment the one you want to try out

    # =====================================================
    # =====================================================
    # Getting Started
    # =====================================================
    # =====================================================
    LoadLicenseFromFile.run()
    # ApplyMeteredLicense.run();
    # LoadLicenseFromStreamObject.run();
    # SetLicenseUsingEmbeddedResource.run();
    # SecureLicense.run();

    # =====================================================
    # =====================================================
    # WorkingWithDocument
    # =====================================================
    # =====================================================
    CreateDocumentXPS.run();
    ChangeDocumentXPS.run();
    CreateDocumentPS.run();

    # =====================================================
    # =====================================================
    # WorkingWithDocumentConversion
    # =====================================================
    # =====================================================
    PostScriptToPdf.run();
    PostScriptToImage.run();
    XPStoPNG.run();
    XPStoBMP.run()
    XPStoJPEG.run();
    XPStoTIFF.run();
    XPStoPDF.run();

    # =====================================================
    # =====================================================
    # WorkingWithDocumentMerging
    # =====================================================
    # =====================================================
    MergePostScriptToPdf.run();
    MergeXPStoPDF.run();
    MergeXPStoXPS.run();

    # =====================================================
    # =====================================================
    # WorkingWithXMPMetadataInEPS
    # =====================================================
    # =====================================================
    GetMetadata.run(); #partially doesn't work (code commented) due to Dictionaries are not supported by Cs2PythonWrapper now
    AddMetadata.run();
    ChangeMetadata_ChangeValues.run();
    ChangeMetadata_AddSimpleProperties.run();
    ChangeMetadata_AddArrayItems.run();
    ChangeMetadata_ChangeArrayItems.run();
    ChangeMetadata_AddNamedValueItem.run();
    ChangeMetadata_ChangeNamedValueItem.run();
    ChangeMetadata_AddNamespace.run();

    # =====================================================
    # =====================================================
    # WorkingWithText
    # =====================================================
    # =====================================================
    AddTextXPS.run();
    AddTextUsingUnicodeStringXPS.run();
    AddTextPS.run();
    AddTextUsingUnicodeStringPS.run();

    # =====================================================
    # =====================================================
    # WorkingWithImages
    # =====================================================
    # =====================================================
    AddImageXPS.run();
    AddTiledImageXPS.run();
    AddImagePS.run();

    # =====================================================
    # =====================================================
    # WorkingWithTextures
    # =====================================================
    # =====================================================
    AddTextureTilingPatternPS.run();

    # =====================================================
    # =====================================================
    # WorkingWithHatchPattern
    # =====================================================
    # =====================================================
    AddHatchPatternPS.run();

    # =====================================================
    # =====================================================
    # WorkingWithGradient
    # =====================================================
    # =====================================================
    AddDiagonalGradientXPS.run();
    AddVerticalGradientXPS.run();
    AddHorizontalGradientXPS.run();
    AddHorizontalGradientPS.run();
    AddVerticalGradientPS.run();
    AddDiagonalGradientPS.run();
    AddRadialGradient1PS.run();
    AddRadialGradient2PS.run();

    # =====================================================
    # =====================================================
    # WorkingWithShapes
    # =====================================================
    # =====================================================
    AddRectangleXPS.run();
    AddEllipseXPS.run();
    ApplyDifferentColorSpacesXPS.run();
    AddEllipsePS.run();
    AddRectanglePS.run();

    # =====================================================
    # =====================================================
    # WorkingWithPages
    # =====================================================
    # =====================================================
    AddPageXPS.run();
    RemovePageXPS.run();
    AddPage1PS.run();
    AddPage2PS.run();

    # =====================================================
    # =====================================================
    # WorkingWithPrintTickets
    # =====================================================
    # =====================================================
    GetPrintTickets.run();
    LinkPrintTickets.run();
    #CreateCustomPrintTicket.run();
    EditPrintTicket.run();

    # =====================================================
    # =====================================================
    # WorkingWithTransparency
    # =====================================================
    # =====================================================
    AddTransparentObjectXPS.run();
    SetOpacityMaskXPS.run();
    ShowPseudoTransparencyPS.run();
    AddTransparentImagePS.run();

    # =====================================================
    # =====================================================
    #WorkingWithVisualBrush
    # =====================================================
    # =====================================================
    AddGrid.run();

    # =====================================================
    # =====================================================
    #WorkingWithCrossPackageOperations
    # =====================================================
    # =====================================================
    AddImageFilledGlyphAndForeignImage.run();
    AddGlyphCloneAndChangeColor.run();
    ManipulatePages.run();

    # =====================================================
    # =====================================================
    #WorkingWithImageConversion
    # =====================================================
    # =====================================================
    SaveImageAsEPS.run(); # fix in .NET

    # =====================================================
    # =====================================================
    #ResizeEPS
    # =====================================================
    # =====================================================
    ResizeEPS.run_points();
    ResizeEPS.run_inches();
    ResizeEPS.run_mms();
    ResizeEPS.run_percents();
    CropEPS.run()

    # =====================================================
    # =====================================================
    #WorkingWithCanvas
    # =====================================================
    # =====================================================
    TransformationsXPS.run();
    ClippingXPS.run();
    TransformationsPS.run();
    ClippingPS.run();

    # Stop before exiting
    print("\n\nProgram Finished.")
    #sys.stdin.read(1)
    
if __name__ == '__main__':
    main()
