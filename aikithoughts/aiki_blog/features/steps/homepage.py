from behave import when, given, then

from aiki_blog.factories import PostFactory
from aiki_blog.models.post import Post
from aiki_blog.templatetags.markdownx import markdownxify


@given('these posts are added')
def posts_added(context):
    for row in context.table:
        post = PostFactory(title=row['title'])
        post.publish()


@when('I visit the homepage')
def visit_homepage(context):
    context.browser.visit(context.get_url('aiki:index'))


@then('I should see "{text}"')
def should_see_text(context, text):
    assert context.browser.is_text_present(text), '"{text}" not found'.format(text=text)


@then('I should see the post "{post_title}"')
def should_see_post(context, post_title):
    should_see_text(context, text=post_title)

    post = Post.objects.get(title=post_title)
    should_see_text(context, text=post.excerpt)
