from django.urls import path

from chair.views import export
from .views import dashboard, submissions, users


app_name = 'chair'

urlpatterns = [
    path('<int:conf_pk>/', dashboard.overview, name='home'),

    #
    # Submissions
    #
    path('<int:conf_pk>/submissions/', submissions.list_submissions, name='submissions'),
    path('<int:conf_pk>/submissions/create/', submissions.create_submission, name='submission-create'),
    path('<int:conf_pk>/submissions/compose_redirect/', submissions.compose_redirect, name='submissions-compose-redirect'),
    path('submissions/<int:sub_pk>/feed_item/', submissions.feed_item, name='submission-feed-item'),
    path('submissions/<int:sub_pk>/overview/', submissions.overview, name='submission-overview'),
    path('submissions/<int:sub_pk>/metadata/', submissions.metadata, name='submission-metadata'),
    path('submissions/<int:sub_pk>/authors/', submissions.authors, name='submission-authors'),
    path('submissions/<int:sub_pk>/authors/delete/', submissions.delete_author, name='submission-author-delete'),
    path('submissions/<int:sub_pk>/authors/create/', submissions.create_author, name='submission-author-create'),
    path('submissions/<int:sub_pk>/authors/invite/', submissions.invite_author, name='submission-author-invite'),
    path('submissions/<int:sub_pk>/authors/reorder/', submissions.reorder_authors, name='submission-authors-reorder'),
    path('submissions/<int:sub_pk>/rev_man/', submissions.review_manuscript, name='submission-review-manuscript'),
    path('submissions/<int:sub_pk>/rev_man/delete/', submissions.delete_review_manuscript, name='submission-review-manuscript-delete'),
    path('submissions/<int:sub_pk>/revoke_review/', submissions.revoke_review, name='revoke-review'),
    path('submissions/<int:sub_pk>/reviews/', submissions.reviews, name='submission-reviewers'),
    path('submissions/<int:sub_pk>/messages/', submissions.emails, name='submission-messages'),
    path('submissions/<int:sub_pk>/camera_ready/', submissions.camera_ready, name='submission-camera-ready'),
    path('submissions/<int:sub_pk>/reviews/assign/', submissions.assign_reviewer, name='assign-reviewer'),
    path('submissions/<int:sub_pk>/reviews/<int:rev_pk>/delete/', submissions.delete_review, name='delete-review'),
    path('submissions/<int:sub_pk>/delete/', submissions.delete_submission, name='submission-delete'),
    path('attachments/<int:att_pk>/download/', submissions.download_attachment, name='download-attachment'),

    #
    # Users
    #
    path('<int:conf_pk>/users/', users.list_users, name='users'),
    path('<int:conf_pk>/users/compose_redirect/', users.compose_redirect, name='users-compose-redirect'),
    path('<int:conf_pk>/users/<int:user_pk>/feed_item/', users.feed_item, name='user-feed-item'),
    path('<int:conf_pk>/users/<int:user_pk>/overview/', users.overview, name='user-overview'),
    path('<int:conf_pk>/users/<int:user_pk>/messages/', users.emails, name='user-messages'),
    path('<int:conf_pk>/users/export/csv/', users.export_csv, name='users-export-csv'),

    #
    # Exports
    #
    path('<int:conf_pk>/export/submissions/', export.export_submissions, name='export-submissions'),
    path('<int:conf_pk>/export/reviews_doc/', export.export_reviews_doc, name='export-reviews-doc'),
]
