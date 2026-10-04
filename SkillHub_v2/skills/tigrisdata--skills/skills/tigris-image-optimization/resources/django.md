# Django Image Optimization with Tigris

## django-imagekit

```bash
pip install django-imagekit
```

```python
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

class Photo(models.Model):
    original = models.ImageField(upload_to="photos/")
    thumbnail = ImageSpecField(
        source="original",
        processors=[ResizeToFill(100, 100)],
        format="JPEG",
        options={"quality": 80},
    )
    medium = ImageSpecField(
        source="original",
        processors=[ResizeToFit(400, 400)],
        format="JPEG",
        options={"quality": 85},
    )
```

```html
<img src="{{ photo.thumbnail.url }}" alt="Thumbnail" />
<img src="{{ photo.medium.url }}" alt="Medium" />
```

## Manual Processing with Pillow

```python
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def create_thumbnail(image_field, size=(100, 100)):
    img = Image.open(image_field)
    img.thumbnail(size, Image.LANCZOS)
    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=80)
    return ContentFile(buffer.getvalue())
```
