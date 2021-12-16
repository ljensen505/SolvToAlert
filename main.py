"""
Written by Lucas Jensen for White Bird Clinic
The main program for transferring data between Solv and ALERT iis
Last updated: 12/15/2021
"""

import csv
from patient_immunization import Patient, Immunization

month = "TEST_MONTH"
solv_file = "data/Solv_data/solv_patient_report_Outreach Vaccine Clinic_O_20211102_20211214_814ea322-5de2-11ec-9ba4-32ce41331b1f.csv"
patient_file = f"data/Patient/{month}_patients.csv"
immunization_file = f"data/Immunization/{month}_immunizations.csv"


def gather_date(data_file):
    """
    Creates a list of patient objects based on a csv file from Solv
    :param data_file: name of the data file from Solv
    :return: list of patient objects
    """
    with open(data_file, 'r') as infile:
        reader = csv.reader(infile)
        header_row = next(reader)
        patients = []

        # Set important indices or values from Solv
        vaccination_date = header_row.index('Date')
        first_name = header_row.index('Patient First Name')
        middle_name = ""
        last_name = header_row.index('Patient Last Name')
        birth_date = header_row.index('Date Of Birth')
        race = header_row.index('Patient Race')
        ethnicity_index = header_row.index('Patient Ethnicity')
        sex_index = header_row.index('Birth Sex')
        giver_index = header_row.index('Name of Vaccine Administrator (First/Last)')
        lot_index = header_row.index('Lot#')
        arm = header_row.index('Which arm is receiving vaccine?')
        brand = header_row.index('Vaccine Brand')
        # insert code for maiden name not existing as a column
        mother_maiden_index = header_row.index("Please enter your Mother's Maiden name")

        for i, row in enumerate(reader):
            if row[lot_index]:
                immunization = Immunization(row[brand], row[vaccination_date], row[arm], row[lot_index],
                                            row[giver_index])
                patient = Patient(i + 1, row[first_name], middle_name, row[last_name], row[birth_date],
                                  row[mother_maiden_index], row[sex_index], row[race], row[ethnicity_index],
                                  immunization)
                patient.set_race_info()
                patients.append(patient)

    return patients


def make_patient_file(patients, filename):
    """
    Makes a csv file of patient info
    :param patients: list of patient objects
    :param filename: the filename for the patient file, previously defined
    :return: nothing
    """
    with open(filename, 'w') as outfile:
        # file header
        outfile.write(
            "Blank,Record Identifier,Patient Status,First Name,Middle Name,Last Name,Name Suffix,Birth Date,"
            "Death Date,Mother's First Name,Mother's Maiden Last Name,Mother's HBsAG Status,Sex (Gender),"
            "American Indian or Alaska Native,Asian,Native Hawaiian or Other Pacific Islander,"
            "Black or African-American,White,Other Race,Ethnicity,Social Security Number,Contact Allowed,Patient ID,"
            "Medicaid ID,Responsible Party First Name,Responsible Party Middle Name,Responsible Party Last Name,"
            "Responsible Party Relationship,Street Address Line,Other Address Line,PO Box Route Line,City,State,"
            "Zip Code,County,Phone,Sending Organization\n")
        for patient in patients:
            # all rows start with a blank entry. No idea why. It's in the ALERT iis documentation
            blank = ""
            outfile.write(
                f"{blank},{patient.get_record()},{patient.get_status()},{patient.get_first()},{patient.get_middle()},"
                f"{patient.get_last()},{patient.get_suffix()},{patient.get_birth_date()},{patient.get_death_date()},"
                f"{patient.get_mother_first()},{patient.get_mother_maiden()},{patient.get_mother_HBsAG()},"
                f"{patient.get_sex()},{patient.get_native_american()},{patient.get_asian()},"
                f"{patient.get_native_hawaiian()},{patient.get_black()},{patient.get_white()},"
                f"{patient.get_other()},{patient.get_ethnicity()},{patient.get_ssn()},{patient.get_contact()},"
                f"{patient.get_patient_id()},{patient.get_medicaid_id()},{patient.get_rp_first()},"
                f"{patient.get_rp_middle()},{patient.get_rp_last()},{patient.get_rp_relation()},"
                f"{patient.get_street_address()},{patient.get_other_address()},{patient.get_po_box()},"
                f"{patient.get_city()},{patient.get_state()},{patient.get_zip()},{patient.get_county()},"
                f"{patient.get_phone()},{patient.get_sending_org()}\n")


def make_immunization_file(patients, filename):
    """
    Makes a csv file of immunization info
    :param patients:
    :param filename:
    :return:
    """
    with open(filename, 'w') as outfile:
        # file header
        outfile.write(
            "Blank,Record Identifier,NDC Code,Trade Name,CPT Code,CVX Code,Vaccine Group,Vaccination Date,"
            "Administration Route Code,Body Site Code,Reaction Code,Manufacturer Code,Immunization Information "
            "Source,Lot Number,Provider Name,Administered By Name,Sending Organization,Vaccine Eligibility\n")
        for patient in patients:
            immunization = patient.get_immunization()
            # all rows start with a blank entry. No idea why. It's in the ALERT iis documentation
            blank = ""
            outfile.write(
                f"{blank},{patient.get_record()},{immunization.get_ndc()},{immunization.get_trade_name()},"
                f"{immunization.get_cpt()},{immunization.get_cvx()},{immunization.get_vaccine_group()},"
                f"{immunization.get_vaccination_date()},{immunization.get_route()},{immunization.get_body_site()},"
                f"{immunization.get_reaction()},{immunization.get_manufacturer_code()},{immunization.get_info_source()},"
                f"{immunization.get_lot_number()},{immunization.get_provider_name()},{immunization.get_giver()},"
                f"{immunization.get_sending_org()},{immunization.get_eligibility()}\n")


def main():
    patients = gather_date(solv_file)
    make_patient_file(patients, patient_file)
    make_immunization_file(patients, immunization_file)


if __name__ == "__main__":
    main()
