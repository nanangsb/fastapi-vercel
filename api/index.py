from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str = None
    available: bool = True

# Contoh data item
items = {
    1: {"name": "Pena", "price": 3.50, "description": "Pena tinta biru", "available": True},
    2: {"name": "Buku Catatan", "price": 5.00, "description": "Buku catatan kecil", "available": False},
    3: {"name": "Lampu Meja", "price": 12.99, "description": "Lampu meja LED", "available": True},
}

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items.get(item_id, {"message": "Item not found"})

@app.post("/items/")
async def create_item(item: Item):
    item_id = max(items.keys()) + 1
    items[item_id] = item.dict()
    return items[item_id]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id].update(item.dict())
        return items[item_id]
    return {"message": "Item not found"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    return {"message": "Item not found"}
