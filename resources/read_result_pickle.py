# -*- coding: utf-8 -*-
"""
Created on Mon March 3 08:39:57 2019

@author: Marcus

Reads pickle file generated as part of the eye tracker output.
The pickle contains (in case recorded) information about the eye tracker,
the calibration/validation results, 
synchronization data, eye-tracker data, 
messages, and eye images (if recorded).

"""
import cPickle as pickle
from cStringIO import StringIO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import moviepy.editor as mpy
import os


EYE_IMAGE_SIZE_PIX = (175, 496)
EYE_IMAGE_SIZE_PIX_FULL_FRAME = (512, 640)
    
f = open("testfile.pkl", 'rb')
gaze_data_container = pickle.load(f)
msg_container = pickle.load(f)
external_signal_container = pickle.load(f)
sync_data_container = pickle.load(f)
stream_errors_container = pickle.load(f)
image_data_container = pickle.load(f)
calibration_history = pickle.load(f)
system_info = pickle.load(f)
settings = pickle.load(f)
python_version = pickle.load(f)
f.close()
            
            
#%% Save eye images to file
list_of_images = []
for i, eye_image in enumerate(image_data_container):
    
    ''' eye_image is a dict with keys
    device_time_stamp
 	Gets the time stamp according to the eye tracker's internal clock. 
 
 	system_time_stamp
 	Gets the time stamp according to the computer's internal clock. 
 
 	camera_id
 	Gets which camera generated the image. 
 
 	image_type
    Gets the type of eye image as a string.
    Valid values are EYE_IMAGE_TYPE_FULL and EYE_IMAGE_TYPE_CROPPED.
 
 	image_data
 	Gets the image data sent by the eye tracker in GIF format. 
    '''
    
    # Get time stamps
    print(eye_image['system_time_stamp'], eye_image['device_time_stamp'],
          eye_image['camera_id'])
    
    # Convert image to numpy array
    temp_im = StringIO(eye_image['image_data'])
    tim = Image.open(temp_im)
    tim.save(os.getcwd() + os.sep + 'images' + os.sep + str(eye_image['system_time_stamp']) + ".gif","GIF")

