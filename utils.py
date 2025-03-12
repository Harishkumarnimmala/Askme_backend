import torch
import re

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


def filter_response(output_response):
    query_match = re.search(r'QUERY:(.*?)\n', output_response)
    answer_match = re.search(r'ANSWER:(.*)', output_response, re.DOTALL)
    if query_match and answer_match:
        query = query_match.group(1).strip()
        answer = answer_match.group(1).strip()
        return query, answer
    return None, None



PROMPT = """
    You are a knowledgeable AI assistant focused on providing accurate information. 

    QUERY: {query}
    Instructions:
    1. Provide Accurate Answer based on Query
    2. If you don't know the answer then respond with "I cannot answer this question."
    ANSWER:
    """