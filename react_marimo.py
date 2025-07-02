import marimo

__generated_with = "0.13.15"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Outlier Detection using Linear Regression
    ---
    """
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""##### To develop a robust model capable of accurately predicting **galaxy mass** based on observable properties such as brightness captured from different bands and redshift. The project aims to enhance model performance by effectively identifying and handling outliers in the dataset.""")
    return


@app.cell
def _(mo):
    mo.md("""
    ### **Understanding the Statistical Concepts for Outlier detection**
    ---
    ##### Features in predicting the target variable contains outliers which might overfit the trained model. In order to detect outliers, we'll understand the concept of ***Probability distribution Function*** which is a mathematical function which describes the likelihood of different outcomes in a random experiment. It consists of two types:

    **PROBABILITY MASS FUNCTION (PMF)** : Probability function which assigns probabilities to discrete random variables. It forms a distribution of prb. of each discrete random variable.

    **PROBABILITY DENSITY FUNCTION (PDF)** : Probability function represents probability density at a given point and it is used for continuous random variables. Here the prb. of a given point remains zero.
    """)

    mo.image(src="images\pdf_pmf.png")

    mo.md("""
    **CUMULATIVE DISTRIBUTION FUNCTION (CDF)** : Function which represents the prb. of a random variable less than or equal to a specific value. A 50% prb. in terms of CDF indicates that we've `accumulated` half of the probability density distribution. 

    **NOTE**🚨: The Inverse of CDF is known as **Percent Point Function (PPF)**.

    ### **Relation between Probability Density Function (PDF) & Cumulative Distribution Function (CDF)**
    ---
    """)

    mo.image(src="images\pdf_cdf.png")

    mo.callout(value="""
    The derivative of CDF gives us the value of PDF respectively. 

    Similarly, a specific interval in Prb. density distribution on integration tells us the CDF value.
    """, kind="info").center()

    mo.md("**Here is the relationship between the Prb. Distribution Functions:**")

    mo.image(src="images\\relation.png")

    mo.callout(value=mo.md("""
    ### **Some Basic Terminlogies of Normalization and Standardization**
    **NORMAL DISTRIBUTION** : Probability distribution with a bell curve.

    **STANDARD NORMAL DISTRIBUTION** : Normal distribution with mean 0 and std.dev. 1.

    **Z-SCORE** : A `standard` measure which tell how many std.dev. a data point is away from the mean(0).<br>
    """))

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
