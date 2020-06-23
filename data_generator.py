@@ -0,0 +1,20 @@
# Step 1) Use testdat library to create a model
# Step 2) Create list of first and last names to choose from and generate piple delimited file

import tesdat

colors_light = ['pink','skyblue']
colors_dark = ['brown','purple']

model = tesdat.getmodel([
tesdat.CyclePattern(colors_light,repeat=2),
tesdat.CyclePattern(colors_dark,repeat=3),
tesdat.IncrementPattern(start=99500, step=1),
]).ordering(1)  

container = tesdat.IterContainer(model, 1000) # 1000 rows

tesdat.CsvFormatter(
container,
delimiter='|', # pipe delimiter
).write('data_generator_output.csv', rewrite=True) 