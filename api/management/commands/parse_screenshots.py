from django.core.management.base import BaseCommand, CommandError
from django.db import models
from api.models import BasePath
from api.models import ScreenshotParse

from pathlib import Path
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
try:
    from PIL import UnidentifiedImageError
except ImportError:
    import UnidentifiedImageError


class Command(BaseCommand):
    help = 'Delete Old and Parse New Screenshots'

    def add_arguments(self, parser):
       parser.add_argument('--path', type=str, required=False, help='Base path')
    

    def crawl_path(self, p):
        for screenshot_path in p.iterdir():
            if screenshot_path.is_dir():
                self.crawl_path(screenshot_path)
            else:
                abs_path = screenshot_path.absolute()
                try:
                    txt = str(pytesseract.image_to_string(Image.open(abs_path), timeout=10))
                    self.path_to_text_maps.append({"path":str(abs_path),"text":txt})
                except UnidentifiedImageError as pil_e:
                    print(f"Cannot parse: {str(abs_path)} {str(pil_e)}")
                except Exception as e:
                    print(e)
                

    def handle(self, *args, **options):
        if options['path']:
            path = Path(options['path'])
            BasePath.objects.create(path=path)
        else:
            path = Path(BasePath.load().path)
        assert path.exists() == True, f"Path {path} does not exist"

        print(f"parsing from: {path}")

        ScreenshotParse.objects.all().delete()
        self.path_to_text_maps = []
        self.crawl_path(Path(path))
        screenshot_obj_list = [ScreenshotParse(**d) for d in self.path_to_text_maps]
        ScreenshotParse.objects.bulk_create(screenshot_obj_list)

        print(f"Done Parsing: {ScreenshotParse.objects.count()}")

