from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0002_exchangeprogram'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            INSERT INTO faculty_exchangeprogram (university, languages, places, deadline, description) VALUES
            ('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', 'Один з найкращих університетів Польщі.'),
            ('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01', 'Найстаріший католицький університет Європи.'),
            ('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', 'Провідний заклад вищої освіти Литви.'),
            ('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', 'Старовинний університет у Кракові.'),
            ('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', 'Національний університет Естонії.'),
            ('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', 'Другий за величиною університет Чехії.');
            """,
            reverse_sql="DELETE FROM faculty_exchangeprogram;"
        )
    ]