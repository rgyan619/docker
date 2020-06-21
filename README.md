# docker
**INSTALL THE DOCKER**

NOTE: THIS PROGRAM IS ONLY VALID FOR REDHAD LINUX.
 
STEP 1. Go to this link https://download.docker.com/linux/centos/7/x86_64/stable/ 

STEP 2. Open your terminal and add this commmand **cd /etc/yum.repos.d/**

STEP 3. Add a file name **docker.repo** in **/etc/yum.repos.d/

STEP 4. Copy paste the code in that file -->>
        
    [docker]

    baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/

    gpgcheck=0

STEP 5. Save this file and run a command **yum install docker.ce --no best**

