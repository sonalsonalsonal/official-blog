from pelican import signals

def validate_absolute_urls(article_generator, metadata):
    article_image = metadata.get('image', None)
    site_url = article_generator.settings.get("SITEURL", "")
    if article_image is not None and article_image.startswith("/"):
        metadata.__setitem__("image", "{0}{1}".format(site_url, article_image))

def register():
    signals.article_generator_context.connect(validate_absolute_urls)
