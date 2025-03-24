from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import DocumentForm
from .models import Docs

class FileUploadView(FormView):
    template_name = 'filemanager/upload.html'
    form_class = DocumentForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FileListView(ListView):
    model = Docs
    template_name = 'filemanager/file_list.html'
    context_object_name = 'files'