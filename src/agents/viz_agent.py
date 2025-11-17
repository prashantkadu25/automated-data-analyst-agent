# src/agents/viz_agent.py
import os
import matplotlib.pyplot as plt
import seaborn as sns
from loguru import logger

def plot_histograms(df, outdir):
    os.makedirs(outdir, exist_ok=True)
    plots = []
    num = df.select_dtypes(include=['number'])
    for col in num.columns:
        fig = plt.figure()
        sns.histplot(df[col].dropna(), kde=False)
        fname = os.path.join(outdir, f"{col}_hist.png")
        fig.savefig(fname, bbox_inches='tight')
        plt.close(fig)
        plots.append(fname)
    logger.info(f"Saved {len(plots)} histograms")
    return plots

def plot_correlation_heatmap(df, outpath):
    num = df.select_dtypes(include=['number'])
    if num.shape[1] < 2:
        return None
    fig = plt.figure(figsize=(8,6))
    sns.heatmap(num.corr(), annot=True, fmt=".2f")
    fig.savefig(outpath, bbox_inches='tight')
    plt.close(fig)
    logger.info(f"Saved correlation heatmap {outpath}")
    return outpath
