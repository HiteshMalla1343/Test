# A Little Question of Love 💗 — Streamlit app

A self-contained romantic quiz with a score-based heart, a perfect-score celebration, floating hearts, and a size-scaling journey from rice to the universe.

## Run locally

1. Install Python 3.10 or newer.
2. Unzip this folder and open a terminal in it.
3. Create and activate a virtual environment (optional but recommended):

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies and start Streamlit:

   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

5. Your browser should open to the local app, usually `http://localhost:8501`.

## Publish it on Streamlit Community Cloud (free tier availability may change)

1. Create a GitHub account if you don't already have one.
2. Create a **public** GitHub repository, for example `little-love-quiz`.
3. Upload `app.py` and `requirements.txt` to the repository root. (You can also upload this README.)
4. Go to **https://share.streamlit.io/** and sign in with GitHub.
5. Choose **Create app**, select the repository, branch, and `app.py`, then deploy.
6. Streamlit will provide a public URL. Open that URL on your phone to test it, then share it privately with your girlfriend.

Official docs: https://docs.streamlit.io/deploy/streamlit-community-cloud

## Personalise it before sharing

Open `app.py` and edit:
- The `questions` array in the HTML/JavaScript to change questions and answers.
- Each question's `correct` number (0-based: `0` is option A, `1` is B, `2` is C, `3` is D).
- The final message in the `#final` section.
- The title and intro copy in the `#welcome` section.

Important: the sample quiz uses playful, generic questions and makes option D the correct answer for all ten questions. Personalise the wording and answer keys so the quiz feels like *your* relationship rather than a generic template.

## Notes

- The quiz and animation logic run in the browser inside Streamlit's HTML component; no database or API key is needed.
- Google Fonts are imported for typography. If a network blocks Google Fonts, the app falls back to system fonts.
- This is a fun surprise, not a secure assessment: answers are client-side and aren't stored or sent to you.
- If you want the site to feel more personal, replace the generic questions and final paragraph before deploying.
