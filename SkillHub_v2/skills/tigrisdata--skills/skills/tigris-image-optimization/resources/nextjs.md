# Next.js Image Optimization with Tigris

## next/image with Tigris

```javascript
// next.config.js
module.exports = {
  images: {
    remotePatterns: [{ protocol: "https", hostname: "*.t3.storage.dev" }],
  },
};
```

```tsx
import Image from "next/image";
<Image src={tigrisUrl} alt="Photo" width={800} height={600} />;
```

`next/image` handles responsive sizing and format conversion (WebP/AVIF) automatically.

## Server-Side Processing with Sharp

```typescript
import sharp from "sharp";
import { put } from "@tigrisdata/storage";

async function uploadWithVariants(file: Buffer, basePath: string) {
  const variants = [
    { suffix: "thumb", width: 100, height: 100 },
    { suffix: "medium", width: 400, height: 400 },
  ];

  // Upload original
  await put(`${basePath}.jpg`, file, {
    access: "public",
    contentType: "image/jpeg",
  });

  // Generate and upload variants
  for (const v of variants) {
    const resized = await sharp(file)
      .resize(v.width, v.height, { fit: "cover" })
      .jpeg({ quality: 80 })
      .toBuffer();

    await put(`${basePath}-${v.suffix}.jpg`, resized, {
      access: "public",
      contentType: "image/jpeg",
    });
  }
}
```
