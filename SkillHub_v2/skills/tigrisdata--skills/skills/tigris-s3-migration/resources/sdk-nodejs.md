# Node.js / TypeScript — Migrate to Tigris SDK

Replace AWS S3 SDK calls with `@tigrisdata/storage` — simpler API, no bucket/region boilerplate:

```bash
npm install @tigrisdata/storage
```

```typescript
// Before (AWS S3)
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
const s3 = new S3Client({ region: "us-east-1" });
await s3.send(new PutObjectCommand({ Bucket: "my-bucket", Key: "file.jpg", Body: data }));

// After (Tigris SDK) — just set env vars and go
import { put } from "@tigrisdata/storage";
await put("file.jpg", data, { contentType: "image/jpeg" });
```
