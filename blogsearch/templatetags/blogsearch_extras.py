from django import template
from tbs.travel.models import BlogSiteReview

register = template.Library()

@register.filter
def get_rating( value ):
    return range( value )

@register.filter
def get_max_rating( value ):
    return range( value )

#@register.filter
#def user_rated( self, current_user ):
#    review = BlogSiteReview.objects.filter(blog_site=self, user=request.user)
#    if review:
#        return True
#    else:
#        return False

