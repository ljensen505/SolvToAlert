# SolvToAlert
A Python script which takes patient data from Solv and formats it for a bulk upload to ALERT iis

This program uses an Immunization class and a Patient class to manage patient data, which is gathered from a data file
generated from Solv. All file types are csv. Data items are tracked using their indices, which are determined by reading
the Solv csv file.

Known issues:

Mother's Maiden Name isn't always included in the Solv data file. A simple check for that column existing should fix it.
If there is no column, the Patient data member for mother's maiden name can be an empty string.

Recent fixes:

Changed eligibility code from S (Special Projects) to O (Other State Supplied)

General improvements reflecting OOP 