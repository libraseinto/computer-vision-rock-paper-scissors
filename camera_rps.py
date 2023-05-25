import cv2
from keras.models import load_model
import numpy as np
import time


def get_prediction():
    TIMER = 3
    model = load_model('keras_model.h5', compile=False)
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == ord('w'):
            prev = time.time()
            while TIMER >= 0:
                ret, frame = cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                org = (50, 50)
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2
                cv2.putText(frame, str(TIMER), org, font, fontScale, color, thickness, cv2.LINE_AA)
                cv2.imshow('frame', frame)
                cv2.waitKey(1)
                cur = time.time()
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER - 1
        # Press q to close the window
        print(prediction)
        max_arr = np.max(prediction)
        print(max_arr)
        max_arr_loc = np.argmax(prediction)
        print(max_arr_loc)
        if k == ord('q'):
            break
                
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    if max_arr_loc == 0:
        user_input = "rock"
    elif  max_arr_loc == 1:
        user_input = "scissors"
    elif  max_arr_loc == 2:
        user_input = "paper"
    else:
        user_input = "nothing"
    return user_input

print(get_prediction())


