from transformers import pipeline

# Load pipeline once before actual initialization
# to avoid downloading during runtime
try:
    pipe = pipeline("text-classification", model="yiyanghkust/finbert-tone")
    print(f"Initial pipeline setup successful: {pipe}")
except Exception as e:
    raise RuntimeError(f"Failed to setup pipeline: {e}") from e
