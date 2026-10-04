# Express Image Optimization with Tigris

## Sharp Middleware

```typescript
import sharp from "sharp";
import multer from "multer";
import { put } from "@tigrisdata/storage";

const upload = multer({ storage: multer.memoryStorage() });

app.post("/upload-image", upload.single("image"), async (req, res) => {
  const file = req.file!;
  const base = `images/${Date.now()}`;

  // Process variants in parallel
  const [thumb, medium] = await Promise.all([
    sharp(file.buffer).resize(100, 100, { fit: "cover" }).jpeg({ quality: 80 }).toBuffer(),
    sharp(file.buffer).resize(400, 400, { fit: "inside" }).jpeg({ quality: 85 }).toBuffer(),
  ]);

  await Promise.all([
    put(`${base}.jpg`, file.buffer, { access: "public", contentType: "image/jpeg" }),
    put(`${base}-thumb.jpg`, thumb, { access: "public", contentType: "image/jpeg" }),
    put(`${base}-medium.jpg`, medium, { access: "public", contentType: "image/jpeg" }),
  ]);

  res.json({ original: `${base}.jpg`, thumb: `${base}-thumb.jpg` });
});
```
