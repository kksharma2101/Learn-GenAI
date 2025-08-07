from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/furniture/beds-more/pr?sid=wwe%2C7p7&marketplace=FLIPKART&p%5B%5D=facets.price_range.from%3DMin&otracker=clp_creative_card_2_1.creativeCard.CREATIVE_CARD_ikfs-2-store_9SQKF1GYVL1K&fm=neo%2Fmerchandising&iid=M_60b038a0-5ff1-4d0c-9027-b031939830e2_1.9SQKF1GYVL1K&ppt=None&ppn=None&ssid=c93yawdx4w0000001754047420962&p%5B%5D=facets.price_range.to%3D10000'
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)