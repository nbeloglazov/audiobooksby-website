from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog-all-books'),
    path('catalog/<slug:slug>', views.catalog, name='catalog-for-tag'),
    path('books/<slug:slug>', views.book_detail, name='book-detail-page'),
    path('person/<slug:slug>', views.person_detail, name='person-detail-page'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('push_data_to_algolia', views.push_data_to_algolia),
    path("404", views.page_not_found),
    path('robots.txt', views.robots_txt),
    path('sitemap.txt', views.sitemap),
    path('posts/jak-vyklasci-audyjaknihu',
         views.how_to_publish_audiobook,
         name='how-to-publish-audiobook')
]
