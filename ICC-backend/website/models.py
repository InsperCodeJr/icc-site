from django.db import models


class Partner_Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categorias dos Parceiros'

    def __str__(self):
        return self.title


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
    category = models.ForeignKey(Partner_Category, on_delete=models.PROTECT, null=True)
    contato = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Parceiros'

    def __str__(self):
        return self.name


class Project(models.Model):
    '''
    Modelo de Projetos de Consultoria:
    Título, Descrição, Parceiros envolvidos, Data de início e fim
    '''
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    partners = models.ManyToManyField(
        Partner,
        blank=True,
        verbose_name='Parceiros envolvidos',
        related_name='projects'
    )
    start_date = models.DateField(verbose_name='Data de início')
    end_date = models.DateField(null=True, blank=True, verbose_name='Data de conclusão')

    class Meta:
        verbose_name_plural = 'Projetos'
        ordering = ['-start_date']

    def __str__(self):
        return self.title


class Team_Member(models.Model):
    name = models.CharField(max_length=200)
    photo_url = models.ImageField(upload_to='team/', null=True, blank=True)
    biography = models.TextField(max_length=200)
    position = models.ForeignKey(Member_Position, on_delete=models.PROTECT, null=True)
    hours = models.IntegerField()
    entry_date = models.DateField()
    exit_date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    linkedin = models.URLField(null=True, blank=True, verbose_name='LinkedIn')
    projects = models.ManyToManyField(
        Project,
        blank=True,
        verbose_name='Projetos participados',
        related_name='members'
    )

    class Meta:
        verbose_name_plural = 'Membros do Time'

    def __str__(self):
        return self.name

    @property
    def number_of_projects(self):
        return self.projects.count()


class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    responsible_partner = models.ForeignKey(Partner, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.title


class Media(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()

    class Meta:
        verbose_name_plural = 'Notícias'

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

    