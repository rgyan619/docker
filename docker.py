# THE SOFTWARE THAT MAKES DOCKER EASY!!
import os
def running():
	os.system("docker ps -a")
	print("Want to remove the running OS (y/n) : ", end="")
	option = input()
	if str(option) == 'y':
		print("Enter the 'name of OS/ OS ID' :", end="")
		image = input()
		os.system("docker rm {}".format(image))
	else:
		print("Wanna to reopen the running OS (y/n) :  ", end="")
		option = input()
		if str(option) == 'y':
			print("Enter the (name of OS/ OS ID) :", end="")
			image = input()
			os.system("docker attach {}".format(image))

	input()
def opening():
	os.system("tput setaf 4")
	print("""                                                                       
	           ##.                         .##                                   	
	           ##.                         .##                                   	
	     .###. ##.     .##.        .##.    .##    .##       .##.        .###.	
	  .##     ###.  .##    ##.   .##   ##. .##   .##    .###    ###.  .##    ##.	
	.##        ##. .##      ##. .##        .######     .############. .##       	
	.##        ##. .##      ##. .##        .### .###   .##            .##       	
	 .##       ##.  .##    ##.  .##    ##. .##   .###   .##      ##.  .##      	
	    .#####.        .##.       .####.   .##     .##     .####.     .##       	""")
	os.system("tput setaf 0")
	print("\n\t\t\t\t<1>  Check installation")
	os.system("tput setaf 1")
	print("\t\t\t\t<2>  Start the Docker")
	os.system("tput setaf 2")
	print("\t\t\t\t<3>  Check the status")
	os.system("tput setaf 3")
	print("\t\t\t\t<4>  Check the Docker Images")
	os.system("tput setaf 4")
	print("\t\t\t\t<5>  Install the Docker Images")
	os.system("tput setaf 5")
	print("\t\t\t\t<6>  Run the Docker")
	os.system("tput setaf 6")
	print("\t\t\t\t<7>  Check the Running Docker")
	os.system("tput setaf 8")
	print("\t\t\t\t<8>  Stop the Docker")
	os.system("tput setaf 2")
	print("\t\t\t\t<exit> Exit()")
	os.system("tput setaf 7")
def open():
	os.system("tput setaf 4")
	print("""
                                               ########
                                               #      #
                                               #      #
                                #########11############             .
                                #      #       #      #           .# #.
                                #      #       #      #           #   #.
                         ######################00#############  .#     #.#.#.#.     
                         #      #      #       #      #      #  .#           #.    
                         #      #      #       #      #      #   .#        #.      
                    .#################################6###########       #.             
                   .#                                                 ##.
                   .#               .###.                            ##.
                    .##            .# # #.                         ##.
                     .##            .###.                         ##.
                      .#     .###                                ##.
                        .####                                  ##.
                          .#                                 ##.
                            .###############################.                          """)

open()
while True:
	opening()
	print("Enter your choice:  ",end="")
	num=input()
	if int(num) == 1:
		os.system("rpm -q docker-ce")
		input()
	elif int(num) == 2:
		os.system("setenforce 0")
		os.system("systemctl start docker")
		input()
	elif int(num) == 3:
		os.system("systemctl status docker")
		input()
	elif int(num) == 4:
		os.system("docker images")
		input()
	elif int(num) == 5:
		print("Enter the image name with its version:  ",end="")
		image=input()
		print("docker pull {}".format(image))
		input()
	elif int(num) == 6:
		print("Enter the name you wanna give to the container: ",end="")
		name=input()
		print("Enter the image with its version: ",end="")
		image=input()
		os.system("docker run -it --name {} {}".format(name,image))
		input()
	elif int(num) == 7:
		running()
	elif int(num) == 8:
		os.system("systemctl stop docker")
		input()
	else:
		print(" Your entered WRONG option!!\n\n")
		os.system("exit()")
	os.system("clear")	
