####################################################################################
#
#   Importing required libraries
#
####################################################################################

import psutil
import sys
import os
import time
import schedule

##############################################################################################################################
#
#   Function Name : ProcessScan
#   Input         : None
#   Description   : Function Gathers details about every currently running process on your computer and returns them as a list
#   Date          : 25/07/2026
#   Author        : Himani Ramesh Salunkhe
#
###############################################################################################################################

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():                                          #used to iterate running/zombi processes
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess    
        
##################################################################################################################################################################################
#
#   Function Name : PlatformServilence
#   Input         : FolderName
#   Description   : function creates a timestamped system monitoring log file inside a specified folder, recording CPU, RAM, network usage, and details of all running processes.
#   Date          : 25/07/2026
#   Author        : Himani Ramesh Salunkhe
#
##################################################################################################################################################################################

def PlatformServilence(FolderName):
    Border = "-"*50
    Ret = False
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as foldername is existing but it is not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")              #string format time                  logfile is created in this code
    FileName = os.path.join(FolderName , "Marvellous_%s.log"%timestamp)


    fobj = open(FileName,"w")           #open with w will create it if not present or overwrite if present

    print(f"Log file gets successfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("-------Marvellous Platform Srvilence System------\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------System report--------------------\n")

    #cpu information
    fobj.write("Number of active cpu cores : %s\n"%psutil.cpu_count())
    fobj.write("CPU usage : %s %%\n"%psutil.cpu_percent())
    fobj.write(Border+"\n")

    #ram information
    memory = psutil.virtual_memory()            #there are two memories virtual and physical
    fobj.write("RAM usage : %s %%\n"%memory.percent)
    fobj.write("total RAM available : %s\n"%memory.total)
    fobj.write(Border+"\n")


    #Network usage
    netobj = psutil.net_io_counters()

    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    #process log
    data = ProcessScan()

    for info in data:
        fobj.write("PID : %s\n"%info.get("pid"))
        fobj.write("Name : %s\n"%info.get("name"))
        fobj.write("Username : %s\n"%info.get("status"))
        fobj.write("CPU Usage: %.2f\n"%info.get("cpu_percent"))
        fobj.write("RAM Usage : %.2f\n"%info.get("memory_percent"))

        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("---------------End of Log file-------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

####################################################################################
#
#   Function Name : main
#   Input         : Command line arguments
#   Description   : It controls the script
#   Date          : 25/07/2026
#   Author        : Himani Ramesh Salunkhe
#
####################################################################################

def main():
    
    Border = "-"*50
    print(Border)
    print("-------Marvellous Platform Srvilence System------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform")
            print("1 : It fetch the information of running processes")
            print("2 : It fetch the informtion about primary strorage of RAM")
            print("3 : It fetch the information about secondary storage as HDD")
            print("4 : It fetch the information about the microprocesssor")
            print("5 : It get auto sceduled periodically")
            print("6 : It maintains ll records into log file")
            print("7 : It sends log files thruogh mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")

        else:
            print("Unable to procees as there is no matching argument")
            print("Please use --h or --u for getting more details")             


    # actual project code
    elif(len(sys.argv)==3):
        print("Scheduler started successfully")
        print("Press Ctrl + C to abort utomation script")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformServilence,sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u for getting more details")        


    print(Border)
    print("------Thank you for using our Automation System------")
    print(Border)

####################################################################################
#
#   Starter of the automation script
#
####################################################################################

if __name__ == "__main__":
    main()    