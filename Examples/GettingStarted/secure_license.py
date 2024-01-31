'''from ionic.zip import *
import io

class SecureLicense:
    @staticmethod
    def run():
        # ExStart:1
        with type(SecureLicense()).Assembly.GetManifestResourceStream("Aspose.Total.NET.lic.zip") as zip:
            with ZipFile.Read(zip) as zf:
                ms = io.BytesIO()
                e = zf["Aspose.Total.NET.lic"]
                e.ExtractWithPassword(ms, "test")
                ms.Position = 0
        # ExEnd:1
'''