from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtto', '0002_alter_empleado_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]