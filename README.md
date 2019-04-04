# Logs Analysis Project
The Logs Analysis project is a requirement to finish Udacity's Full Stack Nanodegree program. The task is to build an internal reporting tool that will use information from a PostgreSQL database to print out reports in plain text what the most popular three articles of all time are, who are the most popular authors of all time are, and on which days did more than 1% of requests lead to errors. The reporting tool is a Python program using the psycopg2 module to connect the database.

## Prepare The Software And Data
My operating system is Windows so the below information will reflect that. My preferred code editor is Atom. I will assume Python has been downloaded and installed already. Some of the necessary files, configurations, and data were provided by Udacity.

### Install Git
"C:\\Users\\Kendrick\\AppData\\Local\\atom\\atom.exe"
1. Go to https://git-scm.com/downloads
2. Download the software for Windows
3. Install Git choosing all of the default options
4. Download [udacity-terminal-config.zip](http://video.udacity-data.com.s3.amazonaws.com/topher/2017/March/58d31ce3_ud123-udacity-terminal-config/ud123-udacity-terminal-config.zip) and unzip.
5. You should have a folder titled "udacity-terminal-config". Go into the folder and take out "bash_profile" so the folder and "bash_profile" are in the same directory.
6. Right-click in an empty space where the folder and "bash_profile" are located and click on "Git Bash Here".
7. In Git, run the following:
```
cd
start .
```
8. Drag the "udacity-terminal-config" folder and bash_profile into the window that popped up.
9. In Git, run the following:
```
mv bash_profile .bash_profile
mv udacity-terminal-config .udacity-terminal-config
```
10. Re-open Git and run the following:
```
git config --global user.name "<Your-Full-Name>"
git config --global user.email "<your-email-address>"
git config --global color.ui auto
git config --global merge.conflictstyle diff3
git config --global core.editor "C:\\Users\\"<Username on your Computer>"\\AppData\\Local\\atom\\atom.exe"
git config --list
```
 
### Install Virtual Box
VirtualBox is software that runs virtual machines. Download it from [virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for Windows. No need to download the extension pack or the SDK.

### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for Windows.

### Download the VM configuration
1. Download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
2. Move the directory FSND-Virtual-Machine to a directory of your choosing if you want.
3. Download the [Vagrant file configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip) to replace the current Vagrant file.

### Download the data
Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will unzip this file and put the file "newsdata.sql" into the "vagrant" directory.

### Start the virtual machine
1. Run Git bash in the 'vagrant' directory or cd into it.
2. From your terminal, run the command:
```
vagrant up
```
3. When the above is finished running, run the command:
```
vagrant ssh
```
4. If your shell prompt starts with the word "vagrant", you're logged into your Linux VM.

### Load the data
In your terminal, created in the instructions above, run the following:
```
psql -d news -f newsdata.sql
```
 ### Run LogsAnalysis.py
 With the data loaded, download "LogsAnalysis.py" from my repo and put it in the "vagrant" directory. Run the following command:
 ```
 python LogsAnalysis.py
 ```
 or, if the above doesn't work
 ```
 python3 LogsAnalysis.py
 ```
 Compare the "LogsAnalysis.txt" in my repo to the one created in your "vagrant" directory".
