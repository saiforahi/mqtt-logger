import datetime
import json
import os
import sys
import glob


class FileMaster():
    log_base_path="logs/"
    def __init__(self,device_id:str,file_size:int=None):
        self.device_id= device_id
        self.file_size = file_size if file_size else 100  # file size in mb

    def set_reading_file(self,new_reading_file_name:str)->bool:
        try:
            self.reading_file_name=new_reading_file_name
            return True
        except Exception as e:
            print("set reading file name error",str(e))
            return False

    def get_file(self):
        try:
            pass
        except Exception as e:
            print(str(e))
            pass

    # function for writing log file
    def write_log_file(self, file_content:str=None) -> None:
        try:
            # checking if log directory exists or not
            if not os.path.isdir(self.log_base_path+self.device_id):
                os.makedirs(self.log_base_path+self.device_id)

            list_of_files = glob.glob(self.log_base_path+self.device_id+'/*.dat', recursive=True)

            if len(list_of_files)<=0:
                path=self.log_base_path+self.device_id+"/"+self.device_id+"_"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".dat"
                print(type(path))
                with open(path, "w") as file:
                    file.write(file_content+"\n")
                    file.close()
            else:
                latest_file = max(list_of_files, key=os.path.getctime)
                file_stats = os.stat(latest_file)
                file_size = file_stats.st_size / (1024 * 1024)
                print(latest_file)
                if file_size <= self.file_size:
                    with open(latest_file, "a") as file:
                        file.write(file_content+"\n")
                        file.close()
                else:
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

    def read_reading_file(self,device_id=None):
        try:
            entries = os.scandir('readings/')
            for entry in entries:
                print(entry.name)
            pass
        except Exception as e:
            print(str(e))
            pass
