import splitfolders

input_folder = "dataset/"

splitfolders.ratio(input_folder, output="output_folders", 
                   seed=42, ratio=(.7,.2,.1), group_prefix=None)
