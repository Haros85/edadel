from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import CreationForm, EditProfile


class SignUp(CreateView):
    form_class = CreationForm
    success_url = '/auth/login/'
    template_name = 'signup.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, user)
            return redirect('index')
        return render(request, 'signup.html', {'form': form})

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
