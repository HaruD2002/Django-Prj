from .models import Request
from .forms import NewRequestForm
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def admin_required(login_url=None):
    return user_passes_test(lambda x: x.is_superuser, login_url=login_url)


class SuperUser(UserPassesTestMixin, LoginRequiredMixin):
    """
    Check user if the user is a superuser or not in CBV
    """

    def test_func(self):
        return self.request.user.is_superuser


class RequestView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = ''
    model = Request
    context_object_name = 'request_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        queryset = super(RequestView, self).get_queryset()
        return queryset.filter(user=self.request.user.id, approval=False)

    def get(self, request, *args, **kwargs):
        user_request = self.get_queryset()
        return render(request, 'request/request.html',
                      {'request_list': user_request})


class CurrentReqView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = ''
    model = Request
    context_object_name = 'current_request'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        queryset = super(CurrentReqView, self).get_queryset()
        return queryset.filter(user=self.request.user.id, approval=True,
                               date_return=None)

    def get(self, request, *args, **kwargs):
        user_request = self.get_queryset()
        return render(request, 'request/my_request.html',
                      {'current_request': user_request})


class PreviousReqView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = ''
    model = Request
    context_object_name = 'previous_request'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        queryset = super(PreviousReqView, self).get_queryset()
        return queryset.filter(user=self.request.user.id)

    def get(self, request, *args, **kwargs):
        user_request = self.get_queryset()
        return render(request, 'request/previous_request.html',
                      {'previous_request': user_request})


class ReqCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = ''
    model = Request
    form_class = NewRequestForm

    def get_success_url(self, **kwargs):
        return reverse('request:my_request_device',
                       kwargs={
                           'username': self.request.user
                       })

    def get(self, request, *args, **kwargself):
        return render(request, 'request/create_request.html',
                      {'form': self.form_class, 'user': self.request.user})

    def form_valid(self, form):
            
        form.instance.user = self.request.user
        if self.request.user.is_superuser:
            form.instance.approval = 1
            form.instance.approval_admin = self.request.user
        form.instance = form.save()
        messages.success(self.request, "your request has been send")
        return super(ReqCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "some thing went wrong")
        return self.get_success_url()


class AdminReqView(SuperUser, ListView):
    model = Request
    login_url = '/login'
    redirect_field_name = ''
    context_object_name = 'request_list_all'

    def get_success_url(self):
        return reverse('request:view_request_list')

    def get_queryset(self):
        queryset = super(AdminReqView, self).get_queryset()
        return queryset.filter(approval=False)


class DeleteRequest(LoginRequiredMixin, DeleteView):
    model = Request
    login_url = '/login/'
    redirect_field_name = ''
    model = Request

    def get_success_url(self, **kwargs):
        messages.error(self.request, '''your request
                       has been deleted ''')
        return reverse('request:my_request_device', kwargs={
            'username': self.request.user})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class UpdateRequest(LoginRequiredMixin, UpdateView):
    model = Request
    login_url = '/login/'
    redirect_field_name = ''
    model = Request
    form_class = NewRequestForm

    def get_success_url(self):
        messages.success(self.request, '''request have been
                         updated successfully''')
        return reverse('request:my_request_device',
                       kwargs={
                           'username': self.request.user
                       })

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)


@admin_required(login_url='/profile}')
@login_required(login_url="/login")
def RejectView(request, request_id):
    this_request = Request.objects.get(id=request_id)
    this_request.approval = -1
    this_request.save()
    print(Request.objects.get(id=this_request.id).approval)
    messages.SUCCESS(request, 'you have accepted the request')
    return HttpResponseRedirect(reverse('request:view_request_list'))

@admin_required(login_url='/profile}')
@login_required(login_url="/login")
def AcceptedView(request, request_id):
    this_request = Request.objects.get(id=request_id)
    this_request.approval_admin = request.user
    this_request.approval = True
    this_request.save()
    messages.success(request, 'you have accepted the request')
    return HttpResponseRedirect(reverse('request:view_request_list'))



@login_required(login_url="/login")
def ReturnView(request, request_id):
    this_request = Request.objects.get(id=request_id)
    this_request.date_return = timezone.now()
    this_request.save()
    messages.success(request, 'you have accepted the request')
    return HttpResponseRedirect(reverse('request:current_request',
                                        kwargs={'username': request.user}))