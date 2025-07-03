# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from forum.models import Post, Comment
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import get_messages
from django.core.signals import request_finished
from django.core.mail import send_mail


def my_callback(sender, **kwargs):
    print('Request finished!')
    send_mail(
        'subject of some sort',
        'here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False
    )


request_finished.connect(my_callback)


def index(request):
    request.session.clear()
    messages.add_message(request, messages.INFO, 'Hello world!')
    return HttpResponse('<html><body>Our first response.</body></html>')


class TestTemplateView(TemplateView):
    template_name = 'test_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now().date()
        return context


class PostListView(ListView):
    model = Post
    context_object_name = 'post_data'

    def get_queryset(self):
        self.queryset = Post.objects.all()
        if self.kwargs.get('year'):
            self.queryset = self.queryset.filter(
                created_at__year=self.kwargs['year']
            )
        if self.kwargs.get('month'):
            self.queryset = self.queryset.filter(
                created_at__month=self.kwargs['month']
            )
        return self.queryset

    def render_to_response(self, context, **response_kwargs):
        first_viewed = self.request.session.get('first_viewed', False)
        if first_viewed:
            return HttpResponse(f'You first viewed on {first_viewed}')
        first_viewed_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.request.session['first_viewed'] = first_viewed_time

        message_content = ''
        storage = get_messages(self.request)
        for message in storage:
            message_content += f'<li>{message}</li>'

        posts = ''
        for post in context['post_data']:
            posts += f'<li>{post.title}</li>'
        return HttpResponse(
            f'<html><body>'
            f'<ul>{posts}</ul>'
            f'<ul>{message_content}</ul>'
            f'</body></html>'
        )


class PostDetailView(DetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        post = context.get('object')
        return HttpResponse(
            f'<html><body><ul>'
            f'<li>Title: {post.title}</li>'
            f'<li>Body: {post.body}</li>'
            f'<li>User: {post.user.first_name}</li>'
            f'</ul></body></html>'
        )


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comment_data'

    def get_queryset(self):
        self.queryset = Comment.objects.filter(post_id=self.kwargs['post_id'])
        return self.queryset

    def render_to_response(self, context, **response_kwargs):
        comments = ''
        for comment in context['comment_data']:
            comments += f'<li>{comment.body}</li>'
        return HttpResponse(f'<html><body><ul>{comments}</ul></body></html>')
