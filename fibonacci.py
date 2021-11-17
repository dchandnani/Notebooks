import math
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots

# Program to display the Fibonacci sequence up to n-th term

def fibonacci():
    nterms = 20

    # first two terms
    n1, n2 = 0, 1
    count = 0
    data = [0, 1]

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            nth = n1 + n2
            data.append(nth)
            n1 = n2
            n2 = nth
            count += 1

    return data


def plotSeries(data):
    fig = make_subplots(rows=1, cols=2)
    fig = px.bar(data, color_discrete_sequence=['purple']*len(data))
    fig.update_layout(title_text="<b>Fibonacci Series</b>",
                      title_font=dict(family="Arial", size=20, color='silver'))
    fig.update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
         'paper_bgcolor': 'rgba(0, 0, 0, 0)', })

    fig.update_yaxes(
        color='rgba(100,100,100,1)',
        showgrid=True, gridcolor='rgba(100,100,100,1)',
        zerolinewidth=1, zerolinecolor='rgba(100,100,100,1)')
    fig.update_xaxes(color='rgba(100,100,100,1)')
    fig.update_layout(showlegend=False)
    fig.show()


data = fibonacci()
print(data)
#plotSeries(data)
