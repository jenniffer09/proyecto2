from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.CharField(max_length=10, null=True),
        ),
    ]