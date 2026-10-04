# Ruby — aws-sdk-s3 with Tigris Endpoint

> **Note:** No native Tigris Ruby SDK exists yet. Use aws-sdk-s3 pointed at Tigris.

```ruby
# Before
s3 = Aws::S3::Client.new(region: "us-east-1")

# After — add endpoint and Tigris credentials
s3 = Aws::S3::Client.new(
  endpoint: "https://t3.storage.dev",
  region: "auto",
  access_key_id: ENV["AWS_ACCESS_KEY_ID"],
  secret_access_key: ENV["AWS_SECRET_ACCESS_KEY"],
)
```
