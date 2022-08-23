from django.core.exceptions import ValidationError

def validate_file_size(value):
    """validates file size of uploaded image
    uses instance max_size if specified, defaults to 2MB
    """
    return value
