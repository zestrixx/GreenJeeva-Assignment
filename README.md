Web Scraping and AI-Enhanced Data Enrichment

Setup Instructions:-
1. Clone this repository to your local machine.
  https://github.com/zestrixx/GreenJeeva-Assignment.git

2. Ensure you have Python installed. You can download it from https://www.python.org.

3. Install the required Python libraries using pip:
    - pip install -r requirements.txt

4. Run the Python script main.py to perform web scraping and AI-enhanced data enrichment.

Dependencies:-
  - beautifulsoup4==4.12.3
  - lxml==5.2.1
  - numpy==1.26.4
  - pandas==2.2.2
  - sumy==0.11.0
  - requests==2.31.0
  - More can be found in the requirements.txt file
  
    - BeautifulSoup: Used for web scraping HTML and XML files.
    - Requests: Used to make HTTP requests to fetch web pages.
    - TextBlob: Used for sentiment analysis of product descriptions.
    - Sumy: Used for summarization of product descriptions.

Approach:-
  - Web Scraping
    - The script uses BeautifulSoup to scrape product information from a specific webpage.
    - It targets specific <div> elements with unique IDs to extract product details such as name and description.
    - Each product description is then further enriched using AI techniques.
  - AI-Enhanced Data Enrichment
    i) Sentiment Analysis:
      - TextBlob library is used to perform sentiment analysis on the product descriptions.
      - Sentiment analysis provides polarity and subjectivity scores for each description.
    ii) Summarization of Description:
      - Sumy's nltk library generates a summary from the product descriptions.
      - Keywords represent important terms or phrases that capture the essence of the description.
      - The enriched data, including product names, descriptions, sentiment analysis results, and extracted keywords, are stored in a structured format (JSON/CSV/SQL database) as per the requirements.
