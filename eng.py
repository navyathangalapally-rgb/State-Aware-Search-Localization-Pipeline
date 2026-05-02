from bs4 import BeautifulSoup
import time

def translate_html(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Step 1: Repair Image Paths
    for img in soup.find_all('img'):
        if 'src' in img.attrs:
            # Flatten path to local images directory
            filename = img['src'].split('/')[-1]
            img['src'] = f"images/{filename}"

    # Step 2: Extract and Localize Text Nodes
    # Note: In production, this integrates with a Translation API
    for text_node in soup.find_all(text=True):
        if text_node.parent.name in ['p', 'td', 'li', 'h1', 'h2']:
            clean_text = text_node.strip()
            if clean_text:
                # Batch processing simulation
                print(f"Translating: {clean_text[:20]}...")
                time.sleep(0.1)

    # Step 3: Save Optimized Output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

if __name__ == "__main__":
    translate_html('manual_en.html', 'manual_de.html')
