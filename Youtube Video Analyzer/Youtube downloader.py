from pytube import YouTube 
import datetime
  
#where to save  
# DOWNLOAD_PATH = "D:/Users/User/NewFolder" #to_do  
  
#link of the video to be downloaded 
# link=["https://www.youtube.com/watch?v=xWOoBJUqlbI", 
#     "https://www.youtube.com/watch?v=xWOoBJUqlbI"
#     ]
videos= "https://www.youtube.com/watch?v=YKRBm8z71FY&list=PLuZ5BJr2xfE2-hHXbZwZm5wJleNBrIk3d&index=77 https://www.youtube.com/watch?v=HrYenNgcdwk&list=PLuZ5BJr2xfE2-hHXbZwZm5wJleNBrIk3d&index=78 https://www.youtube.com/watch?v=SXNTXXfdKe4&list=PLuZ5BJr2xfE2-hHXbZwZm5wJleNBrIk3d&index=79 https://www.youtube.com/watch?v=15s4aw8Q3Q0&list=PLuZ5BJr2xfE2-hHXbZwZm5wJleNBrIk3d&index=80 "
split_videos= videos.split()
sep = '&list'
for i in range(len(split_videos)):
    split_videos[i] = split_videos[i].split(sep, 1)[0]
link = split_videos
# print(link[0])
  
# try:  
#     # creating youtube object using YouTube  
#     youtube_obj = YouTube(link[0])  
# except:  
#     print("Connection Error") #to handle exception  
# # filters out all the files with "mp4" extension  
# mp4files = youtube_obj.streams.filter('mp4')  
# #to set the name of the file  
# youtube_obj.set_filename('Downloaded Video')  
# # get the video with the extension and  
# # resolution passed in the get() function  
# d_video = youtube_obj.get(mp4files[-1].extension,mp4files[-1].resolution)  
# try:  
#     # downloading the video  
#     d_video.download(DOWNLOAD_PATH)  
# except:  
#     print("The is Some Error!")  
# print('Task is Completed!')  


# from pytube import YouTube
print(link)
for links in link:
    print(links)
    begin = datetime.datetime.now()
    print ("Begin date and time: ")
    print (begin.strftime("%Y-%m-%d %H:%M:%S"))
    YouTube(links).streams.first().download()
    yt = YouTube(links)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    begin = datetime.datetime.now()
    print ("End date and time: ")
    print (begin.strftime("%Y-%m-%d %H:%M:%S"))
