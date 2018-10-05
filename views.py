from django.shortcuts import render
from .forms import PostForm
from .models import Estudiante

def post_list(request):
	posts= Estudiante.objects.filter(nombre='Angel')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            # post.nombre = request.user
            form.save()
            #Prueguntar porque redirect no esta definida
            #return redirect('bolg/post_list.html')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, matricula_id):
	matri = Estudiante.objects.get(matricula=matricula_id)
	if request.method == "GET":
		form = PostForm(instance=matri)
	else:
		form = PostForm(request.POST, instance=matri)
		if form.is_valid():
			form.save()
		#return redirect('bolg/post_list.html')
	return render(request, 'blog/post_edit.html', {'form': form})