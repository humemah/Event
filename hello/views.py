from multiprocessing import Event
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .forms import EventForm
from .forms import Event
# Create your views here.
def home(request):
    return HttpResponse("HelloWorld")
def display_event(request):
	display_event = Event.objects.all().order_by('date')
	return render(request, 'registration/display_event.html', 
		{'display_event': display_event})

def login_user(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Event')
            else:
                messages.success(request, ("There Was An Error Logging In, Try Again..."))
                return redirect('login')
    else:
	    return render(request, 'registration/login.html', {})

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('login')
	else:
		form = RegisterUserForm()
	return render(request, 'registration/register_user.html', {
		'form':form,})
def add_event(request):
    submitted = False
    form=EventForm
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user.id # logged in user
            event.save()
			#form.save()
            return 	render(request, 'registration/Event.html', {'form':form})
        else:
            form = EventForm
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'registration/Event.html', {'form':form})
def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	return redirect('display_event')

def event_update(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
		return redirect('display_event')
	return render(request, 'registration/event_update.html',
		{'event': event,
		'form':form})

