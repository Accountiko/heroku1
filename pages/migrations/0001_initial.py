# Generated by Django 4.2.1 on 2023-05-11 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('card_titles', models.TextField(blank=True, help_text='use | for next line', null=True)),
                ('card_descriptions', models.TextField(blank=True, help_text='use | for next line', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('definition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('documents', models.TextField(help_text='use | for next line')),
            ],
        ),
        migrations.CreateModel(
            name='Eligibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('eligibilities', models.TextField(help_text='use | for next line')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('each questions', models.TextField(help_text='use | for next line')),
                ('each answers', models.TextField(help_text='use | for next line')),
            ],
        ),
        migrations.CreateModel(
            name='HowToRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('card_titles', models.TextField(help_text='use | for next line')),
                ('card_descriptions', models.TextField(help_text='use | for next line . must same line as card-title')),
            ],
        ),
        migrations.CreateModel(
            name='SplitFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('points', models.TextField(blank=True, help_text='use | for next line', null=True)),
                ('extras', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_description', models.TextField(help_text='use | for next line', max_length=255)),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='definitions', to='pages.definition')),
                ('documents_required', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.documentsrequired')),
                ('eligibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.eligibility')),
                ('extra_cards', models.ManyToManyField(blank=True, null=True, to='pages.cards')),
                ('extra_split_faces', models.ManyToManyField(blank=True, null=True, to='pages.splitface')),
                ('faq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.faq')),
                ('how_to_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.howtoregister')),
            ],
        ),
    ]