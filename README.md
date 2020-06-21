# docker
**INSTALL THE DOCKER**
NOTE: THIS PROGRAM IS ONLY VALID FOR REDHAD LINUX.
Step 1. Go to this link https://download.docker.com/linux/centos/7/x86_64/stable/Packages/
Step 2. Open your terminal and add this command **cd /etc/yum.repos.d/ **
Step 3. Add a file name **docker.repo** in /etc/yum.repos.d
Step 4. Copy paste this code in that file -->
          **[docker]**
          **baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/ **
          **gpgcheck=0**
          and save it.
Step 5. Run this command **yum install docker-ce --nobest**
Step 6. Wait till the docker install in your system and for verification use this command 
          ** rpm -q docker-ce **

**RUN THE SCRIPT**
  
