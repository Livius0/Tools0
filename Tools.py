import os
import time
import shutil
import tempfile
import winreg
chiave =''
chiave2=''
valore=''
ram=''
while chiave != '0':
    chiave = input("Tell me which Windows you want to activate:\n1 Home\n2. Pro\n3. Edu\n4. Enterprise\n5. Workstation\n6. Remove 'Activate Windows' only (requires restart)\n7. Settings to restore Windows\n8. Activate Office 2021\n9. Restore changes from setting 8\n10. Reduce CPU processes\n11. Clean Temp\n0. Close the program\n")
    if chiave == '1':
        chiave = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
        try:
            time.sleep(1)
            os.system(f"slmgr /ipk {chiave}")
            time.sleep(1)
            os.system("slmgr /skms kms8.msguides.com")
            time.sleep(1)
            os.system("slmgr /ato")
            time.sleep(1)
            print("Activated\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
        time.sleep(1)
    elif chiave == '2':
        chiave = "W269N-WFGWX-YVC9B-4J6C9-T83GX"
        try:
            time.sleep(1)
            os.system(f"slmgr /ipk {chiave}")
            time.sleep(1)
            os.system("slmgr /skms kms8.msguides.com")
            time.sleep(1)
            os.system("slmgr /ato")
            time.sleep(1)
            print("Activated\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
        time.sleep(3)
    elif chiave == '3':
        chiave = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
        try:
            time.sleep(1)
            os.system(f"slmgr /ipk {chiave}")
            time.sleep(1)
            os.system("slmgr /skms kms8.msguides.com")
            time.sleep(1)
            os.system("slmgr /ato")
            time.sleep(1)
            print("Activated\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
        time.sleep(3)
    elif chiave == '4':
        chiave = "NPPR9-FWDCX-D2C8J-H872K-2YT43"
        try:
            time.sleep(1)
            os.system(f"slmgr /ipk {chiave}")
            time.sleep(1)
            os.system("slmgr /skms kms8.msguides.com")
            time.sleep(1)
            os.system("slmgr /ato")
            time.sleep(1)
            print("Activated\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
    elif chiave == '5':
        chiave = "NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J"
        try:
            time.sleep(1)
            os.system(f"slmgr /ipk {chiave}")
            time.sleep(1)
            os.system("slmgr /skms kms8.msguides.com")
            time.sleep(1)
            os.system("slmgr /ato")
            time.sleep(1)
            print("Activated\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
    elif chiave == '6':
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSET\Services\svsvc", 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "start", 0, winreg.REG_DWORD, 4)
            winreg.CloseKey(key)
            time.sleep(1)
            print("Done. Restart the PC.\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
    elif chiave == '7':
        try:
            os.system(f"slmgr.vbs /upk")
            time.sleep(1)
            print("Key removed. Now go to Settings\\Activation to enter another one.\n")
            time.sleep(1)
            os.system(f"slmgr.vbs /ckms")
            time.sleep(1)
            print("server connection removed.\n")
            time.sleep(1)
            os.system('reg query "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform" /v BackupProductKeyDefault')
            time.sleep(1)
            print("Here are the keys. If you don't see them, use another setting to activate Windows.\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
    elif chiave == '8':
        try:
            os.chdir(os.path.join(os.environ['ProgramFiles'], 'Microsoft Office', 'Office16'))
            time.sleep(1)
            os.system("for /f %x in ('dir /b ..\\root\\Licenses16\\ProPlus2021VL_KMS*.xrm-ms') do cscript ospp.vbs /inslic:\"..\\root\\Licenses16\\%x\"")
            time.sleep(1)
            os.system("cscript ospp.vbs /setprt:1688")
            time.sleep(1)
            os.system("cscript ospp.vbs /unpkey:6F7TH >nul")
            time.sleep(1)
            os.system("cscript ospp.vbs /inpkey:FXYTK-NJJ8C-GB6DW-3DYQT-6F7TH")
            time.sleep(1)
            os.system("cscript ospp.vbs /sethst:107.175.77.7")
            time.sleep(1)
            os.system("cscript ospp.vbs /act")
            print("Activated\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
    elif chiave == '9':
        try:
            os.chdir(os.path.join(os.environ['ProgramFiles'], 'Microsoft Office', 'Office16'))
            time.sleep(1)
            os.system("cscript ospp.vbs /unpkey:FXYTK >nul")
            time.sleep(1)
            os.system("cscript ospp.vbs /remhst")
            time.sleep(1)
            print("Removed all changes.\n")
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")
    elif chiave == '10':
        ram= input ("tell me how much RAM you have:")
        ram= int(ram)
        valore= 0 
        if ram < 4:
            print("Minimum 4 GB of RAM")
        elif ram == 4 :
            valore = 400000
            print("OK, restart the PC")
            time.sleep(1)
        elif ram == 6 :
            valore = 600000
            print("OK, restart the PC")
            time.sleep(1)
        elif ram == 8 :
            valore = 800000
            print("OK, restart the PC")
            time.sleep(1)
        elif ram == 16 :
            valore = 1000000
            print("OK, restart the PC")
            time.sleep(1)
        elif ram == 24 :
            valore = 1800000
            print("ok riavvia il pc")
            time.sleep(1)
        elif ram == 32 :
            valore = 2000000
            print("OK, restart the PC")
            time.sleep(1)
        elif ram == 64 :
            valore = 4000000
            print("OK, restart the PC")
            time.sleep(1)
        else:
            print("Invalid RAM. Try the one that is closest to your RAM(4gb,6gb,8gb,16gb,24gb,32gb,64gb).")
            exit(1)

        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSET\Control", 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "SvcHostSplitThresholdInKB", 0, winreg.REG_SZ, str(valore))
            winreg.CloseKey(key)
            time.sleep(1)
            time.sleep(3)
        except Exception as e:
            print(f"Errore: {e}")

    elif chiave == '11':
        def clean_system_temp_folder():
            system_temp_dir = "C:\\Windows\\Temp" 

            for root, dirs, files in os.walk(system_temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        print(f"File Removed: {file_path}")
                    except Exception as e:
                        print(f"Errore durante la rimozione del file {file_path}: {e}")

                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        shutil.rmtree(dir_path)
                        print(f"Folder Removed: {dir_path}")
                    except Exception as e:
                        print(f"Error deleting Folder {dir_path}: {e}")

        if __name__ == "__main__":
            clean_system_temp_folder()
        time.sleep(5)

        def clean_temp_folders():
            temp_dir = tempfile.gettempdir()
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception as e:
                        print(f"Error deleting file: {file}: {e}")

            print("Cleanup completed successfully!")

        if __name__ == "__main__":
            clean_temp_folders()
            
        time.sleep(5)
        
    elif chiave == '0':
        break
    else:
        print("Enter a number\n")
        time.sleep(1)
        continue
