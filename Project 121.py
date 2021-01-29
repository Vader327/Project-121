import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
image = cv2.imread("hotel_room.jpg") 

while (cap.isOpened()):
  ret, img = cap.read()

  img = cv2.resize(img, (640, 480)) 
  image = cv2.resize(image, (640, 480)) 

  if not ret:
    break
  
  img = np.flip(img, axis=1)

  upper_black = np.array([110, 110, 110], np.uint8) 
  lower_black = np.array([0, 0, 0], np.uint8)

  mask = cv2.inRange(img, lower_black, upper_black)
  res = cv2.bitwise_and(img, img, mask = mask)
  
  final = img - res
  final = np.where(final == 0, image, final)
  
  output_file.write(final)
  cv2.imshow("Output", final)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
