import json
from FileMaster import FileMaster

if __name__ == '__main__':
    file_master=FileMaster(device_id="123",file_size=1)
    file_master.write_log_file(file_content=json.dumps({'ID': 9060002205120008, 'Time_Stamp': '2023-02-15 10:07:02', 'Phase_A_Voltage': 226.7}))
    #reading
