"""
Author: Joshua Ashkinaze

Description: Pulls in the battle data, and writes out the model names to a csv file for annotation

Date: 2024-03-19 19:45:00
"""




import pandas as pd
import gdown
import os
import logging, datetime, os



def main():
    logging.basicConfig(
        filename=f"{os.path.splitext(os.path.basename(__file__))[0]}.log",
        level=logging.INFO,
        format='%(asctime)s: %(message)s',
        datefmt='%Y-%m-%d__%H--%M--%S'
    )

    filename = "clean_battle_20240313.json"
    if not os.path.exists(filename):
        logging.info("Downloading")
        url = "https://drive.google.com/file/d/1Kpg6HD1QCrytCVT7FgRvZhY885TnmpEo/view?usp=sharing"
        filename = gdown.download(url, fuzzy=True)
    else:
        logging.info("reading in")

    df = pd.read_json(filename)
    model_a_names = list(df['model_a'].unique())
    model_b_names = list(df['model_b'].unique())
    all_models = list(set(model_a_names + model_b_names))
    model_df = pd.DataFrame(all_models)
    model_df.columns = ['long_name']
    model_df.to_csv("model_names.csv")  # download model names to annotate later
    logging.info("Done, wrote stuff")

if __name__ == "__main__":
    main()
