import cv2
import time

def capture_photos(photo_count=20, interval=2, save_path='.'):
    # Initialize the webcam
    try:
        cap = cv2.VideoCapture(0)
    except :
        print
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        for i in range(photo_count):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print(f"Failed to grab frame {i}")
                break
            
            # Display the resulting frame
            cv2.imshow('Photo Capture', frame)
            
            # Save the captured frame
            photo_filename = f"{save_path}/photo_{i+1}.jpg"
            cv2.imwrite(photo_filename, frame)
            print(f"Photo {i+1} saved as {photo_filename}")
            
            # Wait for 2 seconds
            time.sleep(interval)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):  # If 'q' is pressed, exit early
                break
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

# Call the function
capture_photos()
