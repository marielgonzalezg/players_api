# Players API

## What the App Does
This app provides information about professional tennis players, including their name, country, profile image, and a GIF representing them. The data is served as a JSON API that can be consumed by other applications, such as iOS apps.

## API Endpoint
The app exposes the following endpoint:

- `GET /players` — Returns a JSON array of player objects.  
- API Link: [https://players-api-n6ux.onrender.com/players](https://players-api-n6ux.onrender.com/players)

Each player object contains the following fields:
- `name` — Player's name  
- `imageUrl` — URL of the player's image  
- `country` — Player's country  
- `countryFlagUrl` — URL of the player´s country flag  
- `gifUrl` — GIF URL

## How to Run the App
- Python 3.9+
- pip (Python package manager)
- Xcode 15 or newer
- iOS 17 or newer (target)

## Clone Repository
- git clone https://github.com/marielgonzalezg/players_api.git
- cd players_api

### Example Response
```json
[
  {
    "name": "Rafael Nadal",
    "imageUrl": "https://example.com/nadal.jpg",
    "country": "Spain",
    "countryFlagUrl": "https://example.com/spain.png",
    "gifUrl": "https://example.com/nadal.gif"
  }
]

