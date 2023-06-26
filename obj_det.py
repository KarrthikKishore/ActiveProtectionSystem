import cv2
from yolov5.models import YOLOv5


# Load the YOLOv5 model
model = YOLOv5()

# Set the input size and output classes
#model.set_input_size(614)
#model.set_output_classes(['Aircraft', 'Helicopter ', 'Drone', 'Military Tank', 'Military Truck', 'UAV '])

# Open a video file or capture from camera
cap = cv2.VideoCapture(0)

# Loop over frames
while True:
    # Read a frame
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection
    boxes, labels, scores = model.forward(frame)

    # Draw boxes around the detected objects
    for box, label, score in zip(boxes, labels, scores):
        x1, y1, x2, y2 = box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(frame, f"{label}: {score:.2f}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
