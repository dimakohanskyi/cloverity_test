import matplotlib.pyplot as plt


def display_bar_chart(avg_data):
    plt.figure(figsize=(10, 6))
    avg_data.plot(kind='bar', color='steelblue', edgecolor='black')
    plt.title('Середнє значення по областях', fontsize=14, fontweight='bold')
    plt.xlabel('Область', fontsize=12)
    plt.ylabel('Середнє значення', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.show()

