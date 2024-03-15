import cv2
import numpy as np

def detect_object_images(image_path, net, class_labels):

    '''
    Function to detect objects in an image
    params:
        - frame_path: path to the image
        - net: the model
        - class_labels: the class labels
    return:
        - image with the detected objects   
    '''

    # Read the image
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    
    # Resize the image
    image_resized = cv2.resize(image, (100, 100))
    
    # Create a blob from the image
    blob = cv2.dnn.blobFromImage(image_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5))
    
    # Print shapes
    
    print("Blob shape:", blob.shape)
    
    # Set input
    net.setInput(blob)
    
    # Forward pass
    detections = net.forward()
    
    # Loop over the detections
    for detection in detections[0][0]:
        if detection[2] > 0.45:
            label = class_labels[int(detection[1])]
            print("label: ", label)
            box = detection[3:7] * np.array([width, height, width, height])
            x_start, y_start, x_end, y_end = box.astype(int)
            cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
            cv2.putText(image, "Conf: {:.2f}".format(detection[2]*100), (x_start, y_start-5), 1, 1.2, (255,0,0), 2)
            cv2.putText(image, label, (x_start, y_start-25), 1, 1.2, (255,0,0), 2)
    
    return image    


def detect_object_video(frame_path, net, class_labels):

    '''
    Function to detect objects in a video
    params:
        - frame_path: path to the frame
        - net: the model
        - class_labels: the class labels
    return:
        - frame with the detected objects   
    '''

    # Read the video
    cap = cv2.VideoCapture(frame_path)
    
    # Loop over the frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break 
        height, width, _ = frame.shape 
        frame_resized = cv2.resize(frame, (100, 100))
        
        # Create a blob from the frame
        blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5))
        
        # Forward pass
        net.setInput(blob)
        detections = net.forward()

        # Loop over the detections
        for detection in detections[0][0]:
            if detection[2] > 0.45:
                label = class_labels[int(detection[1])]
                print("label: ", label)
                box = detection[3:7] * np.array([width, height, width, height])
                x_start, y_start, x_end, y_end = box.astype(int)
                cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
                cv2.putText(frame, "Conf: {:.2f}".format(detection[2]*100), (x_start, y_start-5), 1, 1.2, (255,0,0), 2)
                cv2.putText(frame, label, (x_start, y_start-25), 1, 1.5, (0,255,255), 2)
        
        cv2.imshow("Detected Objects", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Break the loop if the 'q' key is pressed
    
    cap.release()
    cv2.destroyAllWindows()