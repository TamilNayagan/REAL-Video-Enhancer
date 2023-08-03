from src.settings import *
from src.messages import *
import src.queue.queue as queue
def onApplicationStart(self):
    import os
    
    #Import all modules
    ''' for module in os.listdir(f'{thisdir}/modules/'):
            if module == '__init__.py' or module[-3:] != '.py':
                continue
            __import__(f'modules.{module[:-3]}', locals(), globals())
            
            self.ui.AICombo.addItem(f'{module[:-3]}')'''
    import modules.Rife as rife
    import modules.ESRGAN as esrgan
    settings = Settings()
    from PyQt5.QtGui import QIntValidator, QIcon
    thisdir=os.getcwd()
    
    
    
    self.input_file = ''
    self.output_folder = ''
    self.setWindowIcon(QIcon(f'{thisdir}/icons/logo v1.png'))
    self.ui.SettingsMenus.clicked.connect(self.settings_menu)
    self.ui.resetSettingsButton.clicked.connect(self.restore_default_settings)
    self.settings = Settings()
    self.gpuMemory=self.settings.VRAM
    self.ui.AICombo.currentIndexChanged.connect(self.switchUI)
    self.switchUI()
    if self.gpuMemory != 'None':
        
        self.ui.vramAmountSpinbox.setValue(int(self.gpuMemory))
        if HardwareInfo.get_video_memory_linux() != None:
            self.ui.vramAmountSpinbox.setMaximum(int(HardwareInfo.get_video_memory_linux()))
    else:
        self.ui.vramAmountSpinbox.setValue(1)
        cannot_detect_vram(self)
    self.ui.vramAmountSpinbox.setMinimum(1)
    self.ui.vramAmountSpinbox.valueChanged.connect(self.changeVRAM)
    self.ui.vramAmountHelpButton.clicked.connect(lambda: vram_help(self))
    #Define Variables
    self.input_file = ''
    self.output_folder = ''
    self.output_folder = settings.OutputDir 
    self.videoQuality = settings.videoQuality
    self.encoder = settings.Encoder
    if os.path.exists(f"{settings.RenderDir}") == False:
        settings.change_setting('RenderDir',f'{thisdir}')
    self.render_folder = settings.RenderDir
    self.ui.sceneChangeSensativityButton.setIcon(QIcon(f"{thisdir}/icons/Rife-ESRGAN-Video-Settings - Help.png"))
    self.ui.encoderHelpButton.setIcon(QIcon(f"{thisdir}/icons/Rife-ESRGAN-Video-Settings - Help.png"))
    self.ui.imageHelpButton.setIcon(QIcon(f"{thisdir}/icons/Rife-ESRGAN-Video-Settings - Help.png"))
    self.ui.Rife_Times.currentIndexChanged.connect(self.showChangeInFPS)
    self.ui.RifePause.clicked.connect(self.pause_render)
    self.ui.RifeResume.clicked.connect(self.resume_render)
    self.ui.RifeResume.hide()
    self.ui.RifePause.hide()
    self.ui.DiscordRPCBox.stateChanged.connect(lambda: changeDiscordRPC(self))
    if settings.DiscordRPC == 'Enabled':
        self.ui.DiscordRPCBox.setChecked(True)
        
    else:
        self.ui.DiscordRPCBox.setChecked(False)
    os.system('ln -sf {app/com.discordapp.Discord,$XDG_RUNTIME_DIR}/discord-ipc-0') #Enables discord RPC on flatpak
    onlyInt = QIntValidator()
    onlyInt.setRange(0, 9)
    self.ui.sceneChangeLineEdit.setValidator(onlyInt)
    self.ui.sceneChangeLineEdit.textChanged.connect(lambda: changeSceneDetection(self))
    self.ui.sceneChangeLineEdit.setText(settings.SceneChangeDetection[2])
    if self.encoder == '264':
        self.ui.EncoderCombo.setCurrentIndex(0)
    if self.encoder == '265':
        self.ui.EncoderCombo.setCurrentIndex(1)
    if self.videoQuality == '10':
        self.ui.VidQualityCombo.setCurrentText('Lossless')
    if self.videoQuality == '14':
        self.ui.VidQualityCombo.setCurrentText('High')
    if self.videoQuality == '18':
        self.ui.VidQualityCombo.setCurrentText('Medium')
    if self.videoQuality == '22':
        self.ui.VidQualityCombo.setCurrentText('Low')
    self.ui.Rife_Model.currentIndexChanged.connect(self.greyOutRifeTimes)
    
    #link help buttons
    self.ui.sceneChangeSensativityButton.clicked.connect(lambda: show_scene_change_help(self))
    self.ui.encoderHelpButton.clicked.connect(lambda:  encoder_help(self))
    
    self.ui.RenderPathLabel.setText(f"{settings.RenderDir}")
    self.ui.RenderDirButton.clicked.connect(lambda: selRenderDir(self))
    
    self.ui.Input_video_rife.clicked.connect(self.openFileNameDialog)
    self.ui.Output_folder_rife.clicked.connect(self.openFolderDialog)
    self.ui.VideoOptionsFrame.hide()
    self.ui.RenderOptionsFrame.hide()
    self.ui.GeneralOptionsFrame.hide()
   
    
    self.ui.EncoderCombo.currentIndexChanged.connect(lambda: selEncoder(self))
    #apparently adding multiple currentindexchanged causes a memory leak unless i sleep, idk why it does this but im kinda dumb
    
    self.ui.VidQualityCombo.currentIndexChanged.connect(lambda: selVidQuality(self))
    self.ui.QueueButton.clicked.connect(lambda: queue.addToQueue(self))
    self.ui.QueueButton.hide()
    self.ui.QueueListWidget.hide()
    self.QueueList=[]
    self.setDirectories()
    self.ui.imageComboBox.setCurrentText(f'{settings.Image_Type}')
    self.ui.imageHelpButton.clicked.connect(lambda: image_help(self))
    self.ui.imageComboBox.currentIndexChanged.connect(lambda: settings.change_setting('Image_Type', f'{self.ui.imageComboBox.currentText()}'))
    if self.gpuMemory == None:
        cannot_detect_vram(self)
    else:
        pass
    # list every model downloaded, and add them to the list
    self.ui.SettingsMenus.setCurrentRow(0)
    self.ui.GeneralOptionsFrame.show()
def list_model_downloaded(self):
        settings = Settings()
        model_filepaths = ([x[0] for x in os.walk(f'{settings.ModelDir}/rife/')])
        models = []
        for model_filepath in model_filepaths:
            if 'rife' in os.path.basename(model_filepath):
                models.append(os.path.basename(model_filepath))
        
        models.sort()
        for model in models:

            
            model = model.replace('r',"R")
            model = model.replace('v','V')
            model = model.replace('a','A')
            self.ui.Rife_Model.addItem(f'{model}')#Adds model to GUI.
            if model == 'Rife-V4.6':
                self.ui.Rife_Model.setCurrentText(f'{model}')