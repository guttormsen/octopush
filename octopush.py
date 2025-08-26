import tkinter as tk

# Features to display on the landing view
FEATURES = [
    "Kunnskapsbase",
    "Lover",
    "Notater",
    "Kalkulatorer",
    "Logikkimport",
    "Q&A",
    "Globalt Søk",
]


def open_feature(name: str) -> None:
    """Open a simple pane representing the selected feature."""
    pane = tk.Toplevel(root)
    pane.title(name)
    tk.Label(pane, text=f"{name} pane", padx=20, pady=20).pack()


# Create the main landing window
root = tk.Tk()
root.title("Octopush")

# Create large buttons (cards) for each feature
for index, name in enumerate(FEATURES):
    button = tk.Button(
        root,
        text=name,
        width=20,
        height=5,
        font=("Helvetica", 16),
        command=lambda n=name: open_feature(n),
    )
    row, col = divmod(index, 3)
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

# Make the grid cells expand equally
for i in range(3):
    root.grid_columnconfigure(i, weight=1)
for i in range((len(FEATURES) + 2) // 3):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
