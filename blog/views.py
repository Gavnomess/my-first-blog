from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, summator_model
from django.utils import timezone
from .forms import PostForm, sum_form
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Result_Serializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by
    ('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


############### Django REST framework ################

#class Result_view(generics.ListCreateAPIView):
#    queryset = summator_model.objects.all()
#    serializer_class = Result_Serializer
class Result_view(APIView):
#class Result_view(generics.RetrieveAPIView):
#    def get_html(request):
#        if request.method == "GET":
#            return render(request, 'blog/test.html',{'edits': edits})
    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/test_REST_Django.html'

    def get(self, request):
        #queryset = summator_model.objects.all()
        #serializer = Result_Serializer(edits, many=True)
        #return Response({"edits": serializer.data})
        #edits = get_object_or_404(summator_model)
        edits = summator_model()
        serializer = Result_Serializer(edits)
        #return Response({'serializer': serializer, 'edits': edits})
        
       
        return Response({'serializer': serializer})

    def post(self, request):
        edits = summator_model(request.POST)
        #a  = int (edits['edit1_model'].data) + int (edits['edit2_model'].data)
        #edits.fields['edit_result_model'].initial = a
       
        serializer = Result_Serializer(edits)
        
        return Response({"serializer": serializer})



#    def post(self, request):
#        edits = get_object_or_404(summator_model)
#        serializer = Result_Serializer(edits, data=request.data)
#        if not serializer.is_valid():
#            return Response({'serializer': serializer, 'edits': edits})
#        serializer.save()
#        return redirect('edits-list')





########### full Django solution ###############

def get_result(request):
    if request.method == "POST":       
        answer = sum_form(request.POST)
        answer1 = sum_form()

        answer1.fields['edit_result'].label = ''
        
        a  = int (answer['edit1'].data) + int (answer['edit2'].data)
        answer1.fields['edit_result'].initial = a

        return render(request, 'blog/test_full_Django.html',{'answer1': answer1})
           
    else:
        answer = sum_form()
        return render(request, 'blog/test_full_Django.html',{'answer': answer})
		
