# Go — Migrate to Tigris SDK

```bash
go get github.com/tigrisdata/storage-go
```

```go
// Before (AWS S3)
cfg, _ := config.LoadDefaultConfig(ctx)
client := s3.NewFromConfig(cfg)
client.PutObject(ctx, &s3.PutObjectInput{Bucket: &bucket, Key: &key, Body: reader})

// After (Tigris SDK)
import "github.com/tigrisdata/storage-go/simplestorage"
client, _ := simplestorage.New(ctx)
client.PutObject(ctx, "my-bucket", "file.jpg", reader)
```

The Go SDK also provides Tigris-specific features (snapshots, forks, renaming) not available through the AWS SDK.
