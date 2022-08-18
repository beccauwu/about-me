from client_side_image_cropping import ClientsideCroppingWidget
from django_addanother.widgets import BaseRelatedWidgetWrapper

class CustomCropWidget(ClientsideCroppingWidget):
    template_name = 'croptemplate.html'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CustomAddAnotherWidgetWrapper(BaseRelatedWidgetWrapper):
    template = 'addanothertemplate.html'
    def __init__(self, widget, add_related_url, add_icon=None):
        super(CustomAddAnotherWidgetWrapper, self).__init__(widget, add_related_url, None, add_icon, None)
