from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel
from graphviz import Digraph
import random

class Product(BaseModel):
    id: int
    stage: int

class Stage(BaseModel):
    name: str
    description: str
    completed: bool

app = FastAPI()

# In-memory storage for stages and products
stages = []
products = []

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

# 테스트 데이터 생성
def create_test_data(num_products: int, num_stages: int) -> List[Product]:
    products = []
    for i in range(num_products):
        stage = random.randint(1, num_stages)
        products.append(Product(id=i+1, stage=stage))
    return products

products = create_test_data(100, 10)

# Flow Chart 생성 함수
def create_flow_chart(products: List[Product], num_stages: int):
    dot = Digraph()

    for stage in range(1, num_stages + 1):
        stage_products = [p.id for p in products if p.stage == stage]
        label = f"Stage {stage}\nProducts: {', '.join(map(str, stage_products))}"
        dot.node(f"Stage {stage}", label)

    for stage in range(1, num_stages):
        dot.edge(f"Stage {stage}", f"Stage {stage + 1}")

    return dot

@app.get("/flow-chart", response_class=HTMLResponse)
def get_flow_chart():
    flow_chart = create_flow_chart(products, 10)
    flow_chart_path = flow_chart.render("flow_chart", format="svg", cleanup=True)
    
    with open(flow_chart_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
        
    html_content = f"""
    <html>
        <body>
            {svg_content}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

