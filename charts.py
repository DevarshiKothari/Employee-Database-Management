import matplotlib.pyplot as plt

def return_chart(chart_data):
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)
    axes.bar(
        [data[0] for data in chart_data],
        [data[1] for data in chart_data]
    )