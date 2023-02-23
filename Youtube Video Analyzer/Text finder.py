import cv2
import numpy as np
def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)
def ColourDistance(e1, e2):
  rmean = ( e1[0] + e2[0] ) / 2
  r = e1[0] - e2[0]
  g = e1[1] - e2[1]
  b = e1[2] - e2[2]
  return np.sqrt((((512+rmean)*r*r)/(2**8)) + 4*g*g + (((767-rmean)*b*b)/(2**8)))
def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
# read video from file
cap = cv2.VideoCapture('The Red Comet Returns! - Super Robot Wars X 37.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

print("Video properties: ")
print("Video dimensions: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Video Frame rate: ", cap.get(cv2.CAP_PROP_FPS))

file = open('button.txt',mode='r')
all_of_it = file.read()
file.close()
hex_array = all_of_it.split()
# Read until video is completed
reduce_repeat=False
second=0
while(cap.isOpened()):
  second+=1
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    # Display the resulting frame
    # cv2.imshow('Frame',frame)
    # np.savetxt('test.out', frame[:,:,(0,1,2)], delimiter=',') 
    # f = open("button.txt", "w")
    # f.write("")
    # f.close()
    # file = open("button.txt", "a")
    # print(hex_array)

    count=0
    found=False
    Array = frame[:,:,(0,1,2)]
    if second%int(29.97002986065788*5)==0:
      for y in range(9):
          for x in range(9):
            rgb = hex_to_rgb(hex_array[count].replace('#', ''))
            # Hex = rgb_to_hex(Array[720-(53+y)][145+x][0],Array[720-(53+y)][145+x][1],Array[720-(53+y)][145+x][2])
            # if(Hex!=hex_array[count]):
            #   boo=False
            value = ColourDistance(rgb,Array[720-(53+y)][145+x])
            if(value<5):
              # print("Found")
              found=True
              break
            count+=1
              # content = str(Hex)
          #     file.write(' ' + content)
          # file.write('\n')
          if(found): 
            break
          count+=27
      if(found and not reduce_repeat):
        # print(int(second/29.97002986065788))
        write_int=int(second/29.97002986065788)
        write_string=str(write_int)
        file = open("file1.txt", "a")
        file.write(write_string +'\n')
        file.close()
        reduce_repeat=True
      else:
        reduce_repeat=False
    # Saving the array in a text file
    # file.close()

    # Press Q on keyboard to  exit
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #   break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
