"""
Title              : Chromatizer
Description        : The Color of Music
Author             : Kondapi Prasanth
Created            : 09-Jul-2022
Modified           : 12-Jul-2022
Version            : 0
Revision History   : 0

"""

import PySimpleGUI as sg, sys, pathlib
from pyaudio import PyAudio
from scipy.interpolate import interp1d
from math import ceil


windowIcon = None
signatureImage = None

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

    pa = PyAudio()
    audioDevices = {}
    window = []
    freqSlider = []

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
        preferences['volTol'] = 0.0000000001
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
        self.preferences['audioDevice'] = self.pa.get_default_input_device_info()['name']
    
    def closeActions(self):
        self.savePreferences()

    def displayPreferences(self):
        debugPrint('inDisplayPreferences')
        self.window['_audioDevice_'].update(value = self.preferences['audioDevice']) 
        self.window['_stripSaver_'].update(value = self.preferences['stripSaver'])
        self.window['_energyDisplay_'].update(value = self.preferences['energyDisplay'])
        self.window['_scrollDisplay_'].update(value = self.preferences['scrollDisplay'])
        self.window['_spectrumDisplay_'].update(value = self.preferences['spectrumDisplay'])
        self.window['_colorOrder_'].update(value = self.preferences['colorOrder'])
        # self.preferences['brightness'].update(value = 100) #! Change it to local variable
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
        self.preferences['brightness'] = 100 #! Change it to local variable
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
                        sg.Sizer(30,00), sg.T('Brightness: '), sg.Graph(canvas_size=(270,30), graph_bottom_left=(0,0), graph_top_right=(270, 30), background_color=tmpBackground, motion_events = False, enable_events = True, drag_submits = True, key='_brightGraph_'), sg.Sizer(30,00),
                        sg.Checkbox('Display FPS', enable_events=True, default=self.preferences['dispFPS'], key='_dispFPS_'), sg.pin(sg.T('01', key='_FPS_', visible=self.preferences['dispFPS'])), sg.Push()],
                        [sg.Sizer(80,7)], [sg.Push(), sg.T(' Select Frequency Ranges for Audio Analysis '.center(100,'-')), sg.Push()],
                        [sg.Graph(canvas_size=(800,40), graph_bottom_left=(0,0), graph_top_right=(800, 40), background_color=tmpBackground, motion_events = False, enable_events = True, drag_submits = True, key='_freqGraph_')]]
        
        aboutLayout =   [[sg.Push(), sg.Image(source=signatureImage), sg.Push()]]

        layout = [[sg.TabGroup([[sg.Tab('LED Control', ctrlLayout, right_click_menu=['', ['Save Settings']]), sg.Tab('Preferences', prefLayout, right_click_menu=['', ['Save Preferences', 'Reset Preferences']]), sg.Tab('About', aboutLayout)]], enable_events=True, key='_mainTab_', size=(800,500), tab_location='top', right_click_menu=['', ['Save Settings']])]]
        
        self.window = sg.Window('Chromatizer: The Color of Music', layout, finalize=True, icon=windowIcon, size=(800,500), enable_close_attempted_event=True)

        #* Adding sliders
        self.freqSlider = graphSlider(self.window['_freqGraph_'], sliderRange=(0,22000), sliders=[self.preferences['minFreq'], self.preferences['lowFreq'], self.preferences['highFreq'], self.preferences['maxFreq']],
                                        colors='S'+self.preferences['colorOrder'], relativeHeight=20, lineWidth=5, leftPad=15, rightPad=60)

        #* Selecting tab from previous session 
        self.window[self.preferences['displayEffect']].select()
        self.window[self.preferences['activeDevice']].select()


def main():
    cs = chromatizer()
    while True:      
        event, values = cs.window.read()
        # debugPrint(type(event))
        debugPrint(event, values)
        debugPrint(sg.user_settings())
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            cs.closeActions()
            break
        elif event == '_audioDevice_' and values['_audioDevice_'] == '--Refresh Audio Devices--':
            cs.getAudioDevices()
            cs.window['_audioDevice_'].update(values=list(cs.audioDevices.keys())+['--Refresh Audio Devices--'], value = cs.preferences['audioDevice'])
        elif event == '_freqGraph_':
            cs.freqSlider.movePoints(values['_freqGraph_'])
            cs.preferences['minFreq'] = cs.freqSlider.sliders[0]
            cs.preferences['lowFreq'] = cs.freqSlider.sliders[1]
            cs.preferences['highFreq'] = cs.freqSlider.sliders[2]
            cs.preferences['maxFreq'] = cs.freqSlider.sliders[3]
            cs.displayPreferences()
            cs.window.refresh()
        elif event == 'Save Preferences' or event == 'Save Settings' or event == '_mainTab_' or event == '_displayEffect_' or event == '_activeDevice_':
            cs.savePreferences()
    cs.window.close()

if __name__ == "__main__":
    main()


