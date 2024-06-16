import asyncio
import pprint

from ai_extractor import extract
from schemas import SchemaNewsWebsites, schema
from scrape import ascrape_playwright

## Will have to change the tags we are searching for based on the site

# TESTING
if __name__ == "__main__":
    token_limit = 4000

    # News sites mostly have <span> tags to scrape
    ballot_url = "https://ballotpedia.org/Presidential_candidates,_2024"

    async def scrape_with_playwright(url: str, tags, **kwargs):
        html_content = await ascrape_playwright(url, tags)

        print("Extracting content with LLM")

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content = extract(**kwargs,
                                    content=html_content_fits_context_window_llm)

        pprint.pprint(extracted_content)

    # Scrape and Extract with LLM
    asyncio.run(scrape_with_playwright(
        url=ballot_url,
        tags=["span"],
        schema_pydantic=SchemaNewsWebsites
    ))
