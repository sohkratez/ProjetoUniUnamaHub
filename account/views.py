from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CreateUserForm

class CreateUserView(FormView):
    template_name = 'registration/user_register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



# Create your views here.
