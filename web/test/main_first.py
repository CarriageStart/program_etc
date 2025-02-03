from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from typing import List


class Stage(BaseModel):
    name: str
    description: str
    completed: bool


app = FastAPI()

# In-memory storage for stages
stages = []

@app.post("/stages/", response_model=Stage)
def create_stage(stage: Stage):
    stages.append(stage)
    return stage

@app.get("/stages/", response_model=List[Stage])
def get_stages():
    return stages

@app.get("/stages/{stage_id}", response_model=Stage)
def get_stage(stage_id: int):
    if stage_id >= len(stages) or stage_id < 0:
        raise HTTPException(status_code=404, detail="Stage not found")
    return stages[stage_id]

@app.put("/stages/{stage_id}", response_model=Stage)
def update_stage(stage_id: int, updated_stage: Stage):
    if stage_id >= len(stages) or stage_id < 0:
        raise HTTPException(status_code=404, detail="Stage not found")
    stages[stage_id] = updated_stage
    return updated_stage

@app.delete("/stages/{stage_id}")
def delete_stage(stage_id: int):
    if stage_id >= len(stages) or stage_id < 0:
        raise HTTPException(status_code=404, detail="Stage not found")
    stages.pop(stage_id)
    return {"message": "Stage deleted successfully"}

