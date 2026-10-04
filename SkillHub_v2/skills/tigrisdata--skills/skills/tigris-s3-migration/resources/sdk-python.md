# Python — Migrate to tigris-boto3-ext

```bash
pip install tigris-boto3-ext
```

```python
from botocore.client import Config

# Before
s3 = boto3.client("s3")

# After — add endpoint, Tigris credentials, and virtual addressing
s3 = boto3.client(
    "s3",
    endpoint_url="https://t3.storage.dev",
    aws_access_key_id="tid_xxx",
    aws_secret_access_key="tsec_yyy",
    region_name="auto",
    config=Config(s3={"addressing_style": "virtual"}),
)
```
