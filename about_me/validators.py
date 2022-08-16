from django.core.exceptions import ValidationError

def validate_file_size(value, instance):
    """validates file size of uploaded image
    uses instance max_size if specified, defaults to 2MB
    """
    filesize = value.size
    if instance.max_size:
        limit = instance.max_size * 1024 * 1024
    else:
        limit = 2 * 1024 * 1024
    if filesize > limit:
        raise ValidationError(f"The maximum file size that can be uploaded is {limit}")
    else:
        return value
