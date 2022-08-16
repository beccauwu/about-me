from client_side_image_cropping import ClientsideCroppingWidget

class CustomCropWidget(ClientsideCroppingWidget):
    template_name = 'croptemplate.html'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
