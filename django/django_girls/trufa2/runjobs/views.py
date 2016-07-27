from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Job
from .forms import JobForm
import logging

# TODO logger should be better configured
# and the Job submission later on should use
# logger.info() not logger.error()

logger = logging.getLogger(__name__)

def job_form(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.date = timezone.now()
            job.save()
            logger.error('Job submitted: %s' % job)
            return redirect('job_form')
    else:
        form = JobForm()
    return render(request, 'runjobs/run_job.html', {'form': form} )
