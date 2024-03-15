def get_number(maintextbox):
    end_index = maintextbox.index("end-1c")
    row, column = map(int, end_index.split("."))

    words = maintextbox.get("1.0", "end-1c").split()

    return row, column, len(words)


def update_rows_label(infolabel, fontSize_perc_var, maintextbox):
    row, column, words = get_number(maintextbox)
    infolabel.configure(
        text=f"Row {row}, Column {column + 1} || Words {words} || {fontSize_perc_var.get()}%")
