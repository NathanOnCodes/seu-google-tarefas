# Generated by Django 5.1.1 on 2024-10-26 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_remove_listatarefa_tarefa_listatarefa_tarefas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listatarefa',
            name='tarefas',
            field=models.ManyToManyField(to='tarefas.tarefa'),
        ),
    ]