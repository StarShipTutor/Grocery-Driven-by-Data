"""
Visualization utilities for consistent chart styling.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Optional, Tuple

# Project color palette
COLORS = {
    "primary": "#2E86AB",      # Steel blue
    "secondary": "#A23B72",    # Raspberry
    "accent": "#F18F01",       # Orange
    "success": "#2ECC71",      # Green
    "warning": "#F39C12",      # Yellow
    "danger": "#E74C3C",       # Red
    "neutral": "#7F8C8D",      # Gray
}

PALETTE = [COLORS["primary"], COLORS["secondary"], COLORS["accent"], 
           COLORS["success"], COLORS["warning"], COLORS["danger"]]


def set_style(style: str = "whitegrid", context: str = "notebook") -> None:
    """
    Set the global matplotlib/seaborn style.
    
    Args:
        style: Seaborn style name
        context: Seaborn context (paper, notebook, talk, poster)
    """
    sns.set_style(style)
    sns.set_context(context)
    sns.set_palette(PALETTE)
    
    plt.rcParams.update({
        "figure.figsize": (12, 6),
        "figure.dpi": 100,
        "savefig.dpi": 150,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.titlesize": 16,
    })


def save_figure(
    filename: str,
    output_dir: Optional[str] = None,
    formats: Tuple[str, ...] = ("png",),
    tight: bool = True,
    transparent: bool = False,
) -> list:
    """
    Save the current figure to file(s).
    
    Args:
        filename: Base filename (without extension)
        output_dir: Output directory (default: outputs/figures)
        formats: Tuple of formats to save (png, svg, pdf)
        tight: Use tight bounding box
        transparent: Transparent background
        
    Returns:
        List of saved file paths
    """
    if output_dir is None:
        output_dir = Path(__file__).parent.parent.parent / "outputs" / "figures"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    saved_paths = []
    for fmt in formats:
        filepath = output_dir / f"{filename}.{fmt}"
        plt.savefig(
            filepath,
            format=fmt,
            bbox_inches="tight" if tight else None,
            transparent=transparent,
            facecolor="white" if not transparent else "none",
        )
        saved_paths.append(str(filepath))
    
    return saved_paths


def create_figure(
    nrows: int = 1,
    ncols: int = 1,
    figsize: Optional[Tuple[float, float]] = None,
    title: Optional[str] = None,
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a figure with consistent styling.
    
    Args:
        nrows: Number of subplot rows
        ncols: Number of subplot columns
        figsize: Figure size (width, height)
        title: Overall figure title
        
    Returns:
        Tuple of (figure, axes)
    """
    if figsize is None:
        figsize = (6 * ncols, 4 * nrows)
    
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    
    if title:
        fig.suptitle(title, fontsize=16, fontweight="bold")
    
    fig.tight_layout()
    
    return fig, axes


def format_axis(
    ax: plt.Axes,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    legend: bool = True,
    grid: bool = True,
    rotate_xticks: Optional[int] = None,
) -> plt.Axes:
    """
    Apply standard formatting to an axis.
    
    Args:
        ax: Matplotlib Axes object
        title: Axis title
        xlabel: X-axis label
        ylabel: Y-axis label
        legend: Show legend
        grid: Show grid
        rotate_xticks: Rotation angle for x-tick labels
        
    Returns:
        Formatted Axes object
    """
    if title:
        ax.set_title(title, fontsize=14, fontweight="bold", pad=10)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12)
    if legend and ax.get_legend_handles_labels()[0]:
        ax.legend(frameon=True, fancybox=True, shadow=True)
    if grid:
        ax.grid(True, alpha=0.3)
    if rotate_xticks is not None:
        plt.setp(ax.get_xticklabels(), rotation=rotate_xticks, ha="right")
    
    return ax
