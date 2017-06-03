"""
This file has functions that provide basic plotting functionality
"""

from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl

# ------------------------------------------------------------------------------
# Define MATLAB R2014 colors
# ------------------------------------------------------------------------------
# https://de.mathworks.com/help/matlab/graphics_transition/why-are-plot-lines-different-colors.html
matlab_blue = [0.0, 0.447, 0.741]
matlab_orange = [0.85, 0.325, 0.098]
matlab_yellow = [0.929, 0.694, 0.125]
matlab_purple = [0.494, 0.184, 0.556]
matlab_green = [0.466, 0.674, 0.188]
matlab_cyan = [0.301, 0.745, 0.933]
matlab_red = [0.635, 0.078, 0.184]


# ------------------------------------------------------------------------------
# Config matplotlib for latex
# ------------------------------------------------------------------------------
def thesis_a4_format():
    """
    Function that can be called if the plot is meant to be used in the thesis.

    Font size will be 12pt
    Font will be Times New Roman
    Width of the plot will be 15cm = 5.91in

    To save a figure as pdf call 'fig.savefig("yolo.pdf")' at end of script

    :return: Nothing
    """

    # Use LaTeX to set the characters
    mpl.rcParams['text.usetex'] = True

    # Figure
    mpl.rcParams['figure.figsize'] = 5.91, 3.94

    # Ticks
    mpl.rcParams['xtick.labelsize'] = 12
    mpl.rcParams['ytick.labelsize'] = 12

    # Axes
    mpl.rcParams['axes.labelsize'] = 12
    mpl.rcParams['axes.titlesize'] = 12
    mpl.rcParams['axes.linewidth'] = 0.6

    # Legend
    mpl.rcParams['legend.markerscale'] = 1
    mpl.rcParams['legend.fontsize'] = 12
    mpl.rcParams['legend.labelspacing'] = '0.3'
    mpl.rcParams['legend.edgecolor'] = '1'
    mpl.rcParams['legend.framealpha'] = '.8'

    # Lines
    mpl.rcParams['lines.linewidth'] = 1.5
    # mpl.rcParams['lines.markersize'] = 4
    mpl.rcParams['lines.color'] = 'r'

    # Font
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = ['Times New Roman']
    mpl.rcParams['font.weight'] = 'regular'
    mpl.rcParams['font.size'] = 12

    # Automatically set the height of the figure
    mpl.rcParams['figure.autolayout'] = True


def paper_us_ieee_format():
    """
    Function that can be called if the plot is meant to be used in a us letter
    IEEE paper.

    Font size will be 8pt
    Font will be Times
    Width of the plot will be 8.62cm

    To save a figure as pdf call 'fig.savefig("yolo.pdf")' at end of script

    :return: Nothing
    """

    # Use LaTeX to set the characters
    mpl.rcParams['text.usetex'] = True

    # Figure
    mpl.rcParams['figure.figsize'] = 3.39, 3.39/15*10

    # Ticks
    mpl.rcParams['xtick.labelsize'] = 8
    mpl.rcParams['ytick.labelsize'] = 8

    # Axes
    mpl.rcParams['axes.labelsize'] = 8
    mpl.rcParams['axes.titlesize'] = 8
    mpl.rcParams['axes.linewidth'] = 0.6

    # Legend
    mpl.rcParams['legend.markerscale'] = 1
    mpl.rcParams['legend.fontsize'] = '8'
    mpl.rcParams['legend.labelspacing'] = '0.3'
    mpl.rcParams['legend.edgecolor'] = '1'
    mpl.rcParams['legend.framealpha'] = '.8'

    # Lines
    mpl.rcParams['lines.linewidth'] = 1.5
    mpl.rcParams['lines.markersize'] = 4
    mpl.rcParams['lines.color'] = 'r'

    # Font
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = ['Times']
    mpl.rcParams['font.weight'] = 'regular'
    mpl.rcParams['font.size'] = 8

    # Automatically set the height of the figure
    mpl.rcParams['figure.autolayout'] = True
