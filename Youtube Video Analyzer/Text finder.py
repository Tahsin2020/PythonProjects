import cv2
import numpy as np

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
# read video from file
cap = cv2.VideoCapture('The Red Comet Returns! - Super Robot Wars X 37.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

file = open('button.txt',mode='r')
all_of_it = file.read()
file.close()
hex_array = all_of_it.split()
# Read until video is completed
second=0
while(cap.isOpened()):
  second+=1
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    # np.savetxt('test.out', frame[:,:,(0,1,2)], delimiter=',') 
    # f = open("button.txt", "w")
    # f.write("")
    # f.close()
    # file = open("button.txt", "a")
    # print(hex_array)

    count=0
    boo=True
    Array = frame[:,:,(0,1,2)]
    for y in range(36):
        for x in range(36):
          Hex = rgb_to_hex(Array[720-(53+y)][145+x][0],Array[720-(53+y)][145+x][1],Array[720-(53+y)][145+x][2])
          if(Hex!=hex_array[count]):
            boo=False
          count+=1
            # content = str(Hex)
        #     file.write(' ' + content)
        # file.write('\n')
    if(boo):
      print(second)
    # Saving the array in a text file
    # file.close()
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()