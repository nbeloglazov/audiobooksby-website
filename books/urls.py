from django.urls import include, path
from books.views import stats, catalog, book, person, support, articles, publisher

urlpatterns = [
    path('', catalog.index, name='index'),
    path('catalog', catalog.catalog, name='catalog-all-books'),
    path('catalog/<slug:tag_slug>', catalog.catalog, name='catalog-for-tag'),
    path('releases/<int:year>', catalog.releases),
    path('releases/<int:year>/<int:month>', catalog.releases),
    path('books/<slug:slug>', book.book_detail, name='book-detail-page'),
    path('person/<slug:slug>', person.person_detail,
         name='person-detail-page'),
    path('publisher/<slug:slug>',
         publisher.publisher_detail,
         name='publisher-detail-page'),
    path('about', stats.about, name='about'),
    path('stats/birthdays', stats.birthdays),
    path('stats/digest', stats.digest),
    path('articles', articles.redirect_to_first_article, name='all-articles'),
    path('articles/<slug:slug>',
         articles.single_article,
         name='single-article'),
    path('search', support.search, name='search'),
    path("404", support.page_not_found),
    path('robots.txt', support.robots_txt),
    path('sitemap.txt', support.sitemap),
    path('data.json', support.get_data_json),
    path('job/push_data_to_algolia', support.push_data_to_algolia),
    # /_ah/warmup - App Engine specific endpoint to pre-warm application for traffic
    # https://cloud.google.com/appengine/docs/standard/configuring-warmup-requests?tab=python#enabling_warmup_requests
    path('_ah/warmup', support.generate_data_json),
    path('job/generate_data_json', support.generate_data_json),
    path('job/update_read_by_author_tag', support.update_read_by_author_tag),
    path('job/sync_image_cache', support.sync_image_cache),
    path('api/markdown_preview', support.markdown_to_html),
    path('api/livelib_books', support.get_livelib_books),
    path('api/convert_orthography', support.convert_orthography),
    path("i18n/", include("django.conf.urls.i18n")),
]
