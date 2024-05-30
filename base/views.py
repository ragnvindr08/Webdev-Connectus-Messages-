from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from .models import Message
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib import messages  # For flash messages



@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None) 
        if form.is_valid():
            form.save()
    else: 
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
  
def send_message(request):
    if request.method == 'POST':
        # Process the form submission
        # Assuming you have a form for sending messages
        pass
    else:
        # Render the form for sending messages
        return render(request, 'send_message.html')
def send_message(request):
    # Your logic for sending messages goes here
    return render(request, 'send_message.html')

def community(request):
    return render(request, 'community.html')

@login_required    #messanges functions :)
def messages_view(request):
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver')
        content = request.POST.get('content')

        try:
            receiver = User.objects.get(username=receiver_username) 
            message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, 'Message sent successfully!')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'messages.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern
        except User.DoesNotExist:
            messages.error(request, 'Invalid username. Please enter a valid user.')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'messages.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern
        except Exception as e:
            messages.error(request, f'Error sending message: {e}')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'messages.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern 
    else:
        received_messages = Message.objects.filter(receiver=request.user)
        return render(request, 'messages.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern
    
def messages_home(request):
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver')
        content = request.POST.get('content')

        try:
            receiver = User.objects.get(username=receiver_username) 
            message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
            messages.success(request, 'Message sent successfully!')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'home.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern
        except User.DoesNotExist:
            messages.error(request, 'Invalid username. Please enter a valid user.')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'home.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern
        except Exception as e:
            messages.error(request, f'Error sending message: {e}')
            received_messages = Message.objects.filter(receiver=request.user)
            return render(request, 'home.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern 
    else:
        received_messages = Message.objects.filter(receiver=request.user)
        return render(request, 'homemessage.html', {'received_messages': received_messages}) # Assuming 'messages' is the correct name of the URL pattern