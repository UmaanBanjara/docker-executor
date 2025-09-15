from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class Command(BaseModel):
    cmd : str

@app.post("/execute")

async def execute_command(command : Command):
    try:
        result = subprocess.run(
            command.cmd , shell=True , capture_output=True , text=True , timeout=5
        )
        return {"output" : result.stdout or result.stderr}
    except subprocess.TimeoutExpired:
        return {"output" : "Command timed out"}
    except Exception as e:
        return {"output" : str(e)}