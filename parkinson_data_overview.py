import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt
    return mo, pd


@app.cell
def _(pd):
    df = pd.read_csv("parkinsons_updrs.csv")
    df.head()
    return (df,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Feature Understanding
    ---

    - `subject#`: **The nth person who is having the biomedical test having *Parkinson's disease*.**
    - `test_time`: **The time duration (in days) since the subject was enrolled.**
    -
    """
    )
    return


@app.cell
def _(df, mo):
    table = mo.ui.table(df.corr().round(decimals=2), show_column_summaries=False)
    table
    return


@app.cell
def _(df, pd):
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    from statsmodels.tools.tools import add_constant

    x_df = df.drop(["subject#","motor_UPDRS","total_UPDRS"],axis=1)
    X = add_constant(x_df)

    vif_data = {
        "features":X.columns.tolist(),
        "vif score":[variance_inflation_factor(X.values,i) for i in range(len(X.columns.tolist()))]
    }

    vif_df = pd.DataFrame(vif_data)
    return (vif_df,)


@app.cell
def _(vif_df):
    vif_df.sort_values(by=["vif score"], ascending=False)
    return


@app.cell
def _(vif_df):
    vif_df
    return


if __name__ == "__main__":
    app.run()
