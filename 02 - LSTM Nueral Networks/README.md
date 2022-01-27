# Stock Market Predictions with a Long Short-Term Memory Neural Network

A starter repository for AI Club at NC State's second workshop of the Fall 2021 semester which covers Long Short-Term Memory Neural Networks.

Adapted from: https://www.datacamp.com/community/tutorials/lstm-python-stock-market

### Data:
- [Alpha Vantage Stock API](https://www.alphavantage.co/)
- [Kaggle - "Huge Stock Market Dataset"](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)


### Prerequisites:
- [Anaconda Individual Edition](https://www.anaconda.com/products/individual)
- Git/GitHub Desktop
- IDE/Text Editor ???

### Workshop Steps:
1. Install prerequisites (see above)
2. Create a new, personal copy of this repo template
3. Clone your personal copy of the repo
4. (Optional) Register for a free Alpha Vantage Stock API key [here](https://www.alphavantage.co/support/#api-key)
   1. Note: After clicking "GET FREE API KEY," your API key will appear on the webpage, below the button.
   2. In the second code block of the `intro.ipynb` notebook, replace `'<API_KEY>'` with your actual API key.
5. Download the Kaggle stock data [here](https://drive.google.com/file/d/1h9slXKahVEy4bpmudAxvPrz4TG_qdXok/view?usp=sharing)
6. Extract the `.zip` archive and move the `Stocks` folder to the `data/external/` directory
7. Create and activate a new virtual environment for the project
8. Install required packages
   ```
   pip install -r requirements.txt
   ```
9. In your terminal/command prompt that is using your virtual environment, run the following to start Jupyter:
   ```
   jupyter notebook
   ```
10. Follow along in the Jupyter notebooks. Start with `intro.ipynb`, then move to `lstm.ipynb`.
