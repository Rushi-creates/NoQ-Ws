# Generated by Django 4.0.3 on 2022-06-14 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_queue_acc_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='acc_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queue_uid', to='core.authuser'),
        ),
        migrations.AlterField(
            model_name='queueuser',
            name='q_uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queueUser_uid', to='core.queue'),
        ),
    ]