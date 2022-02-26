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
    
@app.get("/sum_list")
def sum_list(list1: list):
    """Sum up the numbers in the input list"""

    total = 0
    for num in list1:
        total += num
    
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')