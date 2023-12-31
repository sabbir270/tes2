from django.shortcuts import render,redirect

from .forms import GroupForm

def AddPlayer(request):
    if request.method=='POST':
        form=GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_player')        
    else:
        form = GroupForm()
    return render(request, 'myapp/add_player.html', {'form': form})

