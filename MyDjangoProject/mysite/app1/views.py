from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'app1/feedback_form.html', {'form': form})

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-submitted_at')
    return render(request, 'app1/feedback_list.html', {'feedbacks':
feedbacks})