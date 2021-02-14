# Introduction
This is a test for seeing how well you can get around doing some basic statistical analyses on a dataset similar to the those that you would see while working at Carta.

In this analysis, you are assuming the role of a data scientist assigned the goal of understanding the usage of surgical supplies for different procedures and surgeons. You have been given a dataset of the supplies that are used for each surgical case, and also a second dataset which gives you the price of each of the items used in surgery. The dataset encompasses the last month of surgeries at your hospital.

## The Goal
Your goal is to answer the following questions:

 1. How many of each item were used over the last month?
 2. What is the average number of items used for each procedure? 
 3. What is the average total cost of supplies for each procedure?

### Total Item Usage
The output for 1) should look like a table with the following columns:

Item Name || Total Number of Items Used

### Average Items per Procedure
The output for 2) should be a table with the following columns:

Procedure Name || Average Number of Items Used per Case

### Average Cost per Procedure
The output for 3) should be a table with the following columns:

Procedure Name || Average Total Cost of Items Used per Case

# Dataset Overview
Here is an explanation of the dataset you have been given:

## hospital-supply-usage.csv

```
case_id: A unique identifier for a single surgical case
primary_surgeon: The surgeon on the case
primary_procedure: The name of the procedure that was performed
item_name: The name of the item used
item_id: A unique id for each item
number_used: The number of items used
number_wasted: The number of items wasted
```

## pricing.csv
```
item_id: A unique identifier for the item (will match item_id in the hospital-supply-usage.csv dataset)
price: The price of the item
```

# Solution Presentation
The final deliverrable is for the following command to output each of the three
outputs described above:
```
python test_04/run.py
```

# Notes
Feel free to change out any stub class implementations, add unit tests (pytest), etc. Whatever 
you'd do normally as part of your workflow! The only thing that matters is that `python test_04/run.py`
will produce the answers we're looking for.


