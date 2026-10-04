# Remix Image Optimization with Tigris

## Sharp in Action Functions

```typescript
import sharp from "sharp";
import { put } from "@tigrisdata/storage";

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const file = formData.get("image") as File;
  const buffer = Buffer.from(await file.arrayBuffer());

  // Generate thumbnail
  const thumb = await sharp(buffer)
    .resize(200, 200, { fit: "cover" })
    .webp({ quality: 80 })
    .toBuffer();

  await Promise.all([
    put(`images/${Date.now()}.jpg`, buffer, { access: "public", contentType: file.type }),
    put(`images/${Date.now()}-thumb.webp`, thumb, { access: "public", contentType: "image/webp" }),
  ]);

  return json({ success: true });
}
```

## Responsive srcset

```html
<img
  src={thumbUrl}
  srcset={`${thumbUrl} 200w, ${mediumUrl} 400w, ${fullUrl} 800w`}
  sizes="(max-width: 400px) 200px, (max-width: 800px) 400px, 800px"
  alt="Photo"
/>
```
