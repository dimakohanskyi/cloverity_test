from utils.csv_reader import load_csv_data
from utils.calculations import calculate_average_by_region
from utils.create_chart import display_bar_chart


def main():
    df = load_csv_data('input_data.csv')
    averages = calculate_average_by_region(df)
    display_bar_chart(averages)


if __name__ == '__main__':
    main()

    