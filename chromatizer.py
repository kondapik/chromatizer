"""
Title              : Chromatizer
Description        : The Color of Music
Author             : Kondapi Prasanth
Created            : 09-Jul-2022
Modified           : 14-Jul-2022
Version            : 0
Revision History   : 0

"""
windowIcon = b'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'
signatureImage=b'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'
splashImage = r'G:\\design\\chromaticArduino\\chromatizer.png'

import PySimpleGUI as sg

splashWindow = sg.Window('splash', [[sg.Image(source=splashImage,
    background_color = None,
    size = (400, 400),
    s = (None, None),
    pad = None,
    p = None,
    key = None,
    k = None,
    tooltip = None,
    subsample = None,
    right_click_menu = None,
    expand_x = False,
    expand_y = False,
    visible = True,
    enable_events = False,
    metadata = None)]], no_titlebar=True, grab_anywhere=True, disable_close=True, margins=(0,0), element_padding=0, transparent_color=sg.theme_background_color(), icon=windowIcon, finalize=True)
splashWindow.Refresh()

import sys, pathlib, numpy as np, pyaudio, librosa, matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter1d
from math import ceil
from time import time, sleep
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

debugOn = True
colorMap = {'W':'white', 'K':'black', 'R':'red', 'G':'green', 'B':'blue', 'C':'cyan', 'Y':'yellow', 'M':'magenta', 'S':'#C0C0C0', 'D':'#808080'}


def getPrefFile() -> pathlib.Path:
    """
    Returns a parent directory path
    where persistent application data can be stored.

    linux: ~/.local/share
    macOS: ~/Library/Application Support
    windows: C:/Users/<USER>/AppData/Roaming
    """

    filePath = pathlib.Path.home()

    if sys.platform == "win32":
        filePath = filePath / "AppData/Roaming"
    elif sys.platform == "linux":
        filePath = filePath / ".local/share"
    elif sys.platform == "darwin":
        filePath = filePath / "Library/Application Support"
    
    return filePath / "chromatizer/preferences.json"

def debugPrint(*args):
    if debugOn:
        print(*args)
        print('\n')

def getPrefName(text):
    return sg.T(text, size=(18,1), justification='left')

def interpolate(y, new_length):
    """Intelligently resizes the array by linearly interpolating the values

    Parameters
    ----------
    y : np.array
        Array that should be resized

    new_length : int
        The length of the new interpolated array

    Returns
    -------
    z : np.array
        New array with length of new_length that contains the interpolated
        values of y.
    """
    if len(y) == new_length:
        return y
    x_old = np.linspace(0, 1, len(y))
    x_new = np.linspace(0, 1, new_length)
    return np.interp(x_new, x_old, y)

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def getClosestIndex(array, searchTarget):
    return min(enumerate(array), key=lambda x: abs(searchTarget - x[1])) 
class expFilter:
    """Simple exponential smoothing filter"""
    def __init__(self, val=0.0, alpha_decay=0.5, alpha_rise=0.5):
        """Small rise / decay factors = more smoothing"""
        assert 0.0 < alpha_decay < 1.0, 'Invalid decay smoothing factor'
        assert 0.0 < alpha_rise < 1.0, 'Invalid rise smoothing factor'
        self.alpha_decay = alpha_decay
        self.alpha_rise = alpha_rise
        self.value = val

    def update(self, value):
        if isinstance(self.value, (list, np.ndarray, tuple)):
            alpha = value - self.value
            alpha[alpha > 0.0] = self.alpha_rise
            alpha[alpha <= 0.0] = self.alpha_decay
        else:
            alpha = self.alpha_rise if value > self.value else self.alpha_decay
        self.value = alpha * value + (1.0 - alpha) * self.value
        return self.value
    
    def updateDecay(self, value):
        self.alpha_decay = value

def getCloser(array, searchItem):
    absolute_val_array = np.abs(array - searchItem)
    smallest_difference_index = absolute_val_array.argmin()
    return array[smallest_difference_index[0]]

class graphSlider():
    graph = []
    figuresOfInterest = ()
    areaOfInterest = ()
    graphSize = []
    posMap = []
    frqGap = []
    sliderRange = []
    sliders = []
    colors = []
    idxMap = {}
    lineHeight = 6
    lineWidth = 5
    textGap = 12

    def movePoints(self, mousePosition):
        debugPrint('inMovePoints: ', self.graph.get_figures_at_location(mousePosition))
        debugPrint('Mouse Position: ', mousePosition)
        if mousePosition[0] in range(self.areaOfInterest[0], self.areaOfInterest[1]):
            elements = self.graph.get_figures_at_location(mousePosition)
            if len(elements):
                currentPoint = [x for x in self.figuresOfInterest if x in elements]
                debugPrint(currentPoint)
                if len(currentPoint):
                    sliderIdx = self.points.index(currentPoint[0]) - 2
                    newFreq = int(self.frqMap(mousePosition[0]))
                    self.setSlider(newFreq, sliderIdx)
                    self.drawSlider()

    def setSlider(self, newFrq, tgtIdx):
        if newFrq in range(self.sliderRange[0], self.sliderRange[1]):
            if tgtIdx<(len(self.sliders)-1) and self.sliders[tgtIdx + 1] - newFrq < self.frqGap:
                if self.setSlider(newFrq + self.frqGap, tgtIdx + 1):
                    self.sliders[tgtIdx] = newFrq
                    return True
                else:
                    return False
            elif tgtIdx>0 and newFrq - self.sliders[tgtIdx - 1] < self.frqGap:
                if self.setSlider(newFrq - self.frqGap, tgtIdx - 1):
                    self.sliders[tgtIdx] = newFrq
                    return True
                else:
                    return False
            else:
                self.sliders[tgtIdx] = newFrq
                return True

    def drawSlider(self):
        self.graph.erase()

        #* Creating lines
        # line[0] from sliderRange[0] to slider[0], line[1] from slider[0] to slider[1], line[2] from slider[1] to sliderRange[1]
        for lineNo in range(0, len(self.sliders) + 1):
            debugPrint('linePoints', (int(self.posMap((lineNo==0)*self.sliderRange[0] + (lineNo!=0)*self.sliders[lineNo-1])), self.lineHeight), (int(self.posMap((lineNo==len(self.sliders))*self.sliderRange[1] + (lineNo!=len(self.sliders))*self.sliders[lineNo%len(self.sliders)])), self.lineHeight))
            self.lines[lineNo] = self.graph.draw_line((int(self.posMap((lineNo==0)*self.sliderRange[0] + (lineNo!=0)*self.sliders[lineNo-1])), self.lineHeight), (int(self.posMap((lineNo==len(self.sliders))*self.sliderRange[1] + (lineNo!=len(self.sliders))*self.sliders[lineNo%len(self.sliders)])), self.lineHeight),
                                                        color=colorMap[(lineNo!=len(self.sliders))*self.colors[lineNo%len(self.colors)] + (lineNo==len(self.sliders))*'S'], width=self.lineWidth)
        
        textPad = self.lineHeight - self.textGap
        self.pointLabels[0] = self.graph.draw_text(str(self.sliderRange[0]), (int(self.posMap(self.sliderRange[0])), textPad), color=colorMap['W'])
        self.pointLabels[1] = self.graph.draw_text(str(self.sliderRange[1]), (int(self.posMap(self.sliderRange[1])), textPad), color=colorMap['W'])
        textPad = self.lineHeight + self.textGap
        for pointNo in range(2, 2 + len(self.sliders)):
            idx = pointNo - 2
            self.pointLabels[pointNo] = self.graph.draw_text(str(self.sliders[idx]), (int(self.posMap(self.sliders[idx])), textPad), color=colorMap[self.colors[idx]])

        pointWidth = int(self.lineWidth*1.8)
        self.points[0] = self.graph.draw_point((int(self.posMap(self.sliderRange[0])), self.lineHeight), pointWidth, color=colorMap['S'])
        self.points[1] = self.graph.draw_point((int(self.posMap(self.sliderRange[1])), self.lineHeight), pointWidth, color=colorMap['S'])
        for pointNo in range(2, 2 + len(self.sliders)):
            idx = pointNo - 2
            self.points[pointNo] = self.graph.draw_point((int(self.posMap(self.sliders[idx])), self.lineHeight), pointWidth, color=colorMap[self.colors[idx]])

        self.figuresOfInterest = tuple(self.points[2:])

    def __init__(self, graphInp, sliderRange=(1,100), sliders=[60], colors='C', relativeHeight=6, lineWidth=5, leftPad=10, rightPad=10):
        self.graph = graphInp
        self.graphSize = self.graph.CanvasSize
        self.areaOfInterest = (leftPad, self.graphSize[0] - rightPad)
        self.posMap = interp1d([sliderRange[0], sliderRange[1]], [self.areaOfInterest[0], self.areaOfInterest[1]])
        self.frqMap = interp1d([leftPad, self.graphSize[0] - rightPad], [sliderRange[0], sliderRange[1]])
        self.lineHeight = relativeHeight
        self.lineWidth = lineWidth
        self.sliderRange = sliderRange
        self.sliders = sliders
        self.colors = colors
        self.lines = [None] * (len(sliders) + 1)
        self.points = [None] * (len(sliders) + 2)
        self.pointLabels = [None] * (len(sliders) + 2)
        
        self.drawSlider()

        self.frqGap = ceil(((sliderRange[1] - sliderRange[0])/(self.areaOfInterest[1] - self.areaOfInterest[0]))*(self.graph.get_bounding_box(3*len(sliders)+5)[1][0] - self.graph.get_bounding_box(3*len(sliders)+5)[0][0]))
        

class chromatizer():

    pa = pyaudio.PyAudio()
    audioDevices = {}
    window = []
    freqSlider = []
    displayEffect = []
    activeDevice = []
    audioStream = []
    noFrames = []
    audioSampleRate = []
    audioDataRoll = []
    hammingWindow = []
    readTimeout = None
    melFrq = []

    preferences = sg.UserSettings(filename=str(getPrefFile()))

    if sg.user_settings_file_exists(str(getPrefFile())):
        preferences.load()
    else:
        preferences['audioDevice'] =  '--Refresh Audio Devices--'
        preferences['stripSaver'] = 'None'
        preferences['energyDisplay'] = False
        preferences['scrollDisplay'] = True
        preferences['spectrumDisplay'] = False
        preferences['displayEffect'] = 'Audio'
        preferences['colorOrder'] = 'BRG'
        preferences['brightness'] = 100
        preferences['dispFPS'] = False
        preferences['noPixels'] = 150
        preferences['tgtFPS'] = 90 
        preferences['noFFT'] = 24
        preferences['gainLimit'] = 0.000005
        preferences['volTol'] = 0.0001
        preferences['audioRoll'] = 2
        preferences['adAudio'] = 0.8
        preferences['adGain'] = 0.01
        preferences['adLED'] = 0.1
        preferences['gammaTable'] = 'Default'
        preferences['clrClose'] = True
        preferences['minFreq'] = 50
        preferences['lowFreq'] = 1500
        preferences['highFreq'] = 6000
        preferences['maxFreq'] = 16000
        preferences['arAudio'] = 0.92
        preferences['arGain'] = 0.99
        preferences['arLED'] = 0.9
        preferences['espUDPIP'] = '192.168.0.150'
        preferences['espUDPPort'] = 7777
        preferences['espSoftGamma'] = False
        preferences['rpLEDPin'] = 18
        preferences['rpLEDFreq'] = 800000
        preferences['rpLEDdma'] = 5
        preferences['rpLEDInvert'] = False
        preferences['rpUseWeb'] = False
        preferences['rpSoftGamma'] = True
        preferences['activeDevice'] = 'ESP 8266'

    #*  Update available input audio devices in a dictionary 
    def getAudioDevices(self):
        debugPrint('in getAudioDevices')
        info = self.pa.get_host_api_info_by_index(0)
        numDevices = info.get('deviceCount')
        self.audioDevices = {}
        for i in range(0, numDevices):
            if (self.pa.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                self.audioDevices[self.pa.get_device_info_by_host_api_device_index(0, i).get('name')] = i
        if self.preferences['audioDevice'] == '--Refresh Audio Devices--' or self.preferences['audioDevice'] not in self.audioDevices.keys():
            self.preferences['audioDevice'] = self.pa.get_default_input_device_info()['name']
        self.refreshAudioData()
    
    def getFPS(self):
        """Return the estimated frames per second

        Returns the current estimate for frames-per-second (FPS).
        FPS is estimated by measured the amount of time that has elapsed since
        this function was previously called. The FPS estimate is low-pass filtered
        to reduce noise.

        This function is intended to be called one time for every iteration of
        the program's main loop.

        Returns
        -------
        fps : float
            Estimated frames-per-second. This value is low-pass filtered
            to reduce noise.
        """
        currTime = time() * 1000.0
        dt = currTime - self.fpsTime
        self.fpsTime = currTime
        if dt == 0.0:
            return self.fps.value
        return self.fps.update(1000.0 / dt)

    def stripRainbow(self):
        debugPrint('inStripRainbow')

    def audioEffect(self):
        debugPrint('inAudioEffect')
        audioData = np.fromstring(self.audioStream.read(self.noFrames, exception_on_overflow=False), dtype=np.int16)
        audioData = audioData / 2.0**15
        self.audioDataRoll[:-1] = self.audioDataRoll[1:]
        self.audioDataRoll[-1, :] = np.copy(audioData)
        audioData = np.concatenate(self.audioDataRoll, axis=0).astype(np.float32)
        melValues = []
        melMax = []

        vol = np.max(np.abs(audioData))
        if vol < self.preferences['volTol']:
            self.stripSaver()
            self.readTimeout = 100
        else:
            self.readTimeout = 0
            audioLen = len(audioData)
            audioData *= self.hammingWindow
            audioDataPadded = np.pad(audioData, ((2**int(np.ceil(np.log2(audioLen))) - audioLen)//2, (2**int(np.ceil(np.log2(audioLen))) - audioLen)//2), mode='constant')
            # YS = np.abs(np.fft.rfft(y_padded)[:N // 2])
            melValues = librosa.feature.melspectrogram(y=audioDataPadded, sr=self.audioSampleRate, n_fft=self.noFrames*self.preferences['audioRoll']//2, win_length=self.noFrames, center=True, pad_mode='constant', power=2.0, n_mels=self.preferences['noFFT'], fmin=self.preferences['minFreq'], fmax=self.preferences['maxFreq'])
            melValues = np.sum(melValues, axis=1)
            melMax = np.max(gaussian_filter1d(melValues, sigma=1.0))
            gainCheck = int(np.max(self.melGain.value) > self.preferences['gainLimit'])
            self.melGain.updateDecay((gainCheck)*self.melGain.alpha_decay + (1-gainCheck)*0.0005)
            self.melGain.update((gainCheck)*melMax + (1-gainCheck)*self.preferences['gainLimit'])

            melValues /= self.melGain.value
            melValues = self.melSmooth.update(melValues)

            leftIndex = getClosestIndex(self.melFrq, self.preferences['lowFreq'])[0]
            rightIndex = getClosestIndex(self.melFrq, self.preferences['highFreq'])[0]
            
            lowBand = melValues[0 : leftIndex + 1]
            midBand = melValues[leftIndex : rightIndex + 1]
            highBand = melValues[rightIndex : self.preferences['noFFT']]

            self.plotAx.cla()
            self.plotAx.plot(self.melFrq, [melMax]*len(self.melFrq),'m', self.melFrq, self.melGain.value,'c' ,self.melFrq[0 : leftIndex+1], lowBand, self.preferences['colorOrder'][0].lower(), self.melFrq[leftIndex : rightIndex+1], midBand, self.preferences['colorOrder'][1].lower(), self.melFrq[rightIndex : self.preferences['noFFT']], highBand, self.preferences['colorOrder'][2].lower())
            
            self.plotFig.draw()

        debugPrint('Audio Data: ', melValues, )
        debugPrint('gain: ',self.melGain.value,'\t','melMax',melMax,'\t','Volume: ', vol)

    def rainbowEffect(self):
        debugPrint('inRainbowEffect')

    def singleEffect(self):
        debugPrint('inSingleEffect')

    def getEffectHandle(self):
        if self.preferences['_displayEffect_'] == 'Audio':
            self.displayEffect = self.audioEffect
            self.readTimeout = 0
        elif self.preferences['_displayEffect_'] == 'Rainbow':
            self.displayEffect = self.rainbowEffect
            self.readTimeout = 0
        elif self.preferences['_displayEffect_'] == 'Single':
            self.displayEffect = self.singleEffect
            self.readTimeout = None

    def refreshAudioData(self):
        deviceInfo = self.pa.get_device_info_by_index(self.audioDevices[self.preferences['audioDevice']])
        self.audioSampleRate = int(deviceInfo['defaultSampleRate'])
        self.noFrames = int(self.audioSampleRate // self.preferences['tgtFPS'])
        self.audioDataRoll = np.random.rand(self.preferences['audioRoll'], self.noFrames) / 1e16
        self.hammingWindow = np.hamming(self.noFrames*self.preferences['audioRoll'])
        self.melFrq = librosa.mel_frequencies(n_mels=self.preferences['noFFT'], fmin=self.preferences['minFreq'], fmax=self.preferences['maxFreq'], htk=False)

        self.melGain= expFilter(np.tile(self.preferences['gainLimit'], self.preferences['noFFT']), alpha_decay=self.preferences['adGain'], alpha_rise=self.preferences['arGain'])
        self.melSmooth = expFilter(np.tile(1e-1, self.preferences['noFFT']),  alpha_decay=self.preferences['adAudio'], alpha_rise=self.preferences['arAudio'])
        # self.ledSmooth = expFilter(np.tile(0, self.preferences['noFFT']),  alpha_decay=self.preferences['adLED'], alpha_rise=self.preferences['arLED'])

        if self.audioStream != []:
            self.audioStream.stop_stream()
            self.audioStream.close()
        
        self.audioStream = self.pa.open(format=pyaudio.paInt16, channels=1, rate=self.audioSampleRate, input=True, input_device_index=self.audioDevices[self.preferences['audioDevice']], frames_per_buffer=self.noFrames)

    def loopActions(self):
        debugPrint('inLoopActions: ', self.displayEffect)
        self.displayEffect()

    def closeActions(self):
        self.savePreferences()
        self.pa.terminate()

    def displayPreferences(self):
        debugPrint('inDisplayPreferences')
        self.window['_audioDevice_'].update(value = self.preferences['audioDevice']) 
        self.window['_stripSaver_'].update(value = self.preferences['stripSaver'])
        self.window['_energyDisplay_'].update(value = self.preferences['energyDisplay'])
        self.window['_scrollDisplay_'].update(value = self.preferences['scrollDisplay'])
        self.window['_spectrumDisplay_'].update(value = self.preferences['spectrumDisplay'])
        self.window['_colorOrder_'].update(value = self.preferences['colorOrder'])
        self.window['_dispFPS_'].update(value = self.preferences['dispFPS'])
        self.window['_noPixels_'].update(value = str(self.preferences['noPixels']))
        self.window['_tgtFPS_'].update(value = str(self.preferences['tgtFPS']))
        self.window['_noFFT_'].update(value = str(self.preferences['noFFT']))
        self.window['_gainLimit_'].update(value = str(self.preferences['gainLimit']))
        self.window['_volTol_'].update(value = str(self.preferences['volTol']))
        self.window['_audioRoll_'].update(value = str(self.preferences['audioRoll']))
        self.window['_adAudio_'].update(value = str(self.preferences['adAudio']))
        self.window['_adGain_'].update(value = str(self.preferences['adGain']))
        self.window['_adLED_'].update(value = str(self.preferences['adLED']))
        self.window['_gammaTable_'].update(value = self.preferences['gammaTable'])
        self.window['_clrClose_'].update(value = self.preferences['clrClose'])
        self.window['_minFreq_'].update(value = str(self.preferences['minFreq']))
        self.window['_lowFreq_'].update(value = str(self.preferences['lowFreq']))
        self.window['_highFreq_'].update(value = str(self.preferences['highFreq']))
        self.window['_maxFreq_'].update(value = str(self.preferences['maxFreq']))
        self.window['_arAudio_'].update(value = str(self.preferences['arAudio']))
        self.window['_arGain_'].update(value = str(self.preferences['arGain']))
        self.window['_arLED_'].update(value = str(self.preferences['arLED']))
        self.window['_espUDPIP_'].update(value = self.preferences['espUDPIP'])
        self.window['_espUDPPort_'].update(value = str(self.preferences['espUDPPort']))
        self.window['_espSoftGamma_'].update(value = self.preferences['espSoftGamma'])
        self.window['_rpLEDPin_'].update(value = str(self.preferences['rpLEDPin']))
        self.window['_rpLEDFreq_'].update(value = str(self.preferences['rpLEDFreq']))
        self.window['_rpLEDdma_'].update(value = str(self.preferences['rpLEDdma']))
        self.window['_rpLEDInvert_'].update(value = self.preferences['rpLEDInvert'])
        self.window['_rpUseWeb_'].update(value = self.preferences['rpUseWeb'])
        self.window['_rpSoftGamma_'].update(value = self.preferences['rpSoftGamma'])
        self.window.refresh()

    def savePreferences(self):
        debugPrint('inSavePreferences')
        event, values = self.window.read(timeout=0)
        self.preferences['audioDevice'] =  values['_audioDevice_']
        self.preferences['stripSaver'] = values['_stripSaver_']
        self.preferences['energyDisplay'] = values['_energyDisplay_']
        self.preferences['scrollDisplay'] = values['_scrollDisplay_']
        self.preferences['spectrumDisplay'] = values['_spectrumDisplay_']
        self.preferences['displayEffect'] = values['_displayEffect_']
        self.preferences['colorOrder'] = values['_colorOrder_']
        self.preferences['brightness'] = self.brightSlider.sliders[0]
        self.preferences['dispFPS'] = values['_dispFPS_']
        self.preferences['noPixels'] = int(values['_noPixels_'])
        self.preferences['tgtFPS'] = int(values['_tgtFPS_'])
        self.preferences['noFFT'] = int(values['_noFFT_'])
        self.preferences['gainLimit'] = float(values['_gainLimit_'])
        self.preferences['volTol'] = float(values['_volTol_'])
        self.preferences['audioRoll'] = int(values['_audioRoll_'])
        self.preferences['adAudio'] = float(values['_adAudio_'])
        self.preferences['adGain'] = float(values['_adGain_'])
        self.preferences['adLED'] = float(values['_adLED_'])
        self.preferences['gammaTable'] = values['_gammaTable_']
        self.preferences['clrClose'] = values['_clrClose_']
        self.preferences['minFreq'] = int(values['_minFreq_'])
        self.preferences['lowFreq'] = int(values['_lowFreq_'])
        self.preferences['highFreq'] = int(values['_highFreq_'])
        self.preferences['maxFreq'] = int(values['_maxFreq_'])
        self.preferences['arAudio'] = float(values['_arAudio_'])
        self.preferences['arGain'] = float(values['_arGain_'])
        self.preferences['arLED'] = float(values['_arLED_'])
        self.preferences['espUDPIP'] = values['_espUDPIP_']
        self.preferences['espUDPPort'] = int(values['_espUDPPort_'])
        self.preferences['espSoftGamma'] = values['_espSoftGamma_']
        self.preferences['rpLEDPin'] = int(values['_rpLEDPin_'])
        self.preferences['rpLEDFreq'] = int(values['_rpLEDFreq_'])
        self.preferences['rpLEDdma'] = int(values['_rpLEDdma_'])
        self.preferences['rpLEDInvert'] = values['_rpLEDInvert_']
        self.preferences['rpUseWeb'] = values['_rpUseWeb_']
        self.preferences['rpSoftGamma'] = values['_rpSoftGamma_']
        self.preferences['activeDevice'] = values['_activeDevice_']

    def __init__(self):
        debugPrint('in Init')
        self.getAudioDevices()
        tmpBackground = '#808080'
        tmpBackground = None
        verticalGap = 5

        rainbowLayout = [[sg.Graph(canvas_size=(800,250), graph_bottom_left=(0,0), graph_top_right=(800,250), background_color=tmpBackground, enable_events=True, drag_submits=True, key='_rainbowGraph_')]]
        
        singleLayout =  [[sg.Graph(canvas_size=(800,250), graph_bottom_left=(0,0), graph_top_right=(800,250), background_color=tmpBackground, enable_events=True, drag_submits=True, key='_singleGraph_')]]

        audioLayout =   [[sg.Canvas(key='_plot_', size=(800,200),background_color=tmpBackground, right_click_menu=['', ['Enable Output Plot', 'Enable Freq., Plot', 'Enable Gain Plot']])],
                        [sg.Sizer(60,3), sg.T('Select \'Strip\'saver: '), sg.Combo(['None','Rainbow'], default_value=self.preferences['stripSaver'], key='_stripSaver_', tooltip='Select what to show when audio level below min threshold.', enable_events=True, readonly=True),
                        sg.Sizer(60,3), sg.Radio('Energy', 'vizEffect', default=self.preferences['energyDisplay'], enable_events=True, tooltip='Colors expand from the center corresponding to sound energy.', key='_energyDisplay_'),
                        sg.Sizer(60,3), sg.Radio('Scroll', 'vizEffect', default=self.preferences['scrollDisplay'], enable_events=True, tooltip='Colors originate in the center and scrolls outwards.', key='_scrollDisplay_'),
                        sg.Sizer(60,3), sg.Radio('Spectrum', 'vizEffect', default=self.preferences['spectrumDisplay'], enable_events=True, tooltip='Audio spectrum is mapped to strip.', key='_spectrumDisplay_'), sg.Push()]]

        prefC1Layout =  [[getPrefName('No of Pixels:'), sg.Input(default_text=str(self.preferences['noPixels']), tooltip='Number of LEDs in the strip.', size=(15,1), justification='center' , enable_events=True, key='_noPixels_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Target FPS:'), sg.Input(default_text=str(self.preferences['tgtFPS']), tooltip='Target refresh rate of LEDs.', size=(15,1), justification='center' , enable_events=True, key='_tgtFPS_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('No of FFT Bands:'), sg.Input(default_text=str(self.preferences['noFFT']), tooltip='Number of frequency bins to use when transforming audio to frequency domain.', size=(15,1), justification='center' , enable_events=True, key='_noFFT_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Gain Limit:'), sg.Input(default_text=str(self.preferences['gainLimit']), tooltip='A lower limit to filter bank output gain. Better let it alone.', size=(15,1), justification='center' , enable_events=True, key='_gainLimit_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Volume Tolerance:'), sg.Input(default_text=str(self.preferences['volTol']), tooltip='\'Strip\'saver will be displayed if recorded audio volume is below threshold.', size=(15,1), justification='center' , enable_events=True, key='_volTol_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Audio Rolling Window:'), sg.Input(default_text=str(self.preferences['audioRoll']), tooltip='Number of past audio frames to include in the rolling window.', size=(15,1), justification='center' , enable_events=True, key='_audioRoll_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Alpha Decay Audio:'), sg.Input(default_text=str(self.preferences['adAudio']), tooltip='Alpha decay of audio input values (Small value = more smoothing).', size=(15,1), justification='center' , enable_events=True, key='_adAudio_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Alpha Decay Gain:'), sg.Input(default_text=str(self.preferences['adGain']), tooltip='Alpha decay of gain value applied to filter bank output (Small value = more smoothing).', size=(15,1), justification='center' , enable_events=True, key='_adGain_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Alpha Decay LED:'), sg.Input(default_text=str(self.preferences['adLED']), tooltip='Alpha decay of LED output values (Small value = more smoothing).', size=(15,1), justification='center' , enable_events=True, key='_adLED_')]]

        prefC2Layout =  [[getPrefName('Gamma Table:'), sg.Combo(['Default','--Select file--'], default_value=self.preferences['gammaTable'], key='_gammaTable_', size=(13,1), tooltip='Select gamma correction table.', enable_events=True, readonly=True)],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Clear on Close:'), sg.Sizer(42,1),sg.Checkbox(' ', default=self.preferences['clrClose'], tooltip='If checked LED strip will be cleared before closing the application.', enable_events=True, key='_clrClose_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Min Frequency:'), sg.Input(default_text=str(self.preferences['minFreq']), tooltip='Frequency lower limit for signal analysis.', size=(15,1), justification='center' , enable_events=True, key='_minFreq_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Low Frequency:'), sg.Input(default_text=str(self.preferences['lowFreq']), tooltip='Upper limit of low frequency range.', size=(15,1), justification='center' , enable_events=True, key='_lowFreq_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('High Frequency:'), sg.Input(default_text=str(self.preferences['highFreq']), tooltip='Lower limit of high frequency range.', size=(15,1), justification='center' , enable_events=True, key='_highFreq_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Max Frequency:'), sg.Input(default_text=str(self.preferences['maxFreq']), tooltip='Frequency upper limit for signal analysis.', size=(15,1), justification='center' , enable_events=True, key='_maxFreq_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Alpha Rise Audio:'), sg.Input(default_text=str(self.preferences['arAudio']), tooltip='Alpha rise of audio input values (Small value = more smoothing).', size=(15,1), justification='center' , enable_events=True, key='_arAudio_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Alpha Rise Gain:'), sg.Input(default_text=str(self.preferences['arGain']), tooltip='Alpha rise of gain value applied to filter bank output (Small value = more smoothing).', size=(15,1), justification='center' , enable_events=True, key='_arGain_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Alpha Rise LED:'), sg.Input(default_text=str(self.preferences['arLED']), tooltip='Alpha rise of LED output values (Small value = more smoothing).', size=(15,1), justification='center' , enable_events=True, key='_arLED_')]]

        prefEspLayout = [[sg.Push(), sg.Column([[sg.Sizer(20,verticalGap)],
                        [getPrefName('UDP IP:'), sg.Input(default_text=self.preferences['espUDPIP'], tooltip='IP address of the ESP8266. Must be same as IP specified in ESP8266 code.', size=(15,1), justification='center' , enable_events=True, key='_espUDPIP_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('UDP Port:'), sg.Input(default_text=str(self.preferences['espUDPPort']), tooltip='Port number used for communication between program and ESP8266.', size=(15,1), justification='center' , enable_events=True, key='_espUDPPort_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('S/W Gamma Correction:'), sg.Sizer(42,1), sg.Checkbox(' ', default=self.preferences['espSoftGamma'], tooltip='Set to False because the ESP firmware handles gamma correction + dither.', enable_events=True, key='_espSoftGamma_')]]), sg.Push()]]

        prefPi1Layout = [[sg.Sizer(20,verticalGap)],
                        [getPrefName('LED Pin:'), sg.Input(default_text=str(self.preferences['rpLEDPin']), tooltip='GPIO pin connected to the LED strip pixels (must support PWM).', size=(15,1), justification='center' , enable_events=True, key='_rpLEDPin_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('LED Freq Hz:'), sg.Input(default_text=str(self.preferences['rpLEDFreq']), tooltip='LED signal frequency in Hz (usually 800kHz).', size=(15,1), justification='center' , enable_events=True, key='_rpLEDFreq_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('LED DMA channel:'), sg.Input(default_text=str(self.preferences['rpLEDdma']), tooltip='DMA channel used for generating PWM signal (try 5).', size=(15,1), justification='center' , enable_events=True, key='_rpLEDdma_')]]

        prefPi2Layout = [[sg.Sizer(20,verticalGap)],
                        [getPrefName('LED Invert:'), sg.Sizer(42,1), sg.Checkbox(' ', tooltip='Set True if using an inverting logic level converter.', default=self.preferences['rpLEDInvert'], enable_events=True, key='_rpLEDInvert_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('Use Web Interface:'), sg.Sizer(42,1), sg.Checkbox(' ', tooltip='Set True to use web interface on restart.', default=self.preferences['rpUseWeb'], enable_events=True, key='_rpUseWeb_')],
                        [sg.Sizer(20,verticalGap)],
                        [getPrefName('S/W Gamma Correction:'), sg.Sizer(42,1), sg.Checkbox(' ', default=self.preferences['rpSoftGamma'], tooltip='Set to True because Raspberry Pi doesn\'t use hardware dithering.', enable_events=True, key='_rpSoftGamma_')]]

        prefLayout =    [[sg.Sizer(20,verticalGap)], [sg.Push(), sg.Column(prefC1Layout, right_click_menu=['', ['Save Settings']]), sg.Sizer(80,3) ,sg.Column(prefC2Layout, right_click_menu=['', ['Save Settings']]), sg.Push()],
                        [sg.Sizer(20,verticalGap)],
                        [sg.Push(), sg.TabGroup([[sg.Tab('ESP 8266', prefEspLayout, right_click_menu=['', ['Save Settings']]), sg.Tab('Raspberry Pi', [[sg.Sizer(44,3), sg.Column(prefPi1Layout, right_click_menu=['', ['Save Settings']]), sg.Sizer(80,3) ,sg.Column(prefPi2Layout, right_click_menu=['', ['Save Settings']]), sg.Push()]], right_click_menu=['', ['Save Settings']])]], size=(800,200), enable_events=True, key='_activeDevice_', tab_location='top'), sg.Push()]]

        ctrlLayout =    [[sg.Sizer(60,3)],[sg.Push(),sg.B(button_text='Start', tooltip='Start the show.', enable_events=True, button_color='green', key='_start_',size=(10,1)), sg.Sizer(60,00), sg.T('Select audio source: '),
                        sg.Combo(list(self.audioDevices.keys())+['--Refresh Audio Devices--'], default_value=self.preferences['audioDevice'], key='_audioDevice_', tooltip='Select audio source.', enable_events=True, readonly=True),sg.Push()],
                        [sg.HorizontalSeparator()],
                        [sg.Push(), sg.TabGroup([[sg.Tab('Audio', audioLayout), sg.Tab('Rainbow', rainbowLayout), sg.Tab('Single', singleLayout)]], size=(800,250), enable_events=True, key='_displayEffect_', tab_location='top'), sg.Push()],
                        [sg.Sizer(60,8)], [sg.Push(), sg.T('Color band order: '),
                        sg.Combo(['RRR', 'RRG', 'RRB', 'RGR', 'RGG', 'RGB', 'RBR', 'RBG', 'RBB', 'GRR', 'GRG', 'GRB', 'GGR', 'GGG', 'GGB', 'GBR', 'GBG', 'GBB', 'BRR', 'BRG', 'BRB', 'BGR', 'BGG', 'BGB', 'BBR', 'BBG', 'BBB'], default_value=self.preferences['colorOrder'], key='_colorOrder_', tooltip='Select color corresponding to Low, Mid and High band activations.', enable_events=True, readonly=True, size=(5,1)),
                        sg.Sizer(30,00), sg.T('Brightness: '), sg.Graph(canvas_size=(270,40), graph_bottom_left=(0,0), graph_top_right=(270, 40), background_color=tmpBackground, motion_events = False, enable_events = True, drag_submits = True, key='_brightGraph_'), sg.Sizer(30,00),
                        sg.Checkbox('Display FPS', enable_events=True, default=self.preferences['dispFPS'], key='_dispFPS_'), sg.pin(sg.T('01', key='_FPS_', visible=self.preferences['dispFPS'])), sg.Push()],
                        [sg.Sizer(80,7)], [sg.Push(), sg.T(' Select Frequency Ranges for Audio Analysis '.center(100,'-')), sg.Push()],
                        [sg.Graph(canvas_size=(800,40), graph_bottom_left=(0,0), graph_top_right=(800, 40), background_color=tmpBackground, motion_events = False, enable_events = True, drag_submits = True, key='_freqGraph_')]]
        
        aboutLayout =   [[sg.Push(), sg.Image(source=signatureImage), sg.Push()]]

        layout = [[sg.TabGroup([[sg.Tab('LED Control', ctrlLayout, right_click_menu=['', ['Save Settings']]), sg.Tab('Preferences', prefLayout, right_click_menu=['', ['Save Preferences', 'Reset Preferences']]), sg.Tab('About', aboutLayout)]], enable_events=True, key='_mainTab_', size=(800,500), tab_location='top', right_click_menu=['', ['Save Settings']])]]
        
        self.window = sg.Window('Chromatizer: The Color of Music', layout, finalize=True, icon=windowIcon, size=(800,500), enable_close_attempted_event=True)

        #* Adding sliders
        self.freqSlider = graphSlider(self.window['_freqGraph_'], sliderRange=(0,22000), sliders=[self.preferences['minFreq'], self.preferences['lowFreq'], self.preferences['highFreq'], self.preferences['maxFreq']],
                                        colors='S'+self.preferences['colorOrder'], relativeHeight=23, lineWidth=5, leftPad=15, rightPad=60)
        self.brightSlider = graphSlider(self.window['_brightGraph_'], sliderRange=(0,100), sliders=[self.preferences['brightness']], colors='C', relativeHeight=20, lineWidth=5, leftPad=15, rightPad=15)

        self.fpsTime = time() * 1000.0
        self.fps = expFilter(val=self.preferences['tgtFPS'], alpha_decay=0.2, alpha_rise=0.2)
        self.getEffectHandle()

        self.melGain= expFilter(np.tile(self.preferences['gainLimit'], self.preferences['noFFT']), alpha_decay=self.preferences['adGain'], alpha_rise=self.preferences['arGain'])
        self.melSmooth = expFilter(np.tile(1e-1, self.preferences['noFFT']),  alpha_decay=self.preferences['adAudio'], alpha_rise=self.preferences['arAudio'])
        # self.ledSmooth = expFilter(np.tile(0, self.preferences['noFFT']),  alpha_decay=self.preferences['adLED'], alpha_rise=self.preferences['arLED'])
        self.stripSaver = self.stripRainbow

        # instantiate matplotlib figure
        fig = plt.figure(facecolor=sg.theme_background_color(), alpha=0.0)
        fig.patch.set_alpha(0.0)
        # fig.FigureBase.set_facecolor(sg.theme_background_color())
        self.plotAx = fig.add_axes([0.005,0.02,0.99,0.97], autoscale_on=True, alpha=0.0, xscale="log")
        # self.plotAx.set_facecolor(sg.theme_background_color())
        self.plotAx.grid(visible=True, which='major')
        DPI = fig.get_dpi()
        fig.set_size_inches(748 / float(DPI), 202 / float(DPI))
        self.plotFig = draw_figure(self.window['_plot_'].TKCanvas, fig)
        self.plotAx.set_ylim(0, 1)
        self.plotAx.set_xlim(self.preferences['minFreq'], self.preferences['maxFreq'])

        #* Selecting tab from previous session 
        self.window[self.preferences['displayEffect']].select()
        self.window[self.preferences['activeDevice']].select()


def main():
    cs = chromatizer()
    splashWindow.close()
    while True:      
        event, values = cs.window.read(cs.readTimeout)
        # debugPrint(type(event))
        debugPrint(event, values)
        debugPrint(sg.user_settings())
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            cs.closeActions()
            break
        elif values['_audioDevice_'] == '--Refresh Audio Devices--':
            cs.getAudioDevices()
            cs.window['_audioDevice_'].update(values=list(cs.audioDevices.keys())+['--Refresh Audio Devices--'], value = cs.preferences['audioDevice'])
        elif event == '_audioDevice_' and values['_audioDevice_'] != '--Refresh Audio Devices--':
            cs.preferences['audioDevice'] = values['_audioDevice_']
            cs.refreshAudioData()
        elif event == '_freqGraph_':
            cs.freqSlider.movePoints(values['_freqGraph_'])
            cs.preferences['minFreq'] = cs.freqSlider.sliders[0]
            cs.preferences['lowFreq'] = cs.freqSlider.sliders[1]
            cs.preferences['highFreq'] = cs.freqSlider.sliders[2]
            cs.preferences['maxFreq'] = cs.freqSlider.sliders[3]
            cs.displayPreferences()
            cs.window.refresh()
        elif event == '_brightGraph_':
            cs.brightSlider.movePoints(values['_brightGraph_'])
            cs.preferences['brightness'] = cs.brightSlider.sliders[0]
            cs.displayPreferences()
            cs.window.refresh()
        elif event == '_displayEffect_':
            cs.preferences['_displayEffect_'] = values['_displayEffect_']
            cs.getEffectHandle()
            
        elif event == 'Save Preferences' or event == 'Save Settings' or event == '_mainTab_' or event == '_displayEffect_' or event == '_activeDevice_':
            cs.freqSlider.sliders = [cs.preferences['minFreq'], cs.preferences['lowFreq'], cs.preferences['highFreq'], cs.preferences['maxFreq']]
            cs.freqSlider.drawSlider()
            cs.savePreferences()
            cs.refreshAudioData()
            cs.window.refresh()
    
        cs.loopActions()

    cs.window.close()

if __name__ == "__main__":
    main()


