from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Sample data
categories = [
    {"name": "Cake", "imgSrc": "cake.png", "ellipseImg": "ellipse-cake.png"},
    {"name": "Powder", "imgSrc": "powder.png", "ellipseImg": "ellipse-powder.png"},
    {"name": "Liquid", "imgSrc": "liquid.png", "ellipseImg": "ellipse-liquid.png"},
    {"name": "Scrubber", "imgSrc": "scrub.png", "ellipseImg": "ellipse-scrub.png"},
]

products = [
    {"imgSrc": "yellow.png", "altText": "Vinshine Detergent Soap - Green", "title": "Vinshine Detergent Soap - Green", "price": "₹999"},
    {"imgSrc": "pink.png", "altText": "Vinshine Detergent Soap - Pink", "title": "Vinshine Detergent Soap - Pink", "price": "₹999"},
    {"imgSrc": "green.png", "altText": "Vinshine Detergent Soap - Green", "title": "Vinshine Detergent Soap - Green", "price": "₹999"},
    {"imgSrc": "red.png", "altText": "Vinshine Detergent Soap - Red", "title": "Vinshine Detergent Soap - Red", "price": "₹999"},
    {"imgSrc": "lightGreen.png", "altText": "Vinshine Detergent Soap - Light Green", "title": "Vinshine Detergent Soap - Light Green", "price": "₹999"},
]

testimonials = [
    {"imageUrl": "testimonial1.png", "name": "Floyd Miles", "rating": ["full-star.png", "full-star.png", "full-star.png", "half-star.png", "empty-star.png"], "description": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet."},
    {"imageUrl": "testimonial2.png", "name": "Ronald Richards", "rating": ["full-star.png", "full-star.png", "full-star.png", "full-star.png", "empty-star.png"], "description": "ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet."},
    {"imageUrl": "testimonial3.png", "name": "Savannah Nguyen", "rating": ["full-star.png", "full-star.png", "full-star.png", "half-star.png", "empty-star.png"], "description": "Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet."},
]

latest_updates = [
    {"imageUrl": "people.png", "subHeading": "Sub Heading", "heading": "Heading", "linkUrl": "#read-more", "linkImageUrl": "arrow1.png"},
    {"imageUrl": "people.png", "subHeading": "Sub Heading", "heading": "Heading", "linkUrl": "#read-more", "linkImageUrl": "arrow1.png"},
    {"imageUrl": "people.png", "subHeading": "Sub Heading", "heading": "Heading", "linkUrl": "#read-more", "linkImageUrl": "arrow1.png"},
]

# Define response models
class Category(BaseModel):
    name: str
    imgSrc: str
    ellipseImg: str

class Product(BaseModel):
    imgSrc: str
    altText: str
    title: str
    price: str

class Testimonial(BaseModel):
    imageUrl: str
    name: str
    rating: List[str]
    description: str

class LatestUpdate(BaseModel):
    imageUrl: str
    subHeading: str
    heading: str
    linkUrl: str
    linkImageUrl: str

@app.get("/categories", response_model=List[Category])
async def get_categories():
    return categories

@app.get("/products", response_model=List[Product])
async def get_products():
    return products

@app.get("/testimonials", response_model=List[Testimonial])
async def get_testimonials():
    return testimonials

@app.get("/latest-updates", response_model=List[LatestUpdate])
async def get_latest_updates():
    return latest_updates

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
