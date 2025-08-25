# Players API

## What the App Does
This app provides information about professional tennis players, including their name, country, profile image, and a link to a GIF representing them. The data is served as a JSON API that can be consumed by other applications, such as iOS apps.

## API Endpoint
The app exposes the following endpoint:

- `GET /players` — Returns a JSON array of player objects.
- Example: [http://localhost:5001/players](http://localhost:5001/players) (for local testing)

Each player object contains the following fields:
- `name` — Player's name
- `imageName` — Local image file name
- `pais` — Player's country
- `paisimagen` — Country image name
- `link` — GIF URL

## How to Run the App
### Requirements
- Xcode 15 or newer
- iOS 17 or newer (target)

### Steps
1. Clone this repository:

```bash
git clone https://github.com/marielgonzalezg/players_api.git
cd players_api

