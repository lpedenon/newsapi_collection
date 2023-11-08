import argparse
from pathlib import Path
from newsapi import fetch_latest_news
import json

''' Write a CLI tool sitting in the newscover.collector that has the following behavior
	Python -m newscover.collector -k <api_key> [-b <# days to lookback>] -i <input_file> -o <output_dir>
The input file is a json file containing a dictionary of named keyword lists. Like this
{ “trump_fiasco”: [“trump”, “trial”], “swift”: [“taylor”, “swift”, “movie”] ]
For each keyword set with name N and keyword list X, the collector will execute a query for the keywords X and write the results to the <output_dir>/N.json.
'''

def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-k', '--api_key', type=str, help='NewsAPI API key')
    parser.add_argument('-b', '--lookback_days', type=int, default=10, help='Number of days to lookback')
    parser.add_argument('-i', '--input_file', type=str, help='Input file')
    parser.add_argument('-o', '--output_dir', type=str, help='Output directory')

    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        keywords_dict = json.load(f)
    
    for k,v in keywords_dict.items():
        for keywords in v:
            articles = fetch_latest_news(args.api_key, " ".join(keywords), args.lookback_days)
            fpath = Path(args.output_dir) / k + ".json"
            with open(fpath, "a") as f:
                json.dump(articles, f, indent=4)

if __name__ == "__main__":
    main() 

    