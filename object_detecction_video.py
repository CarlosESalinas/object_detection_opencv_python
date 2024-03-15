from functions import detect_object_video
import cv2
from classes import class_labels
from models import mobile_net_ssd_config

prototxt = mobile_net_ssd_config["prototxt"]
model = mobile_net_ssd_config["caffemodel"]

# classlabels
class_labels = class_labels

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt, model)
frame_path = 'videos/people.mp4'

detected_video = detect_object_video(frame_path, net, class_labels)

cv2.imshow("Detected Objects", detected_video)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
