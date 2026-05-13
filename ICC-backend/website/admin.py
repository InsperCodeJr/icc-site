from django.contrib import admin
from .models import (
    Partner_Category, Activity, ActivityImage, ActivityContentBlock,
    Partner, Team_Member, Media, Member_Position, Statistic, Participant,
    Project, ProjectImage, ProjectTimelineEvent, ProjectContentBlock,
    ActivityCategory, CalendarMonth, Contact
)

admin.site.register(Partner_Category)
admin.site.register(Partner)
admin.site.register(Team_Member)
admin.site.register(Media)
admin.site.register(Member_Position)
admin.site.register(Participant)
admin.site.register(Contact)


# ── Inlines ───────────────────────────────────────────────────────────────────

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption', 'order')
    ordering = ('order',)


class ProjectTimelineEventInline(admin.TabularInline):
    model = ProjectTimelineEvent
    extra = 1
    fields = ('date', 'title', 'description', 'order')
    ordering = ('order',)


class ProjectContentBlockInline(admin.StackedInline):
    model = ProjectContentBlock
    extra = 1
    fields = ('title', 'text', 'image', 'image_caption', 'image_align', 'order')
    ordering = ('order',)


class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1
    fields = ('image', 'caption', 'order')
    ordering = ('order',)


class ActivityContentBlockInline(admin.StackedInline):
    model = ActivityContentBlock
    extra = 1
    fields = ('title', 'text', 'image', 'image_caption', 'image_align', 'order')
    ordering = ('order',)


# ── Model Admins ──────────────────────────────────────────────────────────────

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date')
    list_filter = ('category',)
    inlines = [ProjectImageInline, ProjectTimelineEventInline, ProjectContentBlockInline]


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    inlines = [ActivityImageInline, ActivityContentBlockInline]


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug', 'badge', 'order')
    list_editable = ('order',)
    ordering = ('order',)
    prepopulated_fields = {'slug': ('label',)}


@admin.register(CalendarMonth)
class CalendarMonthAdmin(admin.ModelAdmin):
    list_display = ('month', 'semester', 'order')
    list_editable = ('order', 'semester')
    ordering = ('order',)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('value', 'description', 'order')
    list_editable = ('order',)
    ordering = ('order',)