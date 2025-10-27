
## Installation
1. Clone the repository:

```bash
git clone https://github.com/dimakohanskyi/cloverity_test
cd cloverity_test
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies using Poetry:
```bash
poetry install --no-root
```

## Running the Application

1. Make sure you're in the project root directory
2. Run the main script:
```bash
poetry run python src/main.py
```

The application will:
1. Read data from `input_data.csv`
2. Calculate averages by region
3. Display a bar chart visualization of the results

## Project Structure

```
├── input_data.csv        # Source data file
├── pyproject.toml        # Project dependencies and metadata
├── README.md
└── src/
    ├── main.py          # Main application entry point
    └── utils/
        ├── calculations.py    # Data processing functions
        ├── create_chart.py    # Visualization functions
        └── csv_reader.py      # Data loading functions
```

## Dependencies

- pandas >= 2.3.3
- matplotlib >= 3.10.7