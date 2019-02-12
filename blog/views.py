from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import posts
from .forms import CreatePost
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView ,CreateView,UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin

post = [

		{
			'author' : 'shailesh',
			'title' : 'blog 1',
			'content' : 'learning django',
			'date_posted' : '29 Dec 2018'
		},

		{
			'author' : 'shailesh',
			'title' : 'blog 2',
			'content' : 'building django project',
			'date_posted' : '01 Dec 2018'
		}
]

# Create your views here.
@login_required
def home(request):
	if request.method == 'POST':
		form = CreatePost(request.POST)
		if(form.is_valid()):
			title = form.cleaned_data.get('title')
			content = form.cleaned_data.get('content')
			author = request.user
			p = posts(title = title , content = content , author = author)
			p.save()
			return redirect('home')

	else:
		form = CreatePost()
		contents ={
			'posts' : posts.objects.all().order_by('-date_posted'),
			'form' : form
		}


	return render(request,'blog/home.html' , contents)

# class PostListView(LoginRequiredMixin,ListView):
# 	model = posts
# 	template_name = 'blog/home.html'
# 	context_object_name = 'posts'
# 	ordering = ['-date_posted']
# 	paginate_by = 5


# 	def form_valid(self ,form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)


class UserPostListView(ListView):
	model = posts
	template_name = 'blog/user_post.html'
	context_object_name ='posts'
	odering = ['-date_posted']
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User , username = self.kwargs.get('username'))
		return posts.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
	model = posts
	template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
	model = posts
	fields = ['title' , 'content']
	template_name = 'blog/posts_form.html'

	def form_valid(self ,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
	model = posts
	fields = ['title' , 'content']

	def form_valid(self , form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
	model = posts
	template_name = 'blog/post_delete.html'

	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request , 'blog/about.html')