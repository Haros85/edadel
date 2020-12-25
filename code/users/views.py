from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm, EditProfile


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    template_name = "signup.html"

    def form_valid(self, form):
        email = form.cleaned_data['email']
        return super().form_valid(form)


@login_required
def edit_profile(request):
    if request.method == "POST":
        usrform = EditProfile(request.POST or None, instance=request.user)
        if usrform.is_valid():
            user = usrform.save()
            return render(request, "profile_edit_done.html", {
                'form': usrform,
            })
        else:
            return render(request, "profile_edit.html", {
                'form': usrform,
            })
    else:
        usrform = EditProfile(instance=request.user)
        return render(request, "profile_edit.html", {
            'form': usrform,
        })
