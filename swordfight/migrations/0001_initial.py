# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('division1', models.CharField(max_length=250)),
                ('division2', models.CharField(max_length=250)),
                ('division3', models.CharField(max_length=250)),
                ('division4', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameId', models.CharField(default='', max_length=200)),
                ('date', models.DateField()),
                ('roadScore', models.IntegerField(blank=True, null=True)),
                ('homeScore', models.IntegerField(blank=True, null=True)),
                ('roadFirstDowns', models.IntegerField(blank=True, null=True)),
                ('roadTotalPlays', models.IntegerField(blank=True, null=True)),
                ('roadTotalYards', models.IntegerField(blank=True, null=True)),
                ('roadYardsPerPlay', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('roadPassingYards', models.IntegerField(blank=True, null=True)),
                ('roadRushingYards', models.IntegerField(blank=True, null=True)),
                ('roadRedZoneConversions', models.IntegerField(blank=True, null=True)),
                ('roadRedZoneAttempts', models.IntegerField(blank=True, default=0, null=True)),
                ('roadPenalty', models.IntegerField(blank=True, null=True)),
                ('roadPenaltyYards', models.IntegerField(blank=True, null=True)),
                ('roadTurnover', models.IntegerField(blank=True, null=True)),
                ('roadDstTD', models.IntegerField(blank=True, null=True)),
                ('roadPossession', models.IntegerField(blank=True, null=True)),
                ('roadPassingFirstDowns', models.IntegerField(blank=True, null=True)),
                ('roadRushingFirstDowns', models.IntegerField(blank=True, null=True)),
                ('roadFirstDownsByPenalty', models.IntegerField(blank=True, null=True)),
                ('roadThirdDownMade', models.IntegerField(blank=True, null=True)),
                ('roadThirdDownAttempt', models.IntegerField(blank=True, null=True)),
                ('roadFourthDownMade', models.IntegerField(blank=True, null=True)),
                ('roadFourthDownAttempt', models.IntegerField(blank=True, null=True)),
                ('roadPassComp', models.IntegerField(blank=True, null=True)),
                ('roadPassAttempt', models.IntegerField(blank=True, null=True)),
                ('roadInterceptionsThrown', models.IntegerField(blank=True, null=True)),
                ('roadSacks', models.IntegerField(blank=True, null=True)),
                ('roadYardsLost', models.IntegerField(blank=True, null=True)),
                ('roadRushingAttempts', models.IntegerField(blank=True, null=True)),
                ('roadYardsPerRush', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('roadFumblesLost', models.IntegerField(blank=True, null=True)),
                ('homeFirstDowns', models.IntegerField(blank=True, null=True)),
                ('homeTotalPlays', models.IntegerField(blank=True, null=True)),
                ('homeTotalYards', models.IntegerField(blank=True, null=True)),
                ('homeYardsPerPlay', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('homePassingYards', models.IntegerField(blank=True, null=True)),
                ('homeRushingYards', models.IntegerField(blank=True, null=True)),
                ('homeRedZoneConversions', models.IntegerField(blank=True, null=True)),
                ('homeRedZoneAttempts', models.IntegerField(blank=True, default=0, null=True)),
                ('homePenalty', models.IntegerField(blank=True, null=True)),
                ('homePenaltyYards', models.IntegerField(blank=True, null=True)),
                ('homeTurnover', models.IntegerField(blank=True, null=True)),
                ('homeDstTD', models.IntegerField(blank=True, null=True)),
                ('homePossession', models.IntegerField(blank=True, null=True)),
                ('homePassingFirstDowns', models.IntegerField(blank=True, null=True)),
                ('homeRushingFirstDowns', models.IntegerField(blank=True, null=True)),
                ('homeFirstDownsByPenalty', models.IntegerField(blank=True, null=True)),
                ('homeThirdDownMade', models.IntegerField(blank=True, null=True)),
                ('homeThirdDownAttempt', models.IntegerField(blank=True, null=True)),
                ('homeFourthDownMade', models.IntegerField(blank=True, null=True)),
                ('homeFourthDownAttempt', models.IntegerField(blank=True, null=True)),
                ('homePassComp', models.IntegerField(blank=True, null=True)),
                ('homePassAttempt', models.IntegerField(blank=True, null=True)),
                ('homeInterceptionsThrown', models.IntegerField(blank=True, null=True)),
                ('homeSacks', models.IntegerField(blank=True, null=True)),
                ('homeYardsLost', models.IntegerField(blank=True, null=True)),
                ('homeRushingAttempts', models.IntegerField(blank=True, null=True)),
                ('homeYardsPerRush', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('homeFumblesLost', models.IntegerField(blank=True, null=True)),
                ('roadTeamWin', models.NullBooleanField()),
                ('roadTeamLoss', models.NullBooleanField()),
                ('roadTeamTie', models.NullBooleanField()),
                ('homeTeamWin', models.NullBooleanField()),
                ('homeTeamLoss', models.NullBooleanField()),
                ('homeTeamTie', models.NullBooleanField()),
                ('roadATSCover', models.NullBooleanField()),
                ('roadATSLoss', models.NullBooleanField()),
                ('roadATSPush', models.NullBooleanField()),
                ('homeATSCover', models.NullBooleanField()),
                ('homeATSLoss', models.NullBooleanField()),
                ('homeATSPush', models.NullBooleanField()),
                ('line', models.FloatField(blank=True, null=True)),
                ('overall', models.NullBooleanField(default=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(blank=True, null=True)),
                ('win', models.NullBooleanField()),
                ('loss', models.NullBooleanField()),
                ('push', models.NullBooleanField()),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.League')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('conference', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=200)),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='swordfight.League')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.League')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.Season')),
            ],
        ),
        migrations.AddField(
            model_name='pick',
            name='pick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.Team'),
        ),
        migrations.AddField(
            model_name='pick',
            name='season',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='swordfight.Season'),
        ),
        migrations.AddField(
            model_name='pick',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pick',
            name='week',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='swordfight.Week'),
        ),
        migrations.AddField(
            model_name='game',
            name='homeTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homeTeam', to='swordfight.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.League'),
        ),
        migrations.AddField(
            model_name='game',
            name='roadTeam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roadTeam', to='swordfight.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.Season'),
        ),
        migrations.AddField(
            model_name='game',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.Week'),
        ),
        migrations.AddField(
            model_name='comment',
            name='pick',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swordfight.Pick'),
        ),
    ]