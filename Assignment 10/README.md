# Assignment 10

## Author
Brenna Auker

*With help with Github Copilot & ChatGPT*

## Class
ITEC 5025

## Important notes

This chatbot uses postgres. I use a dockerfile for my postgres database but didn't include it here. It is just a basic docker image of pgvector/pg:17. I can if needed proved the docker compose needed. It doesn't need to be pgvector but I am also using this image for a personal project that uses PGVector. 

Thank you for the feedback in Week 8. This works a lot better I think and I am getting better results I think in general for what I want to use this for. 

## How to Run

1. Navigate to the project directory:
   ```bash
   cd "Assignment 10"
   ```

2. Install Requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Run the training code:
   ```bash
   python process_data.py
   ```

   If this fails, delete `processed_convo_data.csv`, `vectorized.keras`, `chatbot_model.keras`

4. Run the main application:
   ```bash
   python index.py
   ```

## Noted Issues

- FIXED ~~Doesn't get some more generalized requests. Need to work on that a bit more with the data~~
- Doesn't always get the title unless it's in Quotes. Might want to fix that for myself
- FIXED ~~If it finds multiples of something, updates multiples~~
- FIXED ~~Display better infomration when items are found~~
- Over trained model a bit I think. (Oh I did. Been reading about how to fix this but not a huge issue right now.)
- FIXED ~~Add confidence check. Below 80% ask the user again.~~