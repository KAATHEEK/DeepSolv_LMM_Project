from data_processing.extract_data import extract_text_from_pdf, scrape_website, get_youtube_transcript
from data_processing.create_embeddings import create_embeddings, store_embeddings

def main():
    # Paths and URLs
    pdf_path = './Apple_Vision_Pro_Privacy_Overview.pdf'  # Use the relative path
    website_url = 'https://www.apple.com/apple-vision-pro/'  # This URL is correct
    youtube_video_id = 'TX9qSaGXFyg'  # Replace with the actual YouTube video ID

    # Extract data from all sources
    pdf_text = extract_text_from_pdf(pdf_path)
    website_text = scrape_website(website_url)
    youtube_transcript = get_youtube_transcript(youtube_video_id)

    # Combine all extracted texts
    all_text = pdf_text + website_text + youtube_transcript

    # Create embeddings
    embeddings = create_embeddings([all_text])

    # Store embeddings in FAISS
    store_embeddings(embeddings)

if __name__ == "__main__":
    main()
