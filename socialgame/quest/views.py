# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from quest.models import get_player, get_quest_list, get_quest_progress_list, get_quest, accept_quest, get_quest_progress, advance_quest

# TODO.
# 仮にIDを固定とする
OSUSER_ID = u'1111'

def index(request):
    # 

    player = get_player(OSUSER_ID)
    quest_list = get_quest_list()
    quest_progress_list = get_quest_progress_list(player)

    ctxt = RequestContext(request,{
        'player': player, 
        'quest_list': quest_list,
        'quest_progress_list': quest_progress_list,
    })
    return render_to_response('quest/quest.html', ctxt)

def accept(request):

    if request.POST:
        quest_id = int(request.POST['quest'])
        quest = get_quest(quest_id)
        if quest:
            player = get_player(OSUSER_ID)
            accept_quest(player, quest)

    return HttpResponseRedirect(reverse('quest_index'))

def advance(request):

    if request.POST:
        quest_progress_id = int(request.POST['quest_progress'])
        quest_progress = get_quest_progress(quest_progress_id)
        if quest_progress:
            player = get_player(OSUSER_ID)
            advance_quest(player, quest_progress)

    return HttpResponseRedirect(reverse('quest_index'))

