from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello visitor!"}

@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}
    
@app.get("/cal_profit/{cost}/{revenue}")
def cal_profit(cost: float, revenue: float):
    """Given the cost and revenue, calculate the profit margin"""

    profit_margin = (revenue - cost)/revenue
    
    return {"profit_margin": profit_margin}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')