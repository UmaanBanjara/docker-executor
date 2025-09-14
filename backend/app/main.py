from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/execute")
async def execute_command(cmd : str):
    try:
        result = subprocess.run(cmd , shell=True , capture_output=True , text = True, timeout=5)
        return {"output" : result.stdout or result.stderr}
    except subprocess.TimeoutExpired:
        return {"output" : "Command timed out"}
    except Exception as e:
        return {"output" : str(e)}