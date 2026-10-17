from django import forms
from django.contrib import admin, messages
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import (
    Partner_Category, Activity, ActivityImage, ActivityContentBlock,
    Partner, Team_Member, Media, Member_Position, Directorate,
    DirectorateMembership, Statistic, Participant,
    Project, ProjectImage, ProjectTimelineEvent, ProjectContentBlock,
    ActivityCategory, CalendarMonth, Contact,
    SuccessCase, SuccessCaseParticipant,
    SelectionProcess, SelectionProcessStage, SelectionProcessStep,
    SelectionProcessRequirement, PreparationMaterial, PreparationMaterialItem,
)

# Títulos do topo e da página inicial do /admin
admin.site.site_header = 'ICC — Administração do site'
admin.site.site_title = 'ICC Admin'
admin.site.index_title = 'Gerenciar conteúdo do site'


# ---------------------------------------------------------------------------
# Parceiros
# ---------------------------------------------------------------------------

@admin.register(Partner_Category)
class PartnerCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'contato', 'site', 'order')
    list_editable = ('order',)
    list_filter = ('category',)
    # Exigido pelo autocomplete de "parceiro responsável" em Atividades.
    search_fields = ('name', 'description', 'contato')
    ordering = ('order', 'name')


# ---------------------------------------------------------------------------
# Equipe
# ---------------------------------------------------------------------------

@admin.register(Member_Position)
class MemberPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'power')
    list_editable = ('power',)
    search_fields = ('title',)
    ordering = ('-power',)


@admin.register(Directorate)
class DirectorateAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)
    ordering = ('order',)


class DirectorateMembershipForm(forms.ModelForm):
    class Meta:
        model = DirectorateMembership
        fields = '__all__'
        labels = {'directorate': 'Diretoria'}


class DirectorateMembershipInline(admin.TabularInline):
    model = DirectorateMembership
    form = DirectorateMembershipForm
    extra = 1
    fields = ('directorate', 'cargo', 'order')
    ordering = ('order',)


class MemberStatusFilter(admin.SimpleListFilter):
    """Separa membros ativos de ex-membros (quem tem data de saída)."""
    title = _('situação')
    parameter_name = 'situacao'

    def lookups(self, request, model_admin):
        return (('ativo', _('Ativos')), ('ex', _('Ex-membros')))

    def queryset(self, request, queryset):
        if self.value() == 'ativo':
            return queryset.filter(exit_date__isnull=True)
        if self.value() == 'ex':
            return queryset.filter(exit_date__isnull=False)
        return queryset


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = Team_Member
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'photo': 'Foto',
            'biography': 'Biografia',
            'position': 'Posição',
            'course': 'Curso',
            'year': 'Ano',
            'hours': 'Horas',
            'entry_date': 'Data de entrada',
            'exit_date': 'Data de saída (preencha para arquivar o membro)',
        }
        help_texts = {
            'exit_date': 'Quem tem data de saída deixa de aparecer no site, '
                         'mas o histórico continua guardado. Apague a data para reativar.',
        }


@admin.register(Team_Member)
class TeamMemberAdmin(admin.ModelAdmin):
    form = TeamMemberForm
    actions = ['arquivar_membros', 'reativar_membros']
    inlines = [DirectorateMembershipInline]
    list_display = ('name', 'get_directorates', 'position', 'course', 'year',
                    'entry_date', 'exit_date', 'is_active')
    list_filter = (MemberStatusFilter, 'directorate_memberships__directorate',
                   'position', 'year')
    # Exigido pelo autocomplete de participantes dos cases.
    search_fields = ('name', 'email', 'course')
    list_select_related = ('position',)
    filter_horizontal = ('projects',)
    date_hierarchy = 'entry_date'
    list_per_page = 50

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('directorate_memberships__directorate')

    @admin.display(description='Diretorias')
    def get_directorates(self, obj):
        return ', '.join(m.directorate.name for m in obj.directorate_memberships.all())

    @admin.display(description='Ativo', boolean=True)
    def is_active(self, obj):
        return obj.exit_date is None

    # Soft delete: membros não são apagados, só arquivados (data de saída).
    def has_delete_permission(self, request, obj=None):
        return False

    @admin.action(description='Arquivar membros selecionados (saída = hoje)')
    def arquivar_membros(self, request, queryset):
        n = queryset.filter(exit_date__isnull=True).update(exit_date=timezone.localdate())
        self.message_user(request, f'{n} membro(s) arquivado(s).', messages.SUCCESS)

    @admin.action(description='Reativar membros selecionados')
    def reativar_membros(self, request, queryset):
        n = queryset.filter(exit_date__isnull=False).update(exit_date=None)
        self.message_user(request, f'{n} membro(s) reativado(s).', messages.SUCCESS)


# ---------------------------------------------------------------------------
# Contato e inscrições
# ---------------------------------------------------------------------------

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'contact_type')
    list_filter = ('contact_type',)
    search_fields = ('name', 'email', 'phone', 'message')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'course', 'semester', 'created_at')
    list_filter = ('semester', 'course', 'created_at')
    search_fields = ('name', 'email', 'course', 'reason')
    date_hierarchy = 'created_at'


# ---------------------------------------------------------------------------
# Projetos
# ---------------------------------------------------------------------------

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


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date')
    list_filter = ('category', 'start_date')
    search_fields = ('title', 'description')
    filter_horizontal = ('partners',)
    date_hierarchy = 'start_date'
    list_select_related = ('category',)
    inlines = [ProjectImageInline, ProjectTimelineEventInline, ProjectContentBlockInline]


# ---------------------------------------------------------------------------
# Atividades e calendário
# ---------------------------------------------------------------------------

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


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'responsible_partner')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    autocomplete_fields = ('responsible_partner',)
    list_select_related = ('category', 'responsible_partner')
    inlines = [ActivityImageInline, ActivityContentBlockInline]


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'slug', 'badge', 'order')
    list_editable = ('order',)
    search_fields = ('label', 'slug', 'description')
    ordering = ('order',)
    prepopulated_fields = {'slug': ('label',)}


@admin.register(CalendarMonth)
class CalendarMonthAdmin(admin.ModelAdmin):
    list_display = ('month', 'year', 'semester', 'order')
    list_editable = ('order', 'semester')
    list_filter = ('semester', 'year')
    search_fields = ('month', 'items')
    ordering = ('year', 'order')


# ---------------------------------------------------------------------------
# Home e notícias
# ---------------------------------------------------------------------------

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('value', 'description', 'order')
    list_editable = ('order',)
    search_fields = ('value', 'description')
    ordering = ('order',)


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'date', 'order')
    list_editable = ('order',)
    list_filter = ('source', 'date')
    search_fields = ('title', 'description', 'source')
    date_hierarchy = 'date'
    ordering = ('-date', 'order')


# ---------------------------------------------------------------------------
# Cases de sucesso
# ---------------------------------------------------------------------------

class SuccessCaseParticipantInline(admin.TabularInline):
    model = SuccessCaseParticipant
    extra = 1
    fields = ('member', 'role', 'order')
    ordering = ('role', 'order')
    autocomplete_fields = ('member',)


@admin.register(SuccessCase)
class SuccessCaseAdmin(admin.ModelAdmin):
    inlines = [SuccessCaseParticipantInline]
    list_display = ('semester', 'area', 'title', 'category', 'award')
    list_filter = ('category', 'semester')
    search_fields = ('title', 'area', 'theme', 'award')
    list_select_related = ('category',)


# ---------------------------------------------------------------------------
# Processo seletivo (página /processo)
# ---------------------------------------------------------------------------

class SelectionProcessStageInline(admin.TabularInline):
    model = SelectionProcessStage
    extra = 1
    fields = ('label', 'date', 'order')
    ordering = ('order',)


class SelectionProcessStepInline(admin.StackedInline):
    model = SelectionProcessStep
    extra = 0
    fields = ('number', 'title', 'description', 'image', 'duration', 'tips', 'order')
    ordering = ('order',)


class SelectionProcessRequirementInline(admin.TabularInline):
    model = SelectionProcessRequirement
    extra = 1
    fields = ('text', 'icon', 'order')
    ordering = ('order',)


@admin.register(SelectionProcess)
class SelectionProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    inlines = [SelectionProcessStageInline, SelectionProcessStepInline,
               SelectionProcessRequirementInline]


class PreparationMaterialItemInline(admin.TabularInline):
    model = PreparationMaterialItem
    extra = 1
    fields = ('text', 'order')
    ordering = ('order',)


@admin.register(PreparationMaterial)
class PreparationMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'process', 'order')
    list_editable = ('order',)
    list_filter = ('process',)
    search_fields = ('title',)
    inlines = [PreparationMaterialItemInline]