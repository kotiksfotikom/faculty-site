from django.db import migrations

def clean_places_text(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        digits = ''.join(filter(str.isdigit, str(program.places)))
        program.places = digits if digits else '0'
        program.save()

def reverse_clean(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('faculty', '0005_auto_20261006_1858'),
    ]
    operations = [
        migrations.RunPython(clean_places_text, reverse_code=reverse_clean),
    ]
