from pydantic import BaseModel

schema = {
    "properties": {
      'name': 'Candidate Name',
      'party': 'Political Party',
      'running_mate': 'Running Mate Name',
      'campaign_website': 'Campaign Website URL',
      'image_url': 'Image URL',
      'brief_summary': 'Brief Summary or Description',
      'source_url': 'Source URL'
    
    },
    "required": ["item_name", "price", "item_extra_info"],
}


class SchemaNewsWebsites(BaseModel):
    news_headline: str
    news_short_summary: str
