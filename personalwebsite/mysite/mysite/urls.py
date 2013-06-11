from django.conf.urls.defaults import *
from views import about_me, future_tech, places, fav_media, famous_quotes, current_datetime, index, detail


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', url(r'^aboutme/$', about_me), 
						    url(r'^futureTech/$',future_tech),
						    url(r'^places/$', places),
                            url(r'^inspire/$', famous_quotes),
                            url(r'^fav/$', fav_media),
                            url(r'^time/$', current_datetime),
                            url(r'^blog/$', index),
                            url(r'^(?P<blog_id>\d+)/$', detail),
                            
                            

						   
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
