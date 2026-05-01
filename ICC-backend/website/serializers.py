from rest_framework import serializers
from .models import Team_Member, Partner, Statistic, Project


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


class ProjectListSerializer(serializers.ModelSerializer):
    partners = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "partners", "start_date", "end_date"]


class ProjectDetailSerializer(serializers.ModelSerializer):
    partners = PartnerSerializer(many=True)
    members = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "title", "description", "partners", "start_date", "end_date", "members"]

    def get_members(self, obj):
        return [{"id": m.id, "name": m.name} for m in obj.members.all()]


class TeamMemberListSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Team_Member
        fields = ["id", "name", "position", "photo_url"]

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
