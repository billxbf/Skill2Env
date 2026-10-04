# PHP — aws-sdk-php with Tigris Endpoint

> **Note:** No native Tigris PHP SDK exists yet. Use aws-sdk-php pointed at Tigris.

```php
// Before
$s3 = new S3Client(['region' => 'us-east-1', 'version' => 'latest']);

// After — add endpoint and Tigris credentials
$s3 = new S3Client([
    'endpoint' => 'https://t3.storage.dev',
    'region' => 'auto',
    'version' => 'latest',
    'use_path_style_endpoint' => true,
    'credentials' => [
        'key' => env('AWS_ACCESS_KEY_ID'),
        'secret' => env('AWS_SECRET_ACCESS_KEY'),
    ],
]);
```
