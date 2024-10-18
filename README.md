# ABOUT

A webscraper that uses selenium to scrape websites and removes the irrelevant script HTML content and get's you the beautiful data that you need.
You have the option to either scrape multiple page at once or scroll down (if there is scrollable content).
Cleaned data is passed to **llama** with the extraction description that you provide to it.
Response is HTML so it can get data in tables or whatever HTML format you want (specify in extraction description)

## REQUIREMENTS
* Download ollama https://github.com/ollama/ollama
```bash
pip install -r requirements.txt
```
## Download llama3.2
```bash
ollama pull llama3.2
```
## Run Scraper
```bash
streamlit run AI Scraper.py
```
## Have Fun
![Sample Image](image/sample.jpeg)
