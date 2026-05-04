from django.urls import path
from . import api_views

urlpatterns = [

    # ── Membros ───────────────────────────────────────────────────────────────
    path('api/members/', api_views.TeamMemberListView.as_view(), name='api-members-list'),
    path('api/members/<int:pk>/', api_views.TeamMemberDetailView.as_view(), name='api-members-detail'),

    # ── Parceiros ─────────────────────────────────────────────────────────────
    path('api/partners/', api_views.PartnerListView.as_view(), name='api-partners-list'),
    path('api/partners/<int:pk>/', api_views.PartnerDetailView.as_view(), name='api-partners-detail'),

    # ── Projetos ──────────────────────────────────────────────────────────────
    path('api/projects/', api_views.ProjectListView.as_view(), name='api-projects-list'),
    path('api/projects/<int:pk>/', api_views.ProjectDetailView.as_view(), name='api-projects-detail'),

    # ── Estatísticas ──────────────────────────────────────────────────────────
    path('api/statistics/', api_views.StatisticListView.as_view(), name='api-statistics-list'),
]
