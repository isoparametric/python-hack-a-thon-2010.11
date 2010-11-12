# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Player(models.Model):
    '''
    ソーシャルゲームプレイヤ（本来はここに置くべきではない）
    '''
    
    name = models.CharField(u'名前', max_length=32)
    level = models.IntegerField(u'レベル', default=1)
    experience = models.IntegerField(u'現在経験値', default=0)
    max_action_point = models.IntegerField(u'最大行動ポイント', default=10)
    action_point = models.IntegerField(u'行動ポイント', default=10)

class Quest(models.Model):
    '''
    ソーシャルゲームのクエスト的な何か
    '''

    name = models.CharField(u'クエスト名', max_length=32)
    description = models.TextField(u'概要', max_length=1024)
    action_point = models.IntegerField(u'消費アクションポイント')
    experience = models.IntegerField(u'得られる経験値')
    lower_progress = models.IntegerField(u'最低限増える進捗度')
    upper_progress = models.IntegerField(u'最高で増える進捗度')
    
    def __unicode__(self):
        '''
        モデルの文字列表現
        '''
        return u'%s' % (self.name)

    class Meta:
        # ソート順
        ordering = ('id',)
        # 単数形
        verbose_name = u'クエスト'
        # 複数形
        verbose_name_plural = verbose_name

class QuestProgress(models.Model):
    '''
    ソーシャルアプリのユーザ毎の達成度
    '''
    
    player = models.ForeignKey(Player) # 対応したプレイヤ
    quest = models.ForeignKey(Quest) # 対応したクエスト
    progress = models.IntegerField(u'達成度', default=0)

    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now=True)

    def __unicode__(self):
        '''
        モデルの文字列表現
        '''
        return u'%sの達成度:%d' % (self.quest.name, self.progress)

    class Meta:
        # ソート順
        ordering = ('-created_at',)
        # 単数形
        verbose_name = u'クエスト達成度'
        # 複数形
        verbose_name_plural = verbose_name

def get_player(name):
    '''
    指定された名前のプレイヤを取得（本来は一意のものから取得しなければ不正）
    '''
    player, is_new = Player.objects.get_or_create(name=name)

    return player

def get_quest_list():
    '''
    全てのクエストを取得
    '''
    return Quest.objects.all()

def get_quest(quest_id):
    '''
    指定クエストを取得
    '''
    return Quest.objects.get(id=quest_id)

def accept_quest(player, quest):
    '''
    指定クエストを受理
    '''
    try:
        QuestProgress.objects.get(player=player, quest=quest)
    except QuestProgress.DoesNotExist:
        quest_progress = QuestProgress(player=player, quest=quest)
        quest_progress.save()


def get_quest_progress_list(player):
    '''
    全てのクエストの進捗状況を取得
    '''
    return QuestProgress.objects.filter(player=player)

def get_quest_progress(quest_progress_id):
    '''
    指定クエスト進行を取得
    '''
    return QuestProgress.objects.get(id=quest_progress_id)

def advance_quest(player, quest_progress):
    '''
    指定クエストを進行
    '''
    if quest_progress.player == player:
        if quest_progress.progress < 100:
            from random import randint
            progress = randint(quest_progress.quest.lower_progress, quest_progress.quest.upper_progress)
            quest_progress.progress += progress
            if quest_progress.progress > 100:
                quest_progress.progress = 100
            quest_progress.save()

