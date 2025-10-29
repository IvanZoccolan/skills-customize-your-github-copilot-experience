from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI(title="Item API", description="A simple REST API for managing items")

# TODO: Define your Pydantic model here
# Create a model for your resource (e.g., Item) with appropriate fields and validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: Optional[float] = None

# TODO: Set up data storage
# You can use an in-memory list or implement file-based persistence
items_db: List[Item] = []
next_id: int = 1

# TODO: Implement GET endpoint to retrieve all items
@app.get("/items", response_model=List[Item])
def get_all_items():
    """Retrieve all items"""
    return items_db

# TODO: Implement GET endpoint with path parameter to retrieve a specific item
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    """Retrieve a specific item by ID"""
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

# TODO: Implement POST endpoint to create a new item
@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    """Create a new item"""
    global next_id
    item.id = next_id
    next_id += 1
    items_db.append(item)
    return item

# TODO: Implement PUT endpoint to update an existing item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: Item):
    """Update an existing item"""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            item_update.id = item_id
            items_db[i] = item_update
            return item_update
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

# TODO: Implement DELETE endpoint to remove an item
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Delete an item"""
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

# TODO: Run the server with: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
