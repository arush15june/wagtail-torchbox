# Generated by Django 2.2.12 on 2020-09-24 07:41

from django.db import migrations, models
import django.db.models.deletion
import headlesspreview.models
import modelcluster.fields
import tbx.core.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('torchbox', '0127_jobindexpage_intro'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('people', '0014_contactreasonslist_is_default_not_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('strapline', models.TextField(blank=True)),
                ('body', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', tbx.core.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))], label='Aligned image')), ('wide_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())], label='Wide image')), ('bustout', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock())])), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code'))], blank=True)),
                ('post_registration_body', wagtail.core.fields.StreamField([('h2', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.core.blocks.CharBlock(classname='title', icon='title')), ('intro', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('aligned_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('alignment', tbx.core.blocks.ImageFormatChoiceBlock()), ('caption', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))], label='Aligned image')), ('wide_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock())], label='Wide image')), ('bustout', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.RichTextBlock())])), ('pullquote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock(classname='quote title')), ('attribution', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(icon='code', label='Raw HTML')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code'))], blank=True)),
                ('event_type', wagtail.core.fields.StreamField([('zoom_meeting', wagtail.core.blocks.StructBlock([('meeting_ID', wagtail.core.blocks.CharBlock())])), ('zoom_webinar', wagtail.core.blocks.StructBlock([('meeting_ID', wagtail.core.blocks.CharBlock())]))], blank=True)),
                ('feed_image', models.ForeignKey(blank=True, help_text='Image used on listings and social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='torchbox.TorchboxImage')),
            ],
            options={
                'abstract': False,
            },
            bases=(headlesspreview.models.HeadlessPreviewMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='EventsPageHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='events.EventsPage')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='people.Author')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
