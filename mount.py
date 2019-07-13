import os

print ("Welcome to MOunting \n")


print ("Ex : /home/username/iso/youriso.iso")
user = input("wanna make a Directory on /mnt/ file? ")
for user in"yes,y,ye":
	try:
		os.system("sudo mkdir /mnt/image")
		comm = ("sudo mount -o loop ")
		comm1 = input("Location : ")
		comm2 = (" /mnt/image")
		final = comm+comm1+comm2
		os.system(final)
	except:
		print ("Error!!")
	break
