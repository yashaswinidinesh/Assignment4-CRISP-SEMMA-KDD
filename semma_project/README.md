# SEMMA Project

- Open `notebooks/SEMMA_Student_Performance.ipynb` in Colab or Cursor.
- Use `prompts/critic_prompt.md` with Claude/GPT for iterative critique.
- Train, evaluate, then export a model to `models/model.joblib`.
- Start the demo API locally:
```bash
pip install -r requirements.txt
uvicorn src.app:app --reload --port 8000
```
