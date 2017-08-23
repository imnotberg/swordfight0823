from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class League(models.Model):
    league = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.league

class Season(models.Model):
    season = models.IntegerField()
    league = models.ForeignKey(League,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.season) + '-' + str(self.league)

class Team(models.Model):
    name = models.CharField(max_length = 200)
    league = models.ForeignKey(League,on_delete=models.CASCADE,null=True)
    conference = models.CharField(max_length = 200)
    division = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
class Week(models.Model):
    week = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.league) + "-" + str(self.season.season) + "-" + str(self.week)

class Game(models.Model):
    gameId = models.CharField(max_length=200, default='')
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    date = models.DateField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    roadTeam = models.ForeignKey(Team, null=True, related_name = 'roadTeam',on_delete=models.CASCADE)
    homeTeam = models.ForeignKey(Team, null=True, related_name = 'homeTeam',on_delete=models.CASCADE)
    roadScore = models.IntegerField(blank=True,null=True)
    homeScore = models.IntegerField(blank=True,null=True)
    roadFirstDowns = models.IntegerField(blank=True,null=True)
    roadTotalPlays = models.IntegerField(blank=True,null=True)
    roadTotalYards = models.IntegerField(blank=True,null=True)
    roadYardsPerPlay = models.DecimalField(decimal_places = 2, max_digits = 10,blank=True,null=True)
    roadPassingYards = models.IntegerField(blank=True,null=True)
    roadRushingYards = models.IntegerField(blank=True,null=True)
    roadRedZoneConversions = models.IntegerField(blank=True,null=True)
    roadRedZoneAttempts = models.IntegerField(blank=True,null=True,default=0)
    roadPenalty = models.IntegerField(blank=True,null=True)
    roadPenaltyYards = models.IntegerField(blank=True,null=True)
    roadTurnover = models.IntegerField(blank=True,null=True)
    roadDstTD = models.IntegerField(blank=True,null=True)
    roadPossession = models.IntegerField(blank=True,null=True)
    roadPassingFirstDowns = models.IntegerField(blank=True,null=True)
    roadRushingFirstDowns = models.IntegerField(blank=True,null=True)
    roadFirstDownsByPenalty = models.IntegerField(blank=True,null=True)
    roadThirdDownMade =models.IntegerField(blank=True,null=True)
    roadThirdDownAttempt = models.IntegerField(blank=True,null=True)
    roadFourthDownMade = models.IntegerField(blank=True,null=True)
    roadFourthDownAttempt = models.IntegerField(blank=True,null=True)
    roadPassComp = models.IntegerField(blank=True,null=True)
    roadPassAttempt = models.IntegerField(blank=True,null=True)
    roadInterceptionsThrown = models.IntegerField(blank=True,null=True)
    roadSacks = models.IntegerField(blank=True,null=True)
    roadYardsLost = models.IntegerField(blank=True,null=True)
    roadRushingAttempts = models.IntegerField(blank=True,null=True)
    roadYardsPerRush = models.DecimalField(decimal_places = 2, max_digits = 10,blank=True,null=True)
    roadFumblesLost= models.IntegerField(blank=True,null=True)
    homeFirstDowns = models.IntegerField(blank=True,null=True)
    homeTotalPlays = models.IntegerField(blank=True,null=True)
    homeTotalYards = models.IntegerField(blank=True,null=True)
    homeYardsPerPlay = models.DecimalField(decimal_places = 2, max_digits = 10,blank=True,null=True)
    homePassingYards = models.IntegerField(blank=True,null=True)
    homeRushingYards = models.IntegerField(blank=True,null=True)
    homeRedZoneConversions = models.IntegerField(blank=True,null=True)
    homeRedZoneAttempts = models.IntegerField(blank=True,null=True,default=0)
    homePenalty = models.IntegerField(blank=True,null=True)
    homePenaltyYards = models.IntegerField(blank=True,null=True)
    homeTurnover = models.IntegerField(blank=True,null=True)
    homeDstTD = models.IntegerField(blank=True,null=True)
    homePossession = models.IntegerField(blank=True,null=True)
    homePassingFirstDowns = models.IntegerField(blank=True,null=True)
    homeRushingFirstDowns = models.IntegerField(blank=True,null=True)
    homeFirstDownsByPenalty = models.IntegerField(blank=True,null=True)
    homeThirdDownMade = models.IntegerField(blank=True,null=True)
    homeThirdDownAttempt = models.IntegerField(blank=True,null=True)
    homeFourthDownMade = models.IntegerField(blank=True,null=True)
    homeFourthDownAttempt =models.IntegerField(blank=True,null=True)
    homePassComp = models.IntegerField(blank=True,null=True)
    homePassAttempt = models.IntegerField(blank=True,null=True)
    homeInterceptionsThrown = models.IntegerField(blank=True,null=True)
    homeSacks = models.IntegerField(blank=True,null=True)
    homeYardsLost = models.IntegerField(blank=True,null=True)
    homeRushingAttempts = models.IntegerField(blank=True,null=True)
    homeYardsPerRush = models.DecimalField(decimal_places = 2, max_digits = 10,blank=True,null=True)
    homeFumblesLost= models.IntegerField(blank=True,null=True)
    roadTeamWin = models.NullBooleanField()
    roadTeamLoss = models.NullBooleanField()
    roadTeamTie = models.NullBooleanField()
    homeTeamWin = models.NullBooleanField()
    homeTeamLoss = models.NullBooleanField()
    homeTeamTie = models.NullBooleanField()
    roadATSCover = models.NullBooleanField()
    roadATSLoss = models.NullBooleanField()
    roadATSPush = models.NullBooleanField()
    homeATSCover = models.NullBooleanField()
    homeATSLoss = models.NullBooleanField()
    homeATSPush = models.NullBooleanField()
    line = models.FloatField(null=True,blank=True)
    overall = models.NullBooleanField(default=True)
    datetime = models.DateTimeField(blank=True,null=True)

    
    
    def __str__(self):
        return str(self.id) + str(self.league) + '-' + str(self.season) + '-' + str(self.week) + '-' + str(self.roadTeam) + ' at ' + str(self.homeTeam)

class Conference(models.Model):
    name = models.CharField(max_length=250)
    division1 = models.CharField(max_length=250)
    division2 = models.CharField(max_length=250)
    division3 = models.CharField(max_length=250)
    division4 = models.CharField(max_length=250)
    


class Pick(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pick = models.ForeignKey(Team,on_delete=models.CASCADE)
    time = models.DateField(null=True,blank=True)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    win = models.NullBooleanField()
    loss = models.NullBooleanField()
    push = models.NullBooleanField()
    season = models.ForeignKey(Season,on_delete=models.CASCADE,null=True,blank=True,default='')
    week = models.ForeignKey(Week,on_delete=models.CASCADE,null=True,blank=True,default='')
    amount = models.IntegerField(null=True,blank=True)
    result = models.IntegerField(null=True,blank=True)
    datetime = models.DateTimeField(null=True,blank=True)    
    
    def __str__(self):
        return str(self.user) + str(self.game.week.week) + str(self.game) + str(self.pick)

class Comment(models.Model):
    pick = models.ForeignKey(Pick,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        
        return self.text