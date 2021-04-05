import datetime
import os
import matplotlib.pyplot as plt

from .json_utils import load_json_file


# Generating bins from longest timestamp
def range_steps(step, max_value):
    num_steps = max_value // step
    new_range = [step * i for i in range(0, int(num_steps))]
    if max_value < num_steps * step:
        new_range.append(max_value)
    return new_range


# Timestamp stuff
def seconds_to_hms(seconds):
    return str(datetime.timedelta(seconds=seconds))


def fetch_timestamps_from_file(filename, file_dir="./"):
    file = os.path.join(file_dir, filename)

    comments = load_json_file(file)
    return [comment["content_offset_seconds"] for comment in comments]


def plot_timestamp(timestamp, **hist_kwargs):
    plt.hist(timestamp, **hist_kwargs)


def plot_timestamp_from_file(
    filename, figure_filename, file_dir="./", step_size=5 * 60
):
    timestamps = fetch_timestamps_from_file(filename, file_dir)
    if not timestamps:
        print("Timestamps not found")
        return

    bins = range_steps(step_size, timestamps[-1])

    plot_timestamp(timestamps, bins=bins)
    plt.savefig(figure_filename)


def plot_two_timestamps(timestamps1, timestamps2, **hist_kwargs):
    plot_timestamp(timestamps1, facecolor="green", alpha=0.5, **hist_kwargs)
    plot_timestamp(timestamps2, facecolor="blue", alpha=0.5, **hist_kwargs)


def plot_timestamp_comparisons_from_files(
    filename1,
    filename2,
    figure_filename,
    step_size=5 * 60,
    file_dir="./",
    **hist_kwargs,
):
    timestamps1 = fetch_timestamps_from_file(filename1, file_dir)
    timestamps2 = fetch_timestamps_from_file(filename2, file_dir)

    max_length = max(len(timestamps1), len(timestamps2))
    if max_length == 0:
        print("No timestamps found")
        return

    bins = range_steps(step_size, timestamps2[-1])

    plot_timestamp_comparisons(
        timestamps1,
        timestamps2,
        figure_filename,
        bins=bins,
        **hist_kwargs,
    )


def plot_timestamp_comparisons(
    timestamps1, timestamps2, figure_filename, **hist_kwargs
):
    plot_timestamp(timestamps1, facecolor="green", alpha=0.5, **hist_kwargs)
    plot_timestamp(timestamps2, facecolor="blue", alpha=0.5, **hist_kwargs)

    plt.savefig(figure_filename)


def save_plots_from_comments_for_search_string_from_dir(
    video_id,
    search_string,
    figure_filename=None,
    overwrite=False,
    step_size=5 * 60,
    file_dir="./",
):
    search_string_filename = f"{search_string}_comments.json"

    search_string_file = os.path.join(file_dir, search_string_filename)
    if not os.path.isfile(search_string_file):
        print(f"{search_string_file} does not exit")
        return

    if figure_filename is None:
        figure_filename = f"{video_id}_{search_string}_{step_size//60}m.png"

    if os.path.isfile(figure_filename) and not overwrite:
        print(f"{figure_filename} exists")
        return

    plot_timestamp_from_file(
        search_string_filename,
        figure_filename,
        file_dir=file_dir,
        step_size=step_size,
    )

    plt.close("all")


def save_plots_from_comment_comparisons_for_search_string_from_dir(
    video_id,
    search_string,
    figure_filename=None,
    overwrite=False,
    step_size=5 * 60,
    file_dir="./",
):
    search_string_filename = f"{search_string}_comments.json"
    comments_filename = "comments.json"

    search_string_file = os.path.join(file_dir, search_string_filename)
    if not os.path.isfile(search_string_file):
        print(f"{search_string_file} does not exit")
        return

    if figure_filename is None:
        figure_filename = f"{video_id}_{search_string}_{step_size//60}m.png"

    if os.path.isfile(figure_filename) and not overwrite:
        print(f"{figure_filename} exists")
        return

    plot_timestamp_comparisons_from_files(
        search_string_filename,
        comments_filename,
        figure_filename,
        file_dir=file_dir,
        step_size=step_size,
    )

    plt.close("all")


def format_timestamps(timestamps):
    return [seconds_to_hms(timestamp) for timestamp in timestamps]
