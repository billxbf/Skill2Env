# Rails Image Optimization with Tigris

## Active Storage Variants

```ruby
# Gemfile
gem "image_processing", "~> 1.2"
```

```erb
<%# Thumbnail %>
<%= image_tag user.avatar.variant(resize_to_fill: [100, 100]) %>

<%# Medium size %>
<%= image_tag user.avatar.variant(resize_to_limit: [400, 400]) %>

<%# WebP conversion %>
<%= image_tag user.avatar.variant(format: :webp, resize_to_limit: [800, 800]) %>
```

Variants are processed on first request and cached. For eager processing:

```ruby
user.avatar.variant(resize_to_fill: [100, 100]).processed
```
