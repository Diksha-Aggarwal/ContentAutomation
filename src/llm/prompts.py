GENERATOR_PROMPT = """
You are an AI research assistant.

Task:
Summarize the top global technology and AI trends based on provided sources.

Constraints:
- Be concise
- Be factual
- No hallucinations

Sources:
{sources}

Summary:
"""

VALIDATOR_PROMPT = """
You are a validation agent.

Task:
Evaluate the following summary for factual correctness and coherence.

Summary:
{summary}

Return:
- A confidence score between 0 and 1
- A short justification
"""
