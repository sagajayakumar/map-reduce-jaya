input1 = open("01mapperOutput.txt","r")  # open file, read-only
output = open("sortoutput.txt", "w") # open file, write
lines = input1.readlines()
#lines.sort()
lines.sort(key=lambda x:x[2])

for line in lines:
	output.write(line)

input1.close()
output.close()
