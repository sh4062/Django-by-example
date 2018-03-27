from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import Post

@register.simple_tag#每一个模板标签都需要包含r～变量来表明自己是一个有效的标签库
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count = 5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count = 5):
    return Post.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]

@register.filter(name = 'markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))