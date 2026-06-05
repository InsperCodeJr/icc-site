from datetime import date
from django.core.management.base import BaseCommand
from website.models import Member_Position, Team_Member

MEMBROS = [
    {
        "nome": "Gabriel Ávila Campos Canaan",
        "data_entrada": "2026-01-01",
        "foto": "https://drive.google.com/open?id=1uk6dM3tt4X42znQtcHHftABZoMs3OKnC",
        "cargo_atual": "Trainee",
        "descricao": "Entrou como trainee, iniciando sua trajetória com foco em aprendizado e crescimento contínuo.",
    },
    {
        "nome": "Luiz Alberto Bordignon Rodrigues da Silva",
        "data_entrada": "2025-07-01",
        "foto": "https://drive.google.com/open?id=1VUbdLqDrROVCqvqJTtrHlPxLtoTs_rfx",
        "cargo_atual": "Mentor",
        "descricao": "Integrou o grupo campeão do Trainee 2025.2 e assumiu o papel de mentor em 2026.1, contribuindo com a formação dos novos membros.",
    },
    {
        "nome": "Sofia Tomazella da Rocha",
        "data_entrada": "2025-07-01",
        "foto": "https://drive.google.com/open?id=1urV5zvZLQHxUqy_NrbhJMicsCud4PRD-",
        "cargo_atual": "Diretoria de Marketing",
        "descricao": "Membro da Diretoria de Marketing desde 2026.1, com participação no Challenge da LEK e atuação no projeto Social Planning do GAS.",
    },
    {
        "nome": "Anderson Benjamim dos Santos",
        "data_entrada": "2023-07-01",
        "foto": "https://drive.google.com/open?id=1Nfr9TnRqk7zeuwxafbLmv-kbnOfKdkpE",
        "cargo_atual": "Diretor Escola de Mentores",
        "descricao": "Bicampeão do Trainee ICC e 3º lugar no Interclubes 2025. Ex-membro de Relações Institucionais, mentor em 2025 e atual Diretor da Escola de Mentores.",
    },
    {
        "nome": "Gabriel Carvalho Silva",
        "data_entrada": "2025-07-01",
        "foto": "https://drive.google.com/open?id=1vV60UwYBPFzaJo38riTDOhK7XfNI7Ejb",
        "cargo_atual": "Diretor de Marketing",
        "descricao": "Campeão do Trainee ICC em 2025.2 e atual Diretor de Marketing, onde lidera as iniciativas de comunicação e posicionamento do clube.",
    },
    {
        "nome": "Enrico Simões Pietro",
        "data_entrada": "2025-01-01",
        "foto": "https://drive.google.com/open?id=16CBuH6YBVlsPeg4BDISNe6_PXQhWK7sB",
        "cargo_atual": "Presidente",
        "descricao": "Ingressou no ICC em 2025.1 e ascendeu à Presidência ainda no mesmo semestre, acumulando 3º lugar no InterClubs à frente da organização.",
    },
    {
        "nome": "Manoel Wilson Do Nascimento Neto",
        "data_entrada": "2025-01-01",
        "foto": "https://drive.google.com/open?id=1ufJVIoKGtFrAZWi1cwq0m-Ln3bOhk4aE",
        "cargo_atual": "Mentor",
        "descricao": "Trainee em 2025.1, evoluiu para mentor nos semestres seguintes. Participou do Interclubs e conquistou o 1º lugar no ON.",
    },
    {
        "nome": "Letícia da Silva Aznar",
        "data_entrada": "2025-07-01",
        "foto": "https://drive.google.com/open?id=1Hg05AYycGiGsE6Z9LGKNg5jmSPkceX0u",
        "cargo_atual": "Diretora de Recursos Humanos",
        "descricao": "Atual Diretora de Recursos Humanos, com participação no Challenge da LEK 2026.1 e trajetória iniciada como trainee em 2025.1.",
    },
    {
        "nome": "Pedro Araújo Marinho da Silva",
        "data_entrada": "2025-07-01",
        "foto": "https://drive.google.com/open?id=1-wPq2YaHcxq1GgZz1y9ccSfdvWZ-4NfA",
        "cargo_atual": "Membro",
        "descricao": "Ingressou no ICC em 2025.2 como trainee e atua atualmente como membro da equipe.",
    },
    {
        "nome": "Fabrizio Antonini Ripoli",
        "data_entrada": "2022-07-01",
        "foto": "https://drive.google.com/open?id=1zfXBKvCPMy2fpkK9Ij7G1sKIKQ3Bww3r",
        "cargo_atual": "Mentor",
        "descricao": "Membro do ICC desde 2022.2, participou do challenge de 2025.2 e atua como mentor em 2026.1, apoiando o desenvolvimento dos novos integrantes.",
    },
    {
        "nome": "Ana Beatriz Da Cunha",
        "data_entrada": "2026-01-01",
        "foto": "https://drive.google.com/open?id=1tGlemjaQRTN1sbl1M6gAqyatNTAIoAND",
        "cargo_atual": "Trainee",
        "descricao": "Entrou como trainee, iniciando sua trajetória com foco em aprendizado e crescimento contínuo.",
    },
    {
        "nome": "Alexandre Gabriel Gomes Rangel",
        "data_entrada": "2026-01-01",
        "foto": "https://drive.google.com/open?id=1udIymkWSJ-6bRkfFktaww0OoNHZMZXK3",
        "cargo_atual": "Membro",
        "descricao": "Ingressou no ICC em 2026.1 como membro, dando seus primeiros passos na consultoria universitária.",
    },
    {
        "nome": "Ana Luísa Farinha",
        "data_entrada": "2025-01-01",
        "foto": "https://drive.google.com/open?id=1c1boJzuUV2FHt5K_WDO2P9ZJjIswHN1R",
        "cargo_atual": "Vice-presidente",
        "descricao": "Atual Vice-presidente do ICC, com passagem pela Diretoria de RH e participações no Challenge do Trainee e no Challenge da LEK.",
    },
    {
        "nome": "Carlos Eduardo Carvalho Vidal",
        "data_entrada": "2026-01-01",
        "foto": "https://drive.google.com/open?id=1aJsCvhXcHp5L0us1iAzxK7Bm6NRTcc9M",
        "cargo_atual": "Trainee",
        "descricao": "Entrou como trainee, iniciando sua trajetória com foco em aprendizado e crescimento contínuo.",
    },
]

POWER_MAP = {
    "presidente": 0,
    "vice-presidente": 1,
    "diretor": 2,
    "diretora": 2,
    "diretoria": 2,
    "mentor": 3,
    "membro": 4,
    "trainee": 5,
}


def _power_for(cargo: str) -> int:
    cargo_lower = cargo.lower()
    for keyword, power in POWER_MAP.items():
        if keyword in cargo_lower:
            return power
    return 3


class Command(BaseCommand):
    help = "Importa os membros do ICC a partir dos dados do membros_icc.sql"

    def add_arguments(self, parser):
        parser.add_argument(
            "--limpar",
            action="store_true",
            help="Remove todos os membros e cargos existentes antes de importar.",
        )

    def handle(self, *args, **options):
        if options["limpar"]:
            Team_Member.objects.all().delete()
            Member_Position.objects.all().delete()
            self.stdout.write("Membros e cargos removidos.")

        self.stdout.write("Criando cargos...")
        cargos_unicos = {m["cargo_atual"] for m in MEMBROS}
        posicoes = {}
        for cargo in cargos_unicos:
            pos, created = Member_Position.objects.get_or_create(
                title=cargo,
                defaults={"power": _power_for(cargo)},
            )
            posicoes[cargo] = pos
            status = "criado" if created else "já existia"
            self.stdout.write(f"  '{cargo}' ({status})")

        self.stdout.write("Importando membros...")
        criados = 0
        ignorados = 0
        for m in MEMBROS:
            ano, mes, dia = m["data_entrada"].split("-")
            _, created = Team_Member.objects.get_or_create(
                name=m["nome"],
                defaults={
                    "photo_url": m["foto"],
                    "biography": m["descricao"],
                    "position": posicoes[m["cargo_atual"]],
                    "entry_date": date(int(ano), int(mes), int(dia)),
                    "hours": None,
                },
            )
            if created:
                criados += 1
                self.stdout.write(f"  + {m['nome']}")
            else:
                ignorados += 1
                self.stdout.write(f"  ~ {m['nome']} (já existia, ignorado)")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nConcluído: {criados} criados, {ignorados} ignorados."
            )
        )
