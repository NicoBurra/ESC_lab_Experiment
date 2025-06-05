from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Experiment, Participation
from .forms import ExperimentForm


def home(request):
    experiments = Experiment.objects.all()
    return render(request, 'experiments/home.html', {'experiments': experiments})


@login_required
def experiment_detail(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk)
    return render(request, 'experiments/detail.html', {'experiment': experiment})


@login_required
def create_experiment(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExperimentForm()
    return render(request, 'experiments/form.html', {'form': form})


@login_required
def accept_experiment(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk)
    Participation.objects.get_or_create(student=request.user.student, experiment=experiment, status='accepted')
    return redirect('home')
