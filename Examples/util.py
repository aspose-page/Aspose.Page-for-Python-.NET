import os

class Util:
    @staticmethod
    def get_data_dir_getting_started():
        return Util.get_data_dir_data() + "GettingStarted/"

    @staticmethod
    def get_data_dir_working_with_gradient():
        return Util.get_data_dir_data() + "WorkingWithGradient/"

    @staticmethod
    def get_data_dir_working_with_visual_brush():
        return Util.get_data_dir_data() + "WorkingWithVisualBrush/"

    @staticmethod
    def get_data_dir_working_with_images():
        return Util.get_data_dir_data() + "WorkingWithImages/"

    @staticmethod
    def get_data_dir_working_with_textures():
        return Util.get_data_dir_data() + "WorkingWithTextures/"

    @staticmethod
    def get_data_dir_working_with_shapes():
        return Util.get_data_dir_data() + "WorkingWithShapes/"

    @staticmethod
    def get_data_dir_working_with_text():
        return Util.get_data_dir_data() + "WorkingWithText/"

    @staticmethod
    def get_data_dir_working_with_pages():
        return Util.get_data_dir_data() + "WorkingWithPages/"

    @staticmethod
    def get_data_dir_working_with_print_tickets():
        return Util.get_data_dir_data() + "WorkingWithPrintTickets/"

    @staticmethod
    def get_data_dir_working_with_transparency():
        return Util.get_data_dir_data() + "WorkingWithTransparency/"

    @staticmethod
    def get_data_dir_working_with_document():
        return Util.get_data_dir_data() + "WorkingWithDocument/"

    @staticmethod
    def get_data_dir_working_with_document_conversion():
        return Util.get_data_dir_data() + "WorkingWithDocumentConversion/"

    @staticmethod
    def get_data_dir_working_with_document_merging():
        return Util.get_data_dir_data() + "WorkingWithDocumentMerging/"

    @staticmethod
    def get_data_dir_working_with_xmp_metadata_in_eps():
        return Util.get_data_dir_data() + "WorkingWithXMPMetadataInEPS/"

    @staticmethod
    def get_data_dir_working_with_eps():
        return Util.get_data_dir_data() + "WorkingWithEPS/"

    @staticmethod
    def get_data_dir_working_with_cross_package_operations():
        return Util.get_data_dir_data() + "WorkingWithCrossPackageOperations/"

    @staticmethod
    def get_data_dir_working_with_image_conversion():
        return Util.get_data_dir_data() + "WorkingWithImageConversion/"

    @staticmethod
    def get_data_dir_working_with_canvas():
        return Util.get_data_dir_data() + "WorkingWithCanvas/"

    @staticmethod
    def get_data_dir_working_with_hatches():
        return Util.get_data_dir_data() + "WorkingWithHatches/"

    @staticmethod
    def get_data_dir_data():
        start_directory = os.path.abspath(os.getcwd())
        '''start_directory = None
        if parent is not None:
            directory_info = parent.Parent
            if directory_info is not None:
                start_directory = directory_info.FullName
        else:
            start_directory = parent.FullName'''
        return os.path.join(start_directory, "Data\\")