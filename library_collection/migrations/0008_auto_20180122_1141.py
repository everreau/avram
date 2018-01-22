# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_collection', '0007_auto_20171218_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='disqus_shortname_prod',
            field=models.CharField(help_text=b'put disqus on production with this shortcode (from disqus admin)', max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='disqus_shortname_test',
            field=models.CharField(help_text=b'put disqus on test with this shortcode', max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='harvest_type',
            field=models.CharField(default=b'X', max_length=3, choices=[(b'X', b'None'), (b'OAC', b'Legacy OAC'), (b'OAI', b'OAI-PMH'), (b'SLR', b'Solr Index'), (b'MRC', b'MARC21'), (b'NUX', b'Shared DAMS'), (b'ALX', b'Aleph MARC XML'), (b'SFX', b'UCSF XML Search Results (tobacco)'), (b'UCB', b'Solr Generic - cursorMark'), (b'PRE', b'Preservica CMIS Atom Feed'), (b'FLK', b'Flickr Api All Public Photos'), (b'YTB', b'YouTube Api - Playlist Videos'), (b'XML', b'XML File'), (b'EMS', b'eMuseum API')]),
        ),
    ]
