from django.contrib import admin
from tbs.travel.models import Region, HelpTopic, BlogSiteReview, Error, BlogEntry, BannerPic, BlogSite, Category
from tbs.reports.models import BlogSiteClick, BannerPicClick

class ErrorAdmin(admin.ModelAdmin):
    list_display = ['id', 'error_desc', 'error_text']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['submit_date', 'user', 'topic', 'type', 'feedback', 'status']

class HelpTopicAdmin(admin.ModelAdmin):
    list_display = ['question', 'group', 'sub_group', 'question_order']

admin.site.register(BannerPic)
admin.site.register(Error, ErrorAdmin)
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(BlogSiteReview)
admin.site.register(HelpTopic, HelpTopicAdmin)
admin.site.register(BlogEntry)
#admin.site.register(SponsorLevel)
admin.site.register(BlogSite)
admin.site.register(BlogSiteClick)
admin.site.register(BannerPicClick)
#admin.site.register(Feedback, FeedbackAdmin)