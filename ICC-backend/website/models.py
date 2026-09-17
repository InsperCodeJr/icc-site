from django.db import models


class Partner_Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categorias dos Parceiros'

    def __str__(self):
        return self.title


class Directorate(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name = 'Diretoria'
        verbose_name_plural = 'Diretorias'
        ordering = ['order']

    def __str__(self):
        return self.name


class Member_Position(models.Model):
    title = models.CharField(max_length=200)
    power = models.IntegerField(
        verbose_name='Prioridade para exibição',
        help_text='Digite 1 para maior prioridade ou 2 para menor.'
    )

    class Meta:
        verbose_name_plural = 'Posição de Membros'

    def __str__(self):
        return self.title


class Partner(models.Model):
    logo_url = models.ImageField(upload_to='partners/')
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        Partner_Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    contato = models.CharField(max_length=20)

    site = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Site do parceiro'
    )
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name_plural = 'Parceiros'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    @property
    def projects_count(self):
        return self.projects.count()

    @property
    def success_cases_count(self):
        return self.projects.filter(end_date__isnull=False).count()


BADGE_CHOICES = [
    ('badge--continuo', 'Contínuo'),
    ('badge--semanal', 'Semanal'),
    ('badge--mensal', 'Mensal'),
    ('badge--semestral', 'Semestral'),
]

SEMESTER_CHOICES = [
    ('1', 'Primeiro Semestre'),
    ('2', 'Segundo Semestre'),
    ('both', 'Ambos'),
]

IMAGE_ALIGN_CHOICES = [
    ('right', 'Imagem à direita'),
    ('left', 'Imagem à esquerda'),
    ('center', 'Imagem centralizada (sem texto)'),
]


class ActivityCategory(models.Model):
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug (identificador na URL)')
    label = models.CharField(max_length=200, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    highlights = models.TextField(verbose_name='Tópicos', blank=True, help_text='Um tópico por linha.')
    icon = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name='Ícone do card')
    badge = models.CharField(max_length=50, verbose_name='Frequência (badge)')
    badge_class = models.CharField(max_length=50, choices=BADGE_CHOICES, verbose_name='Estilo do badge', default='badge--semanal')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name = 'Categoria de Atividade'
        verbose_name_plural = 'Categorias de Atividades'
        ordering = ['order']

    def __str__(self):
        return self.label

    def get_highlights_list(self):
        return [line.strip() for line in self.highlights.splitlines() if line.strip()]


class CalendarMonth(models.Model):
    month = models.CharField(max_length=50, verbose_name='Mês')
    year = models.IntegerField(
        null=True, blank=True, verbose_name='Ano',
        help_text='Necessário para o frontend desenhar a grade de dias da semana. Sem ano, só a lista de tópicos é exibida.',
    )
    items = models.TextField(
        verbose_name='Tópicos',
        help_text='Um tópico por linha. Para aparecer na grade de dias, use o formato "DD/MM - Título" (é o que import_calendar_ics gera).',
    )
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default='both', verbose_name='Semestre')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name = 'Mês do Calendário'
        verbose_name_plural = 'Calendário do Semestre'
        ordering = ['year', 'order']
        constraints = [
            models.UniqueConstraint(fields=['month', 'year'], name='unique_month_per_year'),
        ]

    def __str__(self):
        return f"{self.month}/{self.year}" if self.year else self.month

    def get_items_list(self):
        return [line.strip() for line in self.items.splitlines() if line.strip()]


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    category = models.ForeignKey(
        ActivityCategory, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Categoria', related_name='projects'
    )
    partners = models.ManyToManyField(Partner, blank=True, verbose_name='Parceiros envolvidos', related_name='projects')
    start_date = models.DateField(verbose_name='Data de início')
    end_date = models.DateField(null=True, blank=True, verbose_name='Data de conclusão')

    class Meta:
        verbose_name_plural = 'Projetos'
        ordering = ['-start_date']

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images', verbose_name='Projeto')
    image = models.ImageField(upload_to='projects/images/', verbose_name='Imagem')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Legenda')
    order = models.IntegerField(default=0, verbose_name='Ordem')

    class Meta:
        verbose_name = 'Imagem do Projeto'
        verbose_name_plural = 'Imagens do Projeto'
        ordering = ['order']

    def __str__(self):
        return f"Imagem {self.order} — {self.project.title}"


class ProjectTimelineEvent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='timeline_events', verbose_name='Projeto')
    date = models.DateField(verbose_name='Data')
    title = models.CharField(max_length=200, verbose_name='Título do evento')
    description = models.TextField(blank=True, verbose_name='Descrição')
    order = models.IntegerField(default=0, verbose_name='Ordem')

    class Meta:
        verbose_name = 'Evento do Cronograma'
        verbose_name_plural = 'Eventos do Cronograma'
        ordering = ['date', 'order']

    def __str__(self):
        return f"{self.date} — {self.title}"


class ProjectContentBlock(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='content_blocks', verbose_name='Projeto')
    title = models.CharField(max_length=200, blank=True, verbose_name='Título do bloco (opcional)')
    text = models.TextField(blank=True, verbose_name='Texto')
    image = models.ImageField(upload_to='projects/content/', null=True, blank=True, verbose_name='Imagem (opcional)')
    image_caption = models.CharField(max_length=200, blank=True, verbose_name='Legenda da imagem')
    image_align = models.CharField(max_length=10, choices=IMAGE_ALIGN_CHOICES, default='right', verbose_name='Posição da imagem')
    order = models.IntegerField(default=0, verbose_name='Ordem')

    class Meta:
        verbose_name = 'Bloco de Conteúdo'
        verbose_name_plural = 'Blocos de Conteúdo'
        ordering = ['order']

    def __str__(self):
        return f"Bloco {self.order} — {self.project.title}"


class Team_Member(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='team/', null=True, blank=True)
    biography = models.TextField(max_length=200)
    position = models.ForeignKey(Member_Position, on_delete=models.PROTECT, null=True)
    course = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=50, null=True, blank=True)
    hours = models.IntegerField(null=True)
    entry_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    linkedin = models.URLField(null=True, blank=True, verbose_name='LinkedIn')
    trajetoria = models.JSONField(
        default=list, blank=True, verbose_name='Trajetória',
        help_text='Lista de {"semestre": "2026.1", "cargo": "Trainee"}, mais recente por último.'
    )
    projects = models.ManyToManyField(Project, blank=True, verbose_name='Projetos participados', related_name='members')

    class Meta:
        verbose_name_plural = 'Membros do Time'

    def __str__(self):
        return self.name

    @property
    def number_of_projects(self):
        return self.projects.count()


class DirectorateMembership(models.Model):
    """
    Vincula um membro a uma diretoria com o cargo específico que ele tem
    nela. Existe como model à parte (em vez de M2M direto ou FK único em
    Team_Member) porque uma pessoa pode estar em mais de uma diretoria ao
    mesmo tempo com cargos diferentes em cada uma (ex: Diretora de
    Pedagógico e, também, Mentora na Escola de Mentores).
    """
    member = models.ForeignKey(Team_Member, on_delete=models.CASCADE, related_name='directorate_memberships')
    directorate = models.ForeignKey(Directorate, on_delete=models.CASCADE, related_name='memberships')
    cargo = models.CharField(max_length=200, verbose_name='Cargo nessa diretoria')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name = 'Vínculo com Diretoria'
        verbose_name_plural = 'Vínculos com Diretorias'
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(fields=['member', 'directorate'], name='unique_member_per_directorate'),
        ]

    def __str__(self):
        return f"{self.member.name} - {self.cargo} ({self.directorate.name})"


class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(
        ActivityCategory, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Categoria', related_name='activities'
    )
    responsible_partner = models.ForeignKey(Partner, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.title


class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='images', verbose_name='Atividade')
    image = models.ImageField(upload_to='activities/images/', verbose_name='Imagem')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Legenda')
    order = models.IntegerField(default=0, verbose_name='Ordem')

    class Meta:
        verbose_name = 'Imagem da Atividade'
        verbose_name_plural = 'Imagens da Atividade'
        ordering = ['order']

    def __str__(self):
        return f"Imagem {self.order} — {self.activity.title}"


class ActivityContentBlock(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='content_blocks', verbose_name='Atividade')
    title = models.CharField(max_length=200, blank=True, verbose_name='Título do bloco (opcional)')
    text = models.TextField(blank=True, verbose_name='Texto')
    image = models.ImageField(upload_to='activities/content/', null=True, blank=True, verbose_name='Imagem (opcional)')
    image_caption = models.CharField(max_length=200, blank=True, verbose_name='Legenda da imagem')
    image_align = models.CharField(max_length=10, choices=IMAGE_ALIGN_CHOICES, default='right', verbose_name='Posição da imagem')
    order = models.IntegerField(default=0, verbose_name='Ordem')

    class Meta:
        verbose_name = 'Bloco de Conteúdo'
        verbose_name_plural = 'Blocos de Conteúdo'
        ordering = ['order']

    def __str__(self):
        return f"Bloco {self.order} — {self.activity.title}"


class Media(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    link = models.URLField(verbose_name='Link da notícia')
    image = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name='Imagem de capa')
    source = models.CharField(max_length=200, blank=True, verbose_name='Fonte')
    date = models.DateField(null=True, blank=True, verbose_name='Data de publicação')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['-date', 'order']

    def __str__(self):
        return self.title


class Statistic(models.Model):
    value = models.CharField(max_length=50, verbose_name='Valor/Número')
    description = models.CharField(max_length=200, verbose_name='Descrição')
    order = models.IntegerField(default=0, verbose_name='Ordem de exibição')

    class Meta:
        verbose_name_plural = 'Estatísticas'
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.description}"


class Participant(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    course = models.CharField(max_length=200, verbose_name='Curso')
    semester = models.CharField(max_length=50, verbose_name='Semestre')
    reason = models.TextField(verbose_name='Por que quer entrar no ICC?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de inscrição')

    class Meta:
        verbose_name_plural = 'Participantes'

    def __str__(self):
        return self.name

class Contact(models.Model):

    class ContactType(models.TextChoices):
        ALUNO = 'aluno', 'Aluno'
        EMPRESA = 'empresa', 'empresa'
    
    name = models.CharField(max_length=200, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=200, verbose_name="Telefone")
    contact_type = models.CharField(
        max_length=8,
        choices=ContactType.choices
    )
    
    class Meta:
        verbose_name_plural = "Pedidos de contato"
    
    def __str__(self):
        return f"{self.name} | {self.contact_type}"
    
class SelectionProcess(models.Model):
    title = models.CharField(
        max_length=200,
        default="Próximo Processo Seletivo",
        verbose_name="Título"
    )
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    
    class Meta:
        verbose_name = "Processo Seletivo"
        verbose_name_plural = "Processos Seletivos"
    
    def __str__(self):
        return self.title
    

class SelectionProcessStage(models.Model):
    process = models.ForeignKey(
        SelectionProcess, 
        on_delete=models.CASCADE, 
        related_name='stages', 
        verbose_name='Processo Seletivo'
        )
    label = models.CharField(max_length=200, verbose_name="Nome da etapa")
    date = models.CharField(max_length=200, verbose_name="Data/Período")
    order = models.IntegerField(default=0, verbose_name="Ordem")
    
    class Meta:
        verbose_name = "Data do Processo"
        verbose_name_plural = "Datas do Processo"
        ordering = ['order']
        
    def __str__(self):
        return f"{self.label} - {self.date}"

class SelectionProcessStep(models.Model):
    process = models.ForeignKey(
        SelectionProcess,
        on_delete=models.CASCADE, 
        related_name='steps', 
        verbose_name='Processo Seletivo'
    )
    number = models.CharField(max_length=10, verbose_name='Número')
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    image = models.ImageField(upload_to='process/steps/', null=True, blank=True, verbose_name='Ícone do quadrado')
    duration = models.CharField(max_length=100, blank=True, verbose_name='Duração')
    tips = models.TextField(blank=True, verbose_name='Dicas', help_text='Um tópico por linha.')
    order = models.IntegerField(default=0, verbose_name='Ordem')
    
    class Meta:
        verbose_name = 'Etapa Detalhada'
        verbose_name_plural = 'Etapas Detalhadas'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.number}. {self.title}"
    
    def get_tips_list(self):
        return [line.strip() for line in self.tips.splitlines() if line.strip()]


class SelectionProcessRequirement(models.Model):
    process = models.ForeignKey(SelectionProcess, on_delete=models.CASCADE, related_name='requirements', verbose_name='Processo Seletivo')
    text = models.CharField(max_length=300, verbose_name='Texto do requisito')
    icon = models.ImageField(upload_to='process/requirements/', null=True, blank=True, verbose_name='Ícone (imagem)')
    order = models.IntegerField(default=0, verbose_name='Ordem')

    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'
        ordering = ['order']
    
    def __str__(self):
        return self.text
    

class PreparationMaterial(models.Model):
    process = models.ForeignKey(
        SelectionProcess, 
        on_delete=models.CASCADE,
        related_name='materials',
        verbose_name='Processo Seletivo'
    )
    title = models.CharField(max_length=200, verbose_name='Título')
    order = models.IntegerField(default=0, verbose_name='Ordem')
    
    class Meta:
        verbose_name = 'Material de Preparação'
        verbose_name_plural = 'Materiais de Preparação'
        ordering = ['order']
    
    def __str__(self):
        return self.title


class PreparationMaterialItem(models.Model):
    """
    Item de um material de preparação.
    Ex: Victor Cheng - Case Interview Secrets
    """
    material = models.ForeignKey(
        PreparationMaterial,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Material'
    )
    text = models.CharField(max_length=300, verbose_name='Texto')
    order = models.IntegerField(default=0, verbose_name='Ordem')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['order']

    def __str__(self):
        return self.text