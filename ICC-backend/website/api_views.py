from rest_framework import generics
from .models import Team_Member, Partner, Statistic, Project, Activity, ActivityCategory, CalendarMonth
from .serializers import (
    TeamMemberListSerializer, TeamMemberDetailSerializer,
    PartnerSerializer, StatisticSerializer,
    ProjectListSerializer, ProjectDetailSerializer,
    ActivitySerializer, ActivityDetailSerializer,
    ActivityCategorySerializer, CalendarMonthSerializer,
)


class TeamMemberListView(generics.ListAPIView):
    serializer_class = TeamMemberListSerializer

    def get_queryset(self):
        show_all = self.request.query_params.get("all", "false").lower() == "true"
        qs = Team_Member.objects.select_related("position").order_by("position__power", "name")
        if not show_all:
            qs = qs.filter(exit_date__isnull=True)
        return qs


class TeamMemberDetailView(generics.RetrieveAPIView):
    serializer_class = TeamMemberDetailSerializer
    queryset = Team_Member.objects.select_related("position").prefetch_related("projects__partners").all()


class PartnerListView(generics.ListAPIView):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        qs = Partner.objects.select_related("category").order_by("name")
        category_id = self.request.query_params.get("category")
        if category_id:
            qs = qs.filter(category__id=category_id)
        return qs


class PartnerDetailView(generics.RetrieveAPIView):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.select_related("category").all()


class ActivityCategoryListView(generics.ListAPIView):
    serializer_class = ActivityCategorySerializer
    queryset = ActivityCategory.objects.all().order_by("order")


class CalendarMonthListView(generics.ListAPIView):
    serializer_class = CalendarMonthSerializer

    def get_queryset(self):
        qs = CalendarMonth.objects.all().order_by("order")
        semester = self.request.query_params.get("semester")
        if semester:
            qs = qs.filter(semester__in=[semester, "both"])
        return qs


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectListSerializer

    def get_queryset(self):
        qs = Project.objects.prefetch_related("partners").select_related("category")
        category = self.request.query_params.get("category")
        if category:
            qs = qs.filter(category__slug=category)
        return qs


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.prefetch_related(
        "partners", "members", "images", "timeline_events", "content_blocks"
    ).select_related("category").all()


class ActivityListView(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        qs = Activity.objects.select_related("category")
        category = self.request.query_params.get("category")
        if category:
            qs = qs.filter(category__slug=category)
        return qs


class ActivityDetailView(generics.RetrieveAPIView):
    serializer_class = ActivityDetailSerializer
    queryset = Activity.objects.prefetch_related(
        "images", "content_blocks"
    ).select_related("category", "responsible_partner").all()


class StatisticListView(generics.ListAPIView):
    serializer_class = StatisticSerializer
    queryset = Statistic.objects.all().order_by("order")