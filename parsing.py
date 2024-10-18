from langchain_ollama import OllamaLLM
from concurrent.futures import ThreadPoolExecutor

def parse_with_ollamm(dom_content: str, parse_description: str) -> str:

    def process_chunk(chunk):
        llm = OllamaLLM(model='llama3.2')
        response = llm.invoke(f"""
        "You are tasked with extracting specific information from the following text content: {chunk}. "
        "Please follow these instructions carefully: \n\n"
        "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
        "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
        "3. **Empty Response:** If no information matches the description, return an empty string ('')."
        "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
        "5. Response Format: ** Your response should be in html"    
        """)
        return response
    
    chunk_size = 6000
    chunks = [dom_content[i:i + chunk_size] for i in range(0, len(dom_content), chunk_size)]
    
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_chunk, chunks))
    
    combined_response = ''.join(results)
    return combined_response
