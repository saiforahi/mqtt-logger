import datetime
import json
import os
import sys
import glob


class FileMaster():
    log_base_path="logs/" # log dir base relative path
    def __init__(self,device_id:str,file_size:int=None): # FileMaster class constructor
        self.device_id= device_id # IOT device ID
        self.file_size = file_size if file_size else 100  # file size in mb

    def set_device_id(self,new_device_id:str)->bool: # device ID setter function
        try:
            self.device_id=new_device_id # setting new device ID
            return True
        except Exception as e:
            print("set reading file name error",str(e))
            return False

    def get_device_id(self)->str: # device ID getter function which returns string type
        try:
            return self.device_id
            pass
        except Exception as e:
            print(str(e))
            pass

    # function for writing log file
    def write_log_file(self, file_content:str=None) -> None: # log file writer function
        try:
            # checking if log directory exists or not
            if not os.path.isdir(self.log_base_path+self.device_id):
                os.makedirs(self.log_base_path+self.device_id)
            # listing all files in device log sub-directory
            list_of_files = glob.glob(self.log_base_path+self.device_id+'/*.dat', recursive=True)

            if len(list_of_files)<=0:
                # writing new file in the case of no previous log
                # generating file name with relative path
                path=self.log_base_path+self.device_id+"/"+self.device_id+"_"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".dat"
                with open(path, "w") as file:
                    file.write(file_content+"\n") # write line to file
                    file.close() # file closes
            else:
                #checking last log file size before appending or writing new one
                latest_file = max(list_of_files, key=os.path.getctime)
                file_size = os.stat(latest_file).st_size / (1024 * 1024) # latest log file size in MB
                if file_size <= self.file_size:
                    # appending to last log file
                    with open(latest_file, "a") as file:
                        file.write(file_content+"\n")
                        file.close()
                else:
                    # writing to new log file in the case of exceeding file size limit
                    path = self.log_base_path + self.device_id + "/" + self.device_id + "_" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".dat"
                    with open(path, "w") as file:
                        file.write(file_content + "\n")
                        file.close()

            pass
        except Exception as e:
            err='on line {}'.format(sys.exc_info()[-1].tb_lineno), str(e)
            print(err)
            pass

    # function for writing "reading" file
    def write_reading_file(self, file_content: list = None) -> None:
        """
        :param file_content:
        """
        try:
            if not os.path.isdir("readings"):
                os.makedirs("readings")
            # checking if reading directory exists or not
            if not os.path.exists("readings/"+self.reading_file_name):
                with open("readings/"+self.reading_file_name, "w") as file:
                    for item in file_content:
                        file.write(json.dumps(item)+"\n")
                    file.close()
                    print("File "+self.reading_file_name+" has been written")
            else:
                file_stats = os.stat("readings/" + self.reading_file_name)
                file_size = file_stats.st_size / (1024 * 1024)

                with open("readings/"+self.reading_file_name,"a" if file_size <= self.file_size else "w") as existing_log_file:
                    for item in file_content:
                        existing_log_file.write(json.dumps(item)+"\n")
                    existing_log_file.close()
                    print("File " + self.reading_file_name + " has been updated")


            pass
        except Exception as e:
            print(str(e))
            pass

    # log files getter function
    def read_log_files(self,device_id=None):
        try:
            entries = os.scandir(self.log_base_path)
            for entry in entries:
                print(entry.name)
            pass
        except Exception as e:
            print(str(e))
            pass
