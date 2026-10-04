# Laravel Image Optimization with Tigris

## Intervention Image

```bash
composer require intervention/image
```

```php
use Intervention\Image\Laravel\Facades\Image;
use Illuminate\Support\Facades\Storage;

public function uploadWithThumbnail(Request $request)
{
    $file = $request->file('image');
    $name = pathinfo($file->getClientOriginalName(), PATHINFO_FILENAME);

    // Original
    Storage::disk('tigris')->put(
        "images/{$name}.jpg",
        $file->getContent(),
        'public'
    );

    // Thumbnail
    $thumb = Image::read($file)->cover(100, 100)->toJpeg(80);
    Storage::disk('tigris')->put("images/{$name}-thumb.jpg", $thumb, 'public');

    // Medium
    $medium = Image::read($file)->scale(width: 400)->toJpeg(85);
    Storage::disk('tigris')->put("images/{$name}-medium.jpg", $medium, 'public');
}
```
