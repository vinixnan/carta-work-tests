# Introduction
This is a test for seeing how well you can get around with typically messy clinical data provided in various forms, including clinical notes processed with NLP, and the ability to interpret literature to a real-world situation

In this analysis, you are assuming the role of a data scientist assigned the goal of automating a field in a cardiac registry concerned with pharmacologic cardiovascular support in infants undergoing cardiac surgery with bypass.  In particular, you will be examining the vasoactive-inotropic score (VIS) as defined in the following publication:

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4159673/
The full text has also been provided as a PDF.

You have been given a dataset of the supplies that are used for each surgical case, and also a second dataset which gives you the price of each of the items used in surgery. The dataset encompasses the last month of surgeries at your hospital.

You will use [FHIR](https://www.hl7.org/fhir) as a common schema across the various data sources.

## The Goal
Your goal is to answer the following questions:

 1. Write a function that converts the parsed clinical note into FHIR Encounter and Procedure resources
 2. What was the patient's VIS score at all times from hospital admission to discharge?
 3. What was the patient's maximum VIS score in their first 24 hours after CICU admission?

### FHIR Resources
The output for 1) should be a function or functions which examine the parsed clinical note, and produce two [FHIR Encounter resources](https://www.hl7.org/fhir/encounter.html) (one for the hospitalization and one for the CICU stay), and one [FHIR Procedure resources](https://www.hl7.org/fhir/procedure.html) following the official documentation.  All FHIR resources can be in the form of Python dictionaries which follow the schema in the documentation.

Each FHIR resources should be saved to a clearly named .json file.

* results/hospital-encounter.json
* results/cicu-encounter.json
* results/asd-procedure.json

Bonus:
* results/patient.json
* results/asd-condition.json
* results/echo-procedure.json


### VIS Score Time-Series
The output for 2) should look like a plot with time on the X-axis, and VIS score on the Y-axis.  Significant points in time should be clearly indicated.

* results/VIS_timeseries.png

### Max VIS Score
The output for 3) should be a function which takes only FHIR resources as inputs, and returns the following
```
{
    "value":  <the max VIS score>,
    "start_datetime":  <when the patient had the max VIS score (start of interval)>,
    "duration":  <total number of minutes the patient was at the maximum VIS score>,
}
```
* results/maximum_VIS_score.json

# Dataset Overview
Here is an explanation of the dataset you have been given:


## raw-sample-note.txt
The raw text of the sample clinical note provided for your reference.  No processing should be performed directly on this note.

## parsed-sample-note.json
The output after the raw sample note is fed through the Natural Language Processing pipeline.  Entities in the note are coded under UMLS.  Use the coded entities to construct the required FHIR resources.

https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt


| UMLS Code | Term |
|---|---|
|   | Atrial Septal Defect |

birth date
gender
male
female


## medication-administrations.json
This is a list of [FHIR MedicationAdministration resources](https://www.hl7.org/fhir/medicationadministration.html) for the sample patient.

## medications.json
This is a list of [FHIR Medication resources](https://www.hl7.org/fhir/medication.html) for the sample patient.

## procedure_log.csv
This is an extract of inpatient procedures, including both surgical procedures and other inpatient procedures.

```
mrn:  The patient's Medical Record Number
procedure_id: A unique identifier for a single procedure
practitioner: Who performed the procedure
primary_procedure_name: The name of the procedure that was performed
primary_procedure_code: A SNOMED-CT code for the procedure
procedure_date: The date the procedure was performed
procedure_time: The time of day the procedure was performed
```


# Solution Presentation
The final deliverable is for the following command to output each of the three outputs described above, saved to the test_05/results directory:
```
python test_05/run.py
```

# Notes
Feel free to change out any stub class implementations, add unit tests (pytest), etc. Whatever 
you'd do normally as part of your workflow! The only thing that matters is that `python test_04/run.py`
will produce the answers we're looking for.


# References:
SNOMED-CT:  https://www.nlm.nih.gov/healthit/snomedct/index.html.  Many browsers can be found online.
