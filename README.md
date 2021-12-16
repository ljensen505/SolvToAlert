# SolvToAlert
A Python script which takes patient data from Solv and formats it for a bulk upload to ALERT iis

This program uses an Immunization class and a Patient class to manage patient data, which is gathered from a data file
generated from Solv. All file types are csv. Data items are tracked using their indices, which are determined by reading
the Solv csv file.

Recent changes:

Changed eligibility code from S (Special Projects) to O (Other State Supplied)

General improvements reflecting OOP 

# Directions
Make sure you have Python3 installed.  Consult IT if you do not.

Download a patient data csv file from Solv for the desired date range. Save the csv file under data/Solv_data

Example: `data/Solv_data/solv_patient_report[...].csv`

You can rename the file from Solv to whatever you want, but remember the file name.

Run the program! Using the terminal, navigate to the directory where main.py (and this README) is stored, and then enter
`python main.py`

You'll be prompted for two items.  The batch name can be whatever you want - I typically use the current month.  The
name of the Solv csv file is whatever you named the file you downloaded before

Example: 

`Batch name: December15`

`What is the name of the Solv csv file: solv_patient_report[...].csv`

You should not have two generated files for ALERT iis.  The patient data file can be found in data/Patient and the
immunization file can be found in data/Immunization.  Both will be titled according to your previous batch name.

Example: `data/Patient/December15_patients.csv`, `data/Immunization/December15_immunizations.csv`

You can now use both of these files to Exchange Data with ALERT iis.

