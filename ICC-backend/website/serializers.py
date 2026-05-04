from rest_framework import serializers
from .models import (
    Team_Member, Partner, Statistic, Project, ProjectImage,
    ProjectTimelineEvent, ProjectContentBlock,
    Activity, ActivityImage, ActivityContentBlock,
    ActivityCategory, CalendarMonth
)


class ActivityCategorySerializer(serializers.ModelSerializer):
    highlights = serializers.SerializerMethodField()
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = ActivityCategory
        fields = ["id", "slug", "label", "description", "highlights", "icon_url", "badge", "badge_class", "order"]

    def get_highlights(self, obj):
        return obj.get_highlights_list()

    def get_icon_url(self, obj):
        request = self.context.get("request")
        if obj.icon and request:
            return request.build_absolute_uri(obj.icon.url)
        return None


class CalendarMonthSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = CalendarMonth
        fields = ["id", "month", "items", "semester", "order"]

    def get_items(self, obj):
        return obj.get_items_list()


class PartnerSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = ["id", "name", "description", "category", "contato", "logo_url"]

    def get_logo_url(self, obj):
        request = self.context.get("request")
        if obj.logo_url and request:
            return request.build_absolute_uri(obj.logo_url.url)
        return None


class ProjectImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ["id", "image_url", "caption", "order"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProjectTimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTimelineEvent
        fields = ["id", "date", "title", "description", "order"]


class ContentBlockSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        fields = ["id", "title", "text", "image_url", "image_caption", "image_align", "order"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProjectContentBlockSerializer(ContentBlockSerializer):
    class Meta(ContentBlockSerializer.Meta):
        model = ProjectContentBlock


class ActivityContentBlockSerializer(ContentBlockSerializer):
    class Meta(ContentBlockSerializer.Meta):
        model = ActivityContentBlock


class ActivityImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ActivityImage
        fields = ["id", "image_url", "caption", "order"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProjectListSerializer(serializers.ModelSerializer):
    partners = serializers.StringRelatedField(many=True)
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "category", "partners", "start_date", "end_date"]


class ProjectDetailSerializer(serializers.ModelSerializer):
    partners = PartnerSerializer(many=True)
    category = ActivityCategorySerializer()
    members = serializers.SerializerMethodField()
    images = ProjectImageSerializer(many=True)
    timeline_events = ProjectTimelineEventSerializer(many=True)
    content_blocks = ProjectContentBlockSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "category",
            "partners", "start_date", "end_date",
            "members", "images", "timeline_events", "content_blocks"
        ]

    def get_members(self, obj):
        return [{"id": m.id, "name": m.name} for m in obj.members.all()]


class ActivitySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Activity
        fields = ["id", "title", "description", "category"]


class ActivityDetailSerializer(serializers.ModelSerializer):
    category = ActivityCategorySerializer()
    images = ActivityImageSerializer(many=True)
    content_blocks = ActivityContentBlockSerializer(many=True)
    responsible_partner = PartnerSerializer()

    class Meta:
        model = Activity
        fields = ["id", "title", "description", "category", "images", "content_blocks", "responsible_partner"]


class TeamMemberListSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Team_Member
        fields = [
            "id",
            "name",
            "position",
            "photo_url",
            "course",
            "year"
        ]

    def get_photo_url(self, obj):
        request = self.context.get("request")
        if obj.photo_url and request:
            return request.build_absolute_uri(obj.photo_url.url)
        return None


class TeamMemberDetailSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    photo_url = serializers.SerializerMethodField()
    projects = ProjectListSerializer(many=True)
    number_of_projects = serializers.IntegerField()

    class Meta:
        model = Team_Member
        fields = [
            "id",
            "name",
            "position",
            "photo_url",
            "biography",
            "number_of_projects",
            "projects",
            "hours",
            "entry_date",
            "exit_date",
            "course",
            "year",
            "email",
            "linkedin"
        ]

    def get_photo_url(self, obj):
        request = self.context.get("request")
        if obj.photo_url and request:
            return request.build_absolute_uri(obj.photo_url.url)
        return None
        


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ["id", "value", "description", "order"]