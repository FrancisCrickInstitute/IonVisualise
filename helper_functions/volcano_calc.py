## Import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import statsmodels.api as sm


### Define functions ###
def stat_test(data):
    """Calculate t test
    Returns:
        dataframe: rows: samples, columns: Feature","P-value, P-adjust
    """

    # Input from users
    one = input("Condition 1: ")
    two = input("Condition 2: ")

    if one != "" and two != "":
        condition_1 = data[data["metadata"] == one]
        condition_2 = data[data["metadata"] == two]

        # Remove metadata
        condition_1 = condition_1.iloc[
            :, :-5
        ]  # need to fix so can be generalized
        condition_2 = condition_2.iloc[
            :, :-5
        ]  # need to fix so can be generalized

        pvalues = stats.ttest_ind(condition_1, condition_2)[1]

        padj = sm.stats.multipletests(pvalues, 0.05, method="fdr_bh")

        results = pd.DataFrame(
            zip(data, pvalues, padj[1]),
            columns=["Feature", "P-value", "P-adjust"],
        )
        results = results.set_index("Feature")
        results["P-adjust"] = results["P-adjust"].fillna(0)

        return condition_1, condition_2, results


def calc_fold_change(condition_1, condition_2):
    """Calculate log fold change
    Returns:
        dataframe: return
    """

    fold_changes = np.mean(condition_1, axis=0) - np.mean(condition_2, axis=0)
    fold_changes = pd.DataFrame(fold_changes, columns=["Fold_Change"])
    return fold_changes


def calc_volcano_plot(fold_changes, results):
    """Make dataframe for volcano plot
    Returns:
        dataframe:
            rows: samples
            columns: columns for volcano plot
    """

    volcano_df = pd.DataFrame.merge(
        fold_changes, results, right_index=True, left_index=True
    )
    return volcano_df


def main():
    ### Run code ###

    # Import data
    data = pd.read_csv(
        "/Users/sarapatti/Desktop/run2_filling_missing_data_mean_50.csv"
    )
    data = pd.DataFrame(data)

    # Add metadata
    ### going to be a problem to generalize
    meta = data.iloc[:, -4:]
    meta[["time point (hpi)", "replicate"]] = meta[
        ["time point (hpi)", "replicate"]
    ].astype(int)
    meta["Sample"] = meta["Sample"].astype(str)
    data["metadata"] = data.apply(
        lambda row: f"{row['time point (hpi)']}_{row['virus type']}", axis=1
    )

    ############ Code itself ##########

    # Calculate statistics
    condition_1, condition_2, results = stat_test(data)

    # Calculate fold change
    fold_changes = calc_fold_change(condition_1, condition_2)

    # Create dataframe
    volcano_df = calc_volcano_plot(results, fold_changes)
    # print(volcano_df)

    return volcano_df
