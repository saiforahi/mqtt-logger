import json
from FileMaster import FileMaster

if __name__ == '__main__':
    file_master=FileMaster(reading_file_name="reading1")
    content = [
        {'ID': 9060002205120008, 'Time_Stamp': '2023-02-15 10:07:02', 'Phase_A_Voltage': 226.7},
        {'ID': 9060002205120008, 'Time_Stamp': '2023-02-15 10:07:02', 'Phase_A_Voltage': 226.7},
    ]
    # writing
    file_master.write_reading_file(file_content=content)
    #reading
