from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class PredictView(TemplateView):
    template_name = "predict.html"