import numpy as np
import pandas as pd
from test_04.supply_analysis.analysis import SupplyUsageAnalysis
from carta_interview import Datasets, get_data_file

USAGE_FILENAME = get_data_file(Datasets.SUPPLY_USAGE)
PRICING_FILENAME = get_data_file(Datasets.PRICING)

analysis = SupplyUsageAnalysis(USAGE_FILENAME, PRICING_FILENAME)
total_item_usage = analysis.get_total_item_usage()
avg_items_per_procedure = analysis.get_avg_items_per_procedure()
avg_cost_per_procedure = analysis.get_avg_cost_per_procedure()

## Print your result here!
print("Total Item Usage")
print(total_item_usage)
print("\n\n")

print("Average Items per Procedure")
print(avg_items_per_procedure)
print("\n\n")

print("Average Cost per Procedure")
print(avg_cost_per_procedure)
print("\n\n")
