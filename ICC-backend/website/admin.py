from datetime import date

from django.contrib import messages
from django.utils.html import format_html

from django.contrib import admin
from .models import (
    Partner_Category, Activity, ActivityImage, ActivityContentBlock,
    Partner, Team_Member, Media, Member_Position, Directorate,
    DirectorateMembership, Statistic, Participant,
    Project, ProjectImage, ProjectTimelineEvent, ProjectContentBlock,
    ActivityCategory, CalendarMonth, Contact,
    SuccessCase, SuccessCaseParticipant
)

admin.site.site_header = 'Administração · Insper Consulting Club'
admin.site.site_title = 'Admin ICC'
admin.site.index_title = 'Conteúdo do site'


def miniatura(imagem, altura=40):
    """Mostra a imagem pequena nas listas e no formulário do admin."""
    if not imagem:
        return '—'
    return format_html(
        '<img src="{}" style="height:{}px;border-radius:4px;object-fit:cover">',
        imagem.url, altura,
    )

admin.site.register(Partner_Category)

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('logo', 'name', 'category', 'is_active', 'order')
    list_display_links = ('logo', 'name')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active', 'category')
    search_fields = ('name',)
    readonly_fields = ('logo_atual',)
    fields = ('name', 'logo_url', 'logo_atual', 'category', 'site', 'description', 'is_active', 'order')

    @admin.display(description='Logo')
    def logo(self, obj):
        return miniatura(obj.logo_url)

    @admin.display(description='Logo atual')
    def logo_atual(self, obj):
        return miniatura(obj.logo_url, 80)


@admin.register(Member_Position)
class MemberPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'power')
    list_editable = ('power',)
    ordering = ('power', 'title')
    search_fields = ('title',)



@admin.register(Directorate)
class DirectorateAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ('order',)


class DirectorateMembershipInline(admin.TabularInline):
    model = DirectorateMembership
    extra = 1
    fields = ('directorate', 'cargo', 'order')
    ordering = ('order',)

class SituacaoFilter(admin.SimpleListFilter):
    title = 'situação'
    parameter_name = 'situacao'

    def lookups(self, request, model_admin):
        return [('atual', 'Membros atuais'), ('ex', 'Ex-membros')]

    def queryset(self, request, queryset):
        if self.value() == 'atual':
            return queryset.filter(exit_date__isnull=True)
        if self.value() == 'ex':
            return queryset.filter(exit_date__isnull=False)
        return queryset


@admin.register(Team_Member)
class TeamMemberAdmin(admin.ModelAdmin):
    inlines = [DirectorateMembershipInline]
    list_display = ('foto', 'name', 'get_directorates', 'position', 'atual')
    list_display_links = ('foto', 'name')
    list_filter = (SituacaoFilter, 'directorate_memberships__directorate', 'position')
    # Exigido pelo autocomplete de participantes dos cases, e útil por si só
    # quando a lista acumula alumni além dos membros ativos.
    search_fields = ('name', 'linkedin')
    actions = ['arquivar', 'reativar']
    readonly_fields = ('foto_atual',)
    fieldsets = (
        (None, {'fields': ('name', 'photo', 'foto_atual', 'position', 'linkedin', 'email')}),
        ('Formação', {'fields': ('course', 'year')}),
        ('No ICC', {'fields': ('entry_date', 'exit_date', 'biography', 'trajetoria', 'hours', 'projects')}),
    )

    def get_directorates(self, obj):
        return ", ".join(m.directorate.name for m in obj.directorate_memberships.all())
    get_directorates.short_description = 'Diretorias'

    @admin.display(description='Foto')
    def foto(self, obj):
        return miniatura(obj.photo)

    @admin.display(description='Foto atual')
    def foto_atual(self, obj):
        return miniatura(obj.photo, 120)

    @admin.display(description='Atual', boolean=True)
    def atual(self, obj):
        return obj.exit_date is None

    @admin.action(description='Arquivar selecionados (sai da página Equipe)')
    def arquivar(self, request, queryset):
        n = queryset.filter(exit_date__isnull=True).update(exit_date=date.today())
        self.message_user(request, f'{n} membro(s) arquivado(s). O histórico continua guardado.', messages.SUCCESS)

    @admin.action(description='Reativar selecionados (volta para a página Equipe)')
    def reativar(self, request, queryset):
        n = queryset.exclude(exit_date__isnull=True).update(exit_date=None)
        self.message_user(request, f'{n} membro(s) reativado(s).', messages.SUCCESS)



admin.site.register(Participant)
admin.site.register(Contact)


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
    list_display = ('label', 'slug', 'badge', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('label',)

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


class SuccessCaseParticipantInline(admin.TabularInline):
    model = SuccessCaseParticipant
    extra = 1
    fields = ('member', 'role', 'order')
    ordering = ('role', 'order')
    autocomplete_fields = ('member',)


@admin.register(SuccessCase)
class SuccessCaseAdmin(admin.ModelAdmin):
    inlines = [SuccessCaseParticipantInline]
    list_display = ('semester', 'title', 'area', 'category', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'category', 'semester')
    search_fields = ('theme', 'area')

