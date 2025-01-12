from django.shortcuts import render, get_object_or_404
from .models import Message

def message_history(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    history = message.history.all()
    return render(request, 'messaging/message_history.html', {'message': message, 'history': history})
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()  # This will trigger the post_delete signal
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('home')  # Redirect to a home or landing page after deletion
    return render(request, 'confirm_delete.html')  # Render a confirmation page

