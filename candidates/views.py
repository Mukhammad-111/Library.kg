from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views import generic
from . import models, forms


class RegisterView(generic.CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'candidates/register.html'

    def get_success_url(self):
        return reverse('applicants:login')


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'candidates/login.html'

    def get_success_url(self):
        return reverse('applicants:applicant_list')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('applicants:login')


class ApplicantListView(generic.ListView):
    template_name = 'candidates/applicant_list.html'
    context_object_name = 'applicant'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')