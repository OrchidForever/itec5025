# Assignment 9

## Author
Brenna Auker

*With help with Github Copilot & ChatGPT*

## Class
ITEC 5025

## How to Run

1. Navigate to the project directory:
   ```bash
   cd "Assignment 09"
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

- Doesn't get some more generalized requests. Need to work on that a bit more with the data
- Doesn't always get the title unless it's in Quotes. Might want to fix that for myself
- If it finds multiples of something, updates multiples
- Display better infomration when itesm are found
- Over trained model a bit I think.
- Add confidence check. Below 80% ask the user again.