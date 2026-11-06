# Character Network Analysis: Alice in Wonderland

An NLP-based data pipeline that analyzes the text of *Alice's Adventures in Wonderland* to perform Named Entity Recognition (NER), Sentiment Analysis, Co-occurrence Analysis, and visualize character interaction networks.

---

## 📌 Project Overview

This project automatically extracts characters and analyzes their relationships from textual data. By integrating coreference resolution (preprocessed), sentence tokenization, name entity recognition, and sentiment analysis, the project constructs a weighted network graph representing how characters interact and their overall emotional polarity towards each other.

---

## 🛠️ Pipeline Architecture

The workflow is divided into three key stages:

1. **Named Entity Recognition (NER) & Character Extraction**
   - Tokenizes raw text into sentences (`SentTokenizer.py`).
   - Identifies candidate character names using NER (`NameEntityRecognition.py`).
   - Filters candidates based on frequency thresholds to isolate main characters.

2. **Co-occurrence & Sentiment Analysis**
   - Processes coreference-resolved text (`AliceInWonderland-coref`) for accurate entity tracking across sentences.
   - Calculates co-occurrence frequency between characters within sentence boundaries.
   - Computes sentiment orientation and edge weights for character relationships (`Coocurence_Sentiment.py`).

3. **Network Graph Visualization**
   - Renders interactive/static character relationship networks using PyVis/NetworkX (`NetworkDisplay.py`).

---

## 📂 Project Structure

```text
CharacterNetwork/
├── Coref/                      # Coreference resolution models/data
├── CorefText/                  # Coreference-resolved text output
├── Output/                     # Generated network graphs & output figures
├── TextData/                   # Raw input texts (e.g., AliceInWonderland.txt)
├── FileManagement.py           # Text reading/writing utilities
├── SentTokenizer.py            # Sentence tokenization pipeline
├── NameEntityRecognition.py    # NER & frequency filtering
├── Coocurence_Sentiment.py     # Co-occurrence matrix & sentiment analysis
├── NetworkDisplay.py           # Network graph rendering
├── main.py                     # Main execution pipeline
└── requirments.txt             # Project dependencies
```

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.8+ installed.

### 2. Installation

Clone this repository and set up a virtual environment:

```bash
git clone https://github.com/Bencolie/CharacterNetwork.git
cd CharacterNetwork

# Create and activate a virtual environment
python -m venv venv1
source venv1/bin/activate  # On Windows: venv1\Scripts\activate

# Install required dependencies
pip install -r requirments.txt
```

### 3. Execution

Run the full pipeline using `main.py`:

```bash
python main.py
```

---

## 📊 Output Example

The script processes the text and generates network graphs stored in the `Output/` folder, displaying:
- **Nodes**: Main characters identified in the story.
- **Edges**: Connections indicating co-occurrence frequency and sentiment polarity between pairs of characters.