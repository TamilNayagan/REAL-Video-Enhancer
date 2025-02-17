import os
homedir = os.path.expanduser(r"~")
import src.programData.thisdir
thisdir = src.programData.thisdir.thisdir()
from PyQt5.QtGui import QIcon
def show_scene_change_help(self):
    self.showDialogBox('1 is the most sensitive, detecting the most frame changes in a scene.\n9 is the least sensitive, detecting fewest frame changes in a scene.')

def show_on_no_output_files(self):
    self.showDialogBox('Output frames or Audio file does not exist. Did you accidently delete them?',True)

def no_input_file(self):
    self.showDialogBox("No input file selected.",True)

def encoder_help(self):
    self.showDialogBox(".h264 is more standardized, but has worse quality. (shorter render time) \n.h265 is less standardized, but retains more visual quality. (longer render time)")

def cannot_detect_vram(self):
    self.showDialogBox("Cannot detect vram amount, please set this value in settings for increased performance.\nIf you are on integrated graphics, consider leaving this value at 1.",True)

def no_downloaded_models(self):
    self.showDialogBox("No models selected, please select at least one model to download.",True)

def failed_download(self):
    self.showDialogBox("Failed to download dependencies, please check your connection and try again.",True)

def image_help(self):
    self.showDialogBox("Extraction and render image type.\nJPG (recommended) lossy, low file size.\nPNG (longer render time) lossless, high file size.\nWEBP (longest render time) lossless, low file size.")

def vram_help(self):
    self.showDialogBox("GPU Threading for the app. \nChanging this alters the amount of VRAM usage.\n2 Is usually fine for most senarios, but if you find that your GPU is not being utilized, try increasing it.")

def quotes(self):
    self.showDialogBox("Filenames with Quotes are not supported, please rename the file and try again.")

def not_enough_storage(self,predicted_space,total_space):
    return self.showQuestionBox(f"Insufficient space for render.\nConsider using a more compressed image format, lowering enhancement iterations, changing the render folder disk, or switching to the Optimized Render Type.\nTotal space predicted for render: {int(predicted_space)} GB.\nTotal space left on disk: {int(total_space)} GB.\nContinue?")

def not_enough_output_storage(self,predicted_space,total_space):
    return self.showQuestionBox(f"Insufficient space for Output file.\n Consider changing the output folder disk.\nTotal space predicted for render: {int(predicted_space)} GB.\nTotal space left on disk: {int(total_space)} GB.\nContinue?")

def model_warning(self):
    return self.showQuestionBox(f"Will remove all unselected models.\nContinue?")

def render_help(self):
    self.showDialogBox("The classic method consumes a significant amount of storage due to its inability to clear rendered frames.\n\nOptimized involves dividing the rendering process into smaller segments, each containing a predetermined number of frames. These segments are then compressed and merged into individual video segments. This approach effectively conserves storage space while maintaining video quality.")

def frame_increments_help(self):
    self.showDialogBox(f"This is how many frames will be rendered before they are merged into a video. (OPTIMIZED PRESET ONLY)\nLower values can lead to more storage usage as merging the video may take longer than the next render to run.\nHigher values can lead to more storage usage as there are more frames rendered before merging.\n(You usually want this on Automatic)")

def not_a_video(self):
    self.showDialogBox("This file is not a valid video.")

def not_valid_link(self):
    self.showDialogBox("This link is invalid.")

def not_enough_vram(self):
    self.showPopup("Your GPU does not meet the minimum required VRAM amount.\nMinimum: 4GB\nRecommended: 8GB\n It is highly advised to use Rife-V4 models and refrain from interpolating in resolutions past 1080p.",self.ignore_vram_popup)
def too_large_video(self):
    self.showDialogBox('WARNING: The video you have chosen exceeds the maximum resolution (3840x2160).\nThis could cause issues in the render!')
def restart_app(self):
    self.showDialogBox("Please restart app for changes to take effect.")
def no_perms(self):
    self.showDialogBox(f"No permissions to write here, please select a different directory or the default Output directory will be {homedir}/Videos")

def no_perms_render(self):
    self.showDialogBox(f"No permissions to write here, please select a different directory or the default Render directory will be {thisdir}")

def no_perms_change_setting(self):
    self.showDialogBox("No permissions to write here, please select a different directory.")

def no_perms_anywhere(self,dir=thisdir):
    self.showDialogBox(f"No permissions to write to {dir}, please select a directory in settings!!!!!")

def notAModel(self):
    self.showDialogBox(f"Not a valid model, please select a different file.")

def alreadyModel(self):
    self.showDialogBox(f"Same model found in models directory, please rename it to a different model.")

def already_Render_folder(self):
    return self.showQuestionBox(f"render folder already exists within directory, this can lead to overwriting of files within this directory.\nSet directory anyway?")

def ensembleModelDoesntExist(self):
    self.showDialogBox('Ensemble model does not exist, please click Install/Remove models to download the ensemble version. Using the regular model instead.')

def ensemble_help(self):
    self.showDialogBox('Ensemble interpolates a single frame twice, leading to a better result, but the render will take twice as long.')

def uninstallMessage(self):
    return self.showQuestionBox(f"Will remove EVERYTHING.\nContinue?")

def transition_detection_lossless_warning(self):
    self.showDialogBox('Transition detection is currently unsupported with Lossless encoding.')

def outdated_binary(self,binary):
    self.showDialogBox(f'Outdated {binary} binary, click on Install/Remove in the Manage Models settings menu to download the latest binary and use newer models!')

def UHDModeHelp(self):
    self.showDialogBox(f'UHD mode allows for flow to be calculated at a lower resolution, hopefully saving on VRAM.\nThis cutoff resolution means that anything greater than it will enable UHD mode, and lower threading on the GPU.')

def GPUIDHelp(self):
    self.showDialogBox(f'GPU ID selects what GPU to use. Usually, 0 is the best option, as ncnn generally selects the dedicated GPU.\nIf you are in a dual-gpu setup, you can set this to 1 if the render does not seem to be using the right GPU.\n-1 option means it uses CPU inference.')

def cantDetectUpscaleTimes(self):
    self.showDialogBox(f'Could not detect the current custom model\'s upscale multiplier.\nPlease select the correct one manually.')