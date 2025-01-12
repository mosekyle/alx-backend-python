from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def message_history(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    history = message.history.all()
    return render(request, 'messaging/message_history.html', {'message': message, 'history': history})


@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()  # This will trigger the post_delete signal
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('home')  # Redirect to a home or landing page after deletion
    return render(request, 'confirm_delete.html')  # Render a confirmation page
def threaded_conversation_view(request, message_id):
    root_message = Message.objects.prefetch_related('replies').select_related('sender', 'receiver').get(id=message_id)
    thread = root_message.get_thread()
    return render(request, 'threaded_conversation.html', {'thread': thread})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from messaging.models import Message
from messaging.forms import MessageForm

@login_required
def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Automatically set the sender to the logged-in user
            message.save()
            return redirect('inbox')  # Redirect to inbox or another appropriate page
    else:
        form = MessageForm()
    return render(request, 'create_message.html', {'form': form})
@login_required
def inbox_view(request):
    messages = Message.objects.filter(receiver=request.user).select_related('sender', 'receiver')
    return render(request, 'inbox.html', {'messages': messages})

