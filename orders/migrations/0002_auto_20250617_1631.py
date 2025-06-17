from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='platba',
            field=models.CharField(
                max_length=50,
                choices=[
                    ('uhradena', 'Uhradená'),
                    ('cakajuca na platbu', 'Čakajúca na platbu'),
                ],
                default='cakajuca na platbu',
            ),
        ),
    ]
