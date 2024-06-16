# Scrape the Web with entities extraction using OpenAI Function

## What is this?

Using LangChain and Open AI
Create a schema in `schemas.py`, pick a url, and use them with `scrape_with_playwright()` in `main.py` to start scraping.

Tip: each website has the bulk of content either in `<p>`, `<span>` or `<h>` tags. For best performance, choose a combination of tags that work for you.

It returns html raw format and cleans it up

### Example

1. Define the schema of the website you want to scrape in `schemas.py` (Pydantic class or dictionary are both fine):

   ```python
   class SchemaNewsWebsites(BaseModel):
       news_headline: str
       news_short_summary: str
   ```

2. To start scraping, in `main.py`, run something like this:

   ```python
   asyncio.run(scrape_with_playwright(
           url="https://www.bbc.com](https://ballotpedia.org/Presidential_candidates,_2024",
           tags=["span"],
           schema_pydantic=SchemaNewsWebsites
       ))
   ```

## Setup

### 1. Create a new Python virtual environment

`python -m venv virtual-env` or `python3 -m venv virtual-env` (Mac)

`py -m venv virtual-env` (Windows 11)

### 2. Activate virtual environment

`.\virtual-env\Scripts\activate` (Windows)

`source virtual-env/bin/activate` (Mac)

### 3. Install dependencies using Poetry

Run `poetry install --sync` or `poetry install`

### 4. Install playwright

```bash
playwright install
```

### 5. Create a new `.env` file to store OpenAI's API key

```text
OPENAI_API_KEY=XXXXXX
```

## Usage

### Run locally

```bash
python main.py
```

