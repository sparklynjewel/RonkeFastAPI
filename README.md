This is a simple REST API. It returns basic profile information and a random cat fact from an external API.
## How to Run Locally


# Clone the repo
git clone https://github.com/sparklynjewel/RonkeFastAPI.git

# Navigate to the folder
cd RonkeFastAPI

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

# Visit in browser
http://127.0.0.1:8000/me

# Visit in browser after deplying- add /me at the back fo the url
https://ronkefastapi-production.up.railway.app/me