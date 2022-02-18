import subprocess

subprocess.Popen('C:/Users/joshs/OneDrive/Documents/VNCViewer')
subprocess.call("plink -i /Users/joshs/OneDrive/Documents/Downloads/newkey.ppk kali@xx.xxx.xxx.xx sudo apt install xfce4 xfce4-goodies -y tightvncserver; sudo apt-get install gnome-core kali-defaults kali-root-login desktop-base -y; tightvncserver -geometry 1920x1080")
subprocess.call("plink -L 5901:localhost:5901 -N -i /Users/joshs/OneDrive/Documents/Downloads/newkey.ppk kali@xx.xxx.xxx.xx")
