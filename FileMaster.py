import json
import os


class FileMaster():
    def __init__(self,reading_file_name:str=None,logging_file_name:str=None):
        self.reading_file_name = reading_file_name+".dat" if reading_file_name else "reading.dat"
        self.logging_file_name = logging_file_name+".dat" if logging_file_name else "log.dat"

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
    def write_log_file(self, file_content=None) -> None:
        try:
            # checking if log directory exists or not
            if not os.path.exists("log/"+self.logging_file_name):
                # creating log file
                with open("log/"+self.logging_file_name, "w") as file:
                    file.write(file_content)
                    file.close()
            else:
                # appending data to existing log file
                with open("log/"+self.logging_file_name,"a") as existing_log_file:
                    existing_log_file.writelines()

            pass
        except Exception as e:
            print(str(e))
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
                with open("readings/"+self.reading_file_name,"a") as existing_log_file:
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
