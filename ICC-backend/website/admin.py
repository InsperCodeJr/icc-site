from django.contrib import admin
from .models import (
    Partner_Category, Activity, ActivityImage, ActivityContentBlock,
    Partner, Team_Member, Media, Member_Position, Statistic, Participant,
    Project, ProjectImage, ProjectTimelineEvent, ProjectContentBlock,
    ActivityCategory, CalendarMonth
)

admin.site.register(Partner_Category)
admin.site.register(Partner)
admin.site.register(Team_Member)
admin.site.register(Member_Position)
admin.site.register(Participant)


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


class SelectionProcessStageInline(admin.TabularInline):
    model = SelectionProcessStage
    extra = 1
    fields = ('label', 'date', 'order')
    ordering = ('order',)


class SelectionProcessStepInline(admin.StackedInline):
    model = SelectionProcessStep
    extra = 1
    fields = ('number', 'title', 'description', 'image', 'duration', 'tips', 'order')
    ordering = ('order',)


class SelectionProcessRequirementInline(admin.TabularInline):
    model = SelectionProcessRequirement
    extra = 1
    fields = ('text', 'icon', 'order')
    ordering = ('order',)
class PreparationMaterialItemInline(admin.TabularInline):
    model = PreparationMaterialItem
    extra = 1
    fields = ('text', 'order')
    ordering = ('order',)
 
 
class PreparationMaterialInline(admin.StackedInline):
    model = PreparationMaterial
    extra = 1
    fields = ('title', 'order')
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


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'date', 'order')
    list_editable = ('order',)
    ordering = ('-date', 'order')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'instagram', 'linkedin', 'whatsapp', 'is_active')


@admin.register(SelectionProcess)
class SelectionProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    inlines = [
        SelectionProcessStageInline,
        SelectionProcessRequirementInline,
        SelectionProcessStepInline,
        PreparationMaterialInline,
    ]
@admin.register(PreparationMaterial)
class PreparationMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'process', 'order')
    inlines = [PreparationMaterialItemInline]
 