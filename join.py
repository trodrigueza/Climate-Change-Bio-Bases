import nbformat

# Load the notebooks
with open("notebook.ipynb") as f1, open("contaminantes.ipynb") as f2:
    nb1 = nbformat.read(f1, as_version=4)
    nb2 = nbformat.read(f2, as_version=4)

# Merge cells
nb1.cells.extend(nb2.cells)

# Save merged notebook
with open("main.ipynb", "w") as f_out:
    nbformat.write(nb1, f_out)
