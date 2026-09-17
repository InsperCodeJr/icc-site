import logging
from django.conf import settings
from django.db.models import Min, F
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import (
    Team_Member, Partner, Statistic, Project, Activity,
    ActivityCategory, CalendarMonth, SelectionProcess,
    Media, Contact, Directorate
)
from .serializers import (
    TeamMemberListSerializer, TeamMemberDetailSerializer,
    PartnerSerializer, StatisticSerializer,
    ProjectListSerializer, ProjectDetailSerializer,
    ActivitySerializer, ActivityDetailSerializer,
    ActivityCategorySerializer, CalendarMonthSerializer,
    DirectorateSerializer,
    SelectionProcessSerializer, MediaSerializer,
    ContactSerializer
)


class TeamMemberListView(generics.ListAPIView):
    serializer_class = TeamMemberListSerializer

    def get_queryset(self):
        show_all = self.request.query_params.get(
            "all", "false").lower() == "true"
        # Uma pessoa pode estar em mais de uma diretoria (ex: diretora de
        # Pedagógico e também mentora), então a ordem é dada pela primeira
        # (menor order) delas; membros sem nenhuma vão para o fim.
        qs = Team_Member.objects.select_related("position").prefetch_related(
            "directorate_memberships__directorate"
        ).annotate(
            min_directorate_order=Min("directorate_memberships__directorate__order")
        ).order_by(
            F("min_directorate_order").asc(nulls_last=True),
            "position__power", "name",
        )
        if not show_all:
            qs = qs.filter(exit_date__isnull=True)
        return qs


class TeamMemberDetailView(generics.RetrieveAPIView):
    serializer_class = TeamMemberDetailSerializer
    queryset = Team_Member.objects.select_related("position").prefetch_related(
        "projects__partners", "directorate_memberships__directorate"
    ).all()


class DirectorateListView(generics.ListAPIView):
    serializer_class = DirectorateSerializer
    queryset = Directorate.objects.all().order_by("order")


class PartnerListView(generics.ListAPIView):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        qs = Partner.objects.select_related("category").order_by("order", "name")
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
        qs = Project.objects.prefetch_related(
            "partners").select_related("category")
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


class MediaListView(generics.ListAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()


# class ContactInfoView(generics.RetrieveAPIView):
#     serializer_class = ContactInfoSerializer

#     def get_object(self):
#         return get_object_or_404(ContactInfo, is_active=True)


class SelectionProcessView(generics.RetrieveAPIView):
    serializer_class = SelectionProcessSerializer

    def get_object(self):
        return get_object_or_404(
            SelectionProcess.objects.prefetch_related(
                'stages', 'steps', 'requirements',
                'materials', 'materials__items'
            ),
            is_active=True
        )


class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        contact = serializer.save()
        self._send_notification(contact)

    def _send_notification(self, contact):
        api_key = settings.SENDGRID_API_KEY
        to_email = settings.EMAIL_DESTINATARIO
        from_email = settings.EMAIL_REMETENTE

        if not api_key or not to_email:
            return

        try:
            import sendgrid
            from sendgrid.helpers.mail import Mail

            message = Mail(
                from_email=from_email,
                to_emails=to_email,
                subject=f"Novo pedido de contato [{contact.get_contact_type_display()}]",
                html_content=f"""
                    <h2>Novo pedido de contato recebido!</h2>
                    <p><strong>Nome:</strong> {contact.name}</p>
                    <p><strong>Email:</strong> {contact.email}</p>
                    <p><strong>Telefone:</strong> {contact.phone}</p>
                    <p><strong>Mensagem:</strong></p>
                    <p>{contact.message}</p>
                """
            )
            sg = sendgrid.SendGridAPIClient(api_key=api_key)
            sg.send(message)
        except Exception:
            logging.getLogger(__name__).exception("Falha no envio do email")
