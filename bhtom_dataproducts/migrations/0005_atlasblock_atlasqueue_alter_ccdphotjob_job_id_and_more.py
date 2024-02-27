# Generated by Django 4.0.4 on 2024-01-29 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bhtom_targets', '0002_alter_target_cadence_priority_and_more'),
        ('bhtom_dataproducts', '0004_alter_dataproduct_data_alter_dataproduct_fits_data_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtlasBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_block', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('wait_time', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AtlasQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_url', models.URLField(blank=True, default=None, null=True)),
                ('result_url', models.URLField(blank=True, db_index=True, default=None, null=True)),
                ('mjd_min', models.FloatField(default=0)),
                ('create_task', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('insert_row', models.IntegerField(default=0, null=True)),
                ('status', models.CharField(choices=[('C', 'CREATED'), ('P', 'IN PROGRESS'), ('S', 'SUCCESS'), ('E', 'ERROR'), ('T', 'THROTTLED')], default='C', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='ccdphotjob',
            name='job_id',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
        migrations.AddConstraint(
            model_name='ccdphotjob',
            constraint=models.UniqueConstraint(fields=('job_id',), name='unique_job_id'),
        ),
        migrations.AddField(
            model_name='atlasqueue',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bhtom_targets.target'),
        ),
        migrations.AddField(
            model_name='atlasblock',
            name='atlas_queue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bhtom_dataproducts.atlasqueue'),
        ),
        migrations.AlterUniqueTogether(
            name='atlasqueue',
            unique_together={('target', 'task_url')},
        ),
    ]