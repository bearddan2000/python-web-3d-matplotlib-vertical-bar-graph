from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def create_graph():
    filename = 'demo'

    # random but consistant data
    lst = [2,9,4,6,4]

    xs = np.arange(len(lst))
    ys = np.array(lst)

    # clear buffer
    plt.clf()
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.bar(xs, ys, zs=xs, zdir='y')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.savefig(f'static/img/{filename}.png')

@app.route('/', methods=['GET'])
def getIndex():
    create_graph()
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)