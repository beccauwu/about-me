from client_side_image_cropping import ClientsideCroppingWidget
from django_addanother.widgets import AddAnotherWidgetWrapper

class CustomCropWidget(ClientsideCroppingWidget):
    template_name = 'croptemplate.html'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CustomAddAnotherWidgetWrapper(AddAnotherWidgetWrapper):
    template_name = 'addanothertemplate.html'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
