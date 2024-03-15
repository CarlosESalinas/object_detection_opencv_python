import cv2
import numpy as np
from models import mobile_net_ssd_config
from classes import class_labels
from functions import detect_object_images

# Load the model configuration
prototxt = mobile_net_ssd_config["prototxt"]
model = mobile_net_ssd_config["caffemodel"]

# classlabels
class_labels = class_labels

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# Path to the image
image_path = 'images/dogs.jpeg'
# Detect the objects in the image
detected_image = detect_object_images(image_path, net, class_labels)
cv2.imshow("Detected Image", detected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

