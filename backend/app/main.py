from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
# import os
# import shutil

app = FastAPI()

# WORKSPACE_DIR = "/workspace" #workspace to delete everytime someone calls this api.

#AS THIS CONTAINER IS HOSTED ON {RENDER} IT IS DIFFERENT COMPARED TO MANUALLY STARTING A NEW FRESH CONTAINER.
#THAT IS THE REASON WHY WE HAVE TO MANUALLY DELETE THE WORKSPACE FOLDER EVERYTIME SOMEONE HITS THIS API
#USUALLY WHILE CREATING A NEW SESSION

class Command(BaseModel):
    cmd : str

# def reset_workspace():
#     #checks if workspace exits or not 
#     os.makedirs(WORKSPACE_DIR , exist_ok=True)
#     #delete everything inside workspace
#     try:
#         if os.path.exists(WORKSPACE_DIR):
#             for filename in os.listdir(WORKSPACE_DIR):
#                 file_path = os.path.join(WORKSPACE_DIR , filename)
#                 if os.path.isfile(file_path) or os.path.islink(file_path):
#                     os.unlink(file_path) #delete file
#                 elif os.path.isdir(file_path):
#                     shutil.rmtree(file_path) #using shutil deltes the whole folder tree excepts the main folder in this case /workspace
#     except Exception as e:
#         print(f"Something went wrong : {str(e)}")

@app.post("/execute")

async def execute_command(command : Command):
    # reset_workspace() #clear workspace before executing.
    try:
        cmd = command.cmd.strip() #remove leading / trailing spaces
        if cmd.startswith("/") and " " not in cmd:
            cmd = cmd[1:]
        result = subprocess.run(
            cmd , shell=True , capture_output=True , text=True , timeout=5
        )
        return {"output" : result.stdout or result.stderr}
    except subprocess.TimeoutExpired:
        return {"output" : "Command timed out"}
    except Exception as e:
        return {"output" : str(e)}
    