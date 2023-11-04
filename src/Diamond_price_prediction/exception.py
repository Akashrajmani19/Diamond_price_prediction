import sys

class CustomException(Exception):
    def __init__(self,error_massage,error_details):
        self.error_massage = error_massage
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno   # tb = traceback
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f"Error occured in python script name {self.file_name} line no. {self.lineno} error massage : {self.error_massage}"
    
if __name__ == "__main__":
    try :
        a = 1/0
        
    except Exception as e:
        raise CustomException(e,sys)