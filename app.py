import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render


# Add page options for the overall app.
ui.page_opts(title="PyShiny App with Plot", fillable=True)


with ui.sidebar():
    # A string id ("selected_number_of_bins") that uniquely identifies this input value.
    # A string label (e.g., "Number of Bins") to be displayed alongside the slider.
    # An integer representing the minimum number of bins (e.g., 0).
    # An integer representing the maximum number of bins (e.g., 100).
    # An integer representing the initial value of the slider (e.g., 20).
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram")
def draw_histogram():
    # pass the numpy data array
    np.random.seed(3)

    random_data_array = 100 + 15 * np.random.randn(437)

    # Pass in the user input the number of bins.
    # Set the density to True.
    plt.hist(
        random_data_array,
        input.selected_number_of_bins(),
        density=True,
        color="orange",
        edgecolor="black",
    )
