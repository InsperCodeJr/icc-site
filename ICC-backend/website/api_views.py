from rest_framework import generics
from .models import Team_Member, Partner, Statistic, Project
from .serializers import (
    TeamMemberListSerializer,
    TeamMemberDetailSerializer,
    PartnerSerializer,
    StatisticSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,
)


# ── Membros ───────────────────────────────────────────────────────────────────

class TeamMemberListView(generics.ListAPIView):
    """
    GET /api/members/
    Retorna membros ativos (sem exit_date), ordenados por cargo e nome.
    Query param opcional: ?all=true → inclui ex-membros também.
    """
    serializer_class = TeamMemberListSerializer

    def get_queryset(self):
        show_all = self.request.query_params.get("all", "false").lower() == "true"
        qs = Team_Member.objects.select_related("position").order_by("position__power", "name")
        if not show_all:
            qs = qs.filter(exit_date__isnull=True)
        return qs


class TeamMemberDetailView(generics.RetrieveAPIView):
    """
    GET /api/members/<id>/
    Retorna todos os dados de um membro, incluindo lista de projetos participados.
    """
    serializer_class = TeamMemberDetailSerializer
    queryset = Team_Member.objects.select_related("position").prefetch_related("projects__partners").all()


# ── Parceiros ─────────────────────────────────────────────────────────────────

class PartnerListView(generics.ListAPIView):
    """
    GET /api/partners/
    Retorna todos os parceiros.
    Query param opcional: ?category=<id> → filtra por categoria.
    """
    serializer_class = PartnerSerializer

    def get_queryset(self):
        qs = Partner.objects.select_related("category").order_by("name")
        category_id = self.request.query_params.get("category")
        if category_id:
            qs = qs.filter(category__id=category_id)
        return qs


class PartnerDetailView(generics.RetrieveAPIView):
    """
    GET /api/partners/<id>/
    Retorna os dados de um parceiro específico.
    """
    serializer_class = PartnerSerializer
    queryset = Partner.objects.select_related("category").all()


# ── Projetos ──────────────────────────────────────────────────────────────────

class ProjectListView(generics.ListAPIView):
    """
    GET /api/projects/
    Retorna todos os projetos, ordenados do mais recente para o mais antigo.
    """
    serializer_class = ProjectListSerializer
    queryset = Project.objects.prefetch_related("partners").all()


class ProjectDetailView(generics.RetrieveAPIView):
    """
    GET /api/projects/<id>/
    Retorna detalhes de um projeto, com parceiros e membros envolvidos.
    """
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.prefetch_related("partners", "members").all()


# ── Estatísticas ──────────────────────────────────────────────────────────────

class StatisticListView(generics.ListAPIView):
    """
    GET /api/statistics/
    Retorna as estatísticas da home, ordenadas pelo campo 'order'.
    """
    serializer_class = StatisticSerializer
    queryset = Statistic.objects.all().order_by("order")