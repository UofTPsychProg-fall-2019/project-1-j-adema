import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, data, event, gui, logging
from psychopy.hardware import keyboard
import random

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

expName = 'Project 1'
expInfo = {'Participant':'', 'session':'psy1210'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False,title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()

win = visual.Window(size=(1600,1068),fullscr=True, winType='pyglet', monitor='testMonitor', allowGUI=False,color=[0,0,0], units='height')
win.recordFrameIntervals=True
win.refreshThreshold = 1/60 + 0.004
logging.console.setLevel(logging.WARNING)
event.globalKeys.add(key='escape',func=core.quit)

defaultKeyboard = keyboard.Keyboard()

cols=['participant','cond_file','img','prev_type',
    'basic','rt','resp','acc']

condition = ['1','2','3','4']
condition = random.sample(condition,1)
expInfo['condition'] = condition

Participant = expInfo['Participant']
Session = expInfo['session']
logFile = 'data/log'+ Participant
outputFileName = logFile

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=False, saveWideText=True,
    dataFileName=outputFileName)

expClock = core.Clock()
trialClock = core.Clock()
imgClock = core.Clock()
fixClock = core.Clock()
prevClock = core.Clock()
fbClock = core.Clock()

instruction1 = visual.TextStim(win=win, name='instruct',
    text='You will be presented with various images. Within each image, there is a target:'
    '\n\n\n\nYour task is to find the target as quickly as possible.\nPress any key to continue.',
    font='Arial',
    pos=(0,0), height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
inst_k = visual.ImageStim(
    win=win,
    name='inst_m',
    image='targ_li.png', mask=None,
    ori=0, pos=(4,-0.5), units = 'cm', size=(6, 6),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
inst_l = visual.ImageStim(
    win=win,
    name='inst_z',
    image='targ_ka.png', mask=None,
    ori=0, pos=(-4,-0.5), units = 'cm', size=(6, 6),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
instruction1.draw()
inst_k.draw()
inst_l.draw()
win.flip()
event.clearEvents()
i_1 = event.waitKeys(keyList=None)
win.flip()
instruction2 = visual.TextStim(win=win, name='instruct2',
    text='1. Stare at the cross onscreen.\n2. A preview will be presented briefly.'
    '\n 3. You will be able to freely search the image for the target.'
    ' Find the target as quickly as possible. Press the "K" key if you see the kangaroo target.'
    ' Press the "L" key if you see the lizard target.\nPress any key to continue.',
    font='Arial',
    pos=(0,0), height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
instruction2.draw()
win.flip()
event.clearEvents()
i_2 = event.waitKeys(keyList=None)
win.flip()
instruction3 = visual.TextStim(win=win, name='instruct4',
    text='It will be difficult to see the target at first. That is okay! Try your best to be as fast as possible, and keep going!'
    '\n\n Press any key to continue.',
    font='Arial',
    pos=(0,0), height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
instruction3.draw()
win.flip()
event.clearEvents()
i_3 = event.waitKeys(keyList=None)
win.flip()
instruction4 = visual.TextStim(win=win, name='instruct3',
    text='To begin the experiment, place your index finger on the "K" key.'
    ' Place your middle finger on the "L" key. Stare at the cross.'
    '\n\n\n\n\n\nPress "K" or "L" to begin.',
    font='Arial',
    pos=(0,0), height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
inst_cross = visual.ShapeStim(
    win=win, name='inst_cross', vertices='cross',
    units = 'cm', size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
instruction4.draw()
inst_cross.draw()
win.flip()
event.clearEvents()
i_4 = event.waitKeys(keyList=['l','k'])
win.flip()
event.clearEvents()

fixate = visual.ShapeStim(
    win=win, name='fixate', vertices='cross',
    units = 'cm', size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
preview = visual.ImageStim(
    win=win,
    name='sneak_peek',
    image='sin', mask=None,
    ori=0, pos=(0, 0), units = 'pix', size=(1600, 1067),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
search = visual.ImageStim(
    win=win,
    name='seek',
    image='sin', mask=None,
    ori=0, pos=(0, 0), units = 'pix', size=(1600, 1067),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
prompt = visual.TextStim(win=win, name='promt',
    text="Time's up! Please respond more quickly. \nPress any key to continue.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
ready = visual.TextStim(win=win, name='text',
    text="Ready to start the next trial?",
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0)
pause_text = visual.TextStim(win=win, name='pause_text',
    text="Take a moment's rest. When you're ready, put your index finger on 'K'. Put your middle finger on 'L'.\n\n\n\n\n\nPress 'K' or 'L' to resume.",
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0)

trials = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond_'+condition[0]+'.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)
thisTrial = trials.trialList[0]
if thisTrial != None:
    for paramName in thisTrial:
        exec('{}=thisTrial[paramName]'.format(paramName))
for thisTrial in trials:
    currentLoop = trials
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{}=thisTrial[paramName]'.format(paramName))

    target = visual.ImageStim(
    win=win,
    name='target',
    image='sin', mask=None,
    ori=0, pos=(targ_x,targ_y), size=(0.03, 0.02),
    color=[1,1,1], colorSpace='rgb', opacity=(0.5),
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

    keys = []
    preview.setImage(prev)
    search.setImage(img)
    target.setImage(targ)
    fixate.draw()
    win.flip()
    core.wait(0.5)
    event.clearEvents()
    fixClock.reset()
    preview.draw()
    fixate.draw()
    win.flip()
    core.wait(0.160)
    event.clearEvents()
    prevClock.reset()
    win.flip()
    event.clearEvents()
    fixate.draw()
    win.flip()
    core.wait(0.5)
    event.clearEvents()
    fixClock.reset()
    event.clearEvents()
    imgClock.reset()
    while len(keys)==0 and imgClock.getTime()<10:
        search.draw()
        target.draw()
        win.flip()
        keys = event.getKeys(keyList=['l','k'],timeStamped=imgClock)
    if imgClock.getTime()>10:
        search.draw()
        target.draw()
        prompt.draw()
        win.flip()
        keys = event.waitKeys(keyList=None,timeStamped=imgClock)
    if keys[0][0]==correct:
        trials.addData('acc',1)
    else:
        trials.addData('acc',0)

    trials.addData('resp', keys[0][0])
    trials.addData('rt', keys[0][1])
    #out.loc[thisTrial, 'trial']=thisTrial
    #out.loc[thisTrial,'img'] = img
    #out.loc[thisTrial,'preview'] = preview
    #out.loc[thisTrial,'prev_type'] = prev_type
    #out.loc[thisTrial,'basic'] = basic
    #out.loc[thisTrial,'resp'] = keys[0][0]
    #out.loc[thisTrial,'rt'] = keys[0][1]
    #out.loc[[thisTrial]].to_csv(filename,mode='a',header=False,index=False)
    win.flip()
    event.clearEvents()
    if trials.thisN == 9:
        pause_text.draw()
        fixate.draw()
        win.flip()
        event.clearEvents()
        pause_key = event.waitKeys(keyList=['l','k'])
    else:
        ready.draw()
        fixate.draw()
        win.flip()
        event.clearEvents()
        ready_key = event.waitKeys(keyList=['l','k'])
    thisExp.nextEntry()
win.flip()

finish_text = visual.TextStim(win=win, name='pause_text',
    text="Thank you for completing the study! Press any key to exit the experiment.",
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0)
finish_text.draw()
win.flip()
event.clearEvents()
end_key = event.waitKeys(keyList=None)
win.flip()
win.close()
core.quit()
