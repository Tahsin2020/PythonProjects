# Open a file: file
file = open('file1.txt',mode='r')
 
# read all lines at once
all_of_it = file.read()
 
# close the file
file.close()

string_array = all_of_it.split()
number_array=[]

for string in string_array:
    number_array.append(int(string))

new_number_array=[]

new_number_array.append(number_array[0])

for i in range(len(number_array)-2):
    if(number_array[i+1]+10==number_array[i+2]) and (number_array[i]+10==number_array[i+1]):
        new_number_array.append(0)
    if not (number_array[i+1]+10==number_array[i+2]) or not (number_array[i]+10==number_array[i+1]):
        new_number_array.append(number_array[i+1])
    # if(number_array[i]==0):
    #     number_array[i+1]=-1

print(number_array)
print(new_number_array)

file = open("timings.txt", "a")

for i in range(len(new_number_array)):
    if(new_number_array[i]!=0):
        seconds = new_number_array[i]
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        # print("%d:%02d:%02d" % (hour, minutes, seconds))
        str = (" %d:%02d:%02d " % (hour, minutes, seconds))
        file.write(str)
    else:
        file.write('-')

file.close()