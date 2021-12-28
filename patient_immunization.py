"""
Lucas Jensen
Patient class and Immunization class for main.py of the Solv -> ALERT program
Last updated: 12/28/2021
"""


def get_batch_name():
    while True:
        batch = input("Batch name: ")
        if " " in batch or "." in batch:
            print("ERROR: don't use a space or period.")
        else:
            return batch


def get_solv_file():
    while True:
        solv_file = input("What is the name of the Solv csv file: ")
        solv_file = f"data/Solv_data/{solv_file}"
        try:
            with open(solv_file, 'r') as _:
                return solv_file
        except FileNotFoundError:
            print("ERROR: file not found. Is it in the data/Solv_data folder?  Spelling?")
            continue


def format_date(date):
    """
    Param: date: YYYY-MM-DD or MM/DD/YYYY or M/DD/YYYY
    return: MMDDYYYY as string
    """

    new_list = []

    if date[4] == '-':

        new_list.append(date[5])
        new_list.append(date[6])
        new_list.append(date[8])
        new_list.append(date[9])
        new_list.append(date[0])
        new_list.append(date[1])
        new_list.append(date[2])
        new_list.append(date[3])

    else:
        for char in date:
            if char != '/':
                new_list.append(char)

    new_date = ''.join(new_list)

    return new_date


def format_body_site(arm_str):
    """
    formats the site of the vaccine injection
    :param arm_str: "Left Deltoid" or "Right Deltoid"
    :return: "LD" or "RD"
    """
    if "right" in arm_str.lower():
        return "RD"
    elif "left" in arm_str.lower():
        return "LD"
    else:
        return ""


def format_sex(sex):
    """
    Formats a patient's gender to match ALERT iis guidelines
    :param sex: "Male" or "Female"
    :return: "M" or "F"
    """
    if sex == "Male":
        return "M"
    elif sex == "Female":
        return "F"
    else:
        return "U"


def format_ethnicity(ethnicity):
    """
    Formats a patient's ethnicity to match ALERT iis guidelines
    :param ethnicity: a string of ethnicity
    :return: "NH" or "H"
    """
    if ethnicity == "Not Hispanic/Latino":
        return "NH"
    elif ethnicity == "Hispanic/Latino":
        return "H"
    else:
        return ""


class Patient:
    """Represents an immunization given, intended for COVID-19 vaccines"""

    def __init__(self, record, first, middle, last, birth_date, maiden, sex, race, ethnicity, immunization_obj):
        """Initialize all data members as private"""
        self._record = record
        self._status = "A"
        self._first = first
        self._middle = middle
        self._last = last
        self._suffix = ""
        self._birth_date = birth_date
        self._death_date = ""
        self._mother_first = ""
        self._mother_maiden = maiden
        self._mother_HBsAG = ""
        self._sex = sex
        self._race = race
        self._native_american = ""
        self._asian = ""
        self._native_hawaiian = ""
        self._black = ""
        self._white = ""
        self._other_race = ""
        self._ethnicity = ethnicity
        self._ssn = ""
        self._contact = ""
        self._patient_id = ""
        self._medicaid_id = ""
        self._rp_first = ""  # responsible party first name
        self._rp_middle = ""
        self._rp_last = ""
        self._rp_relationship = ""
        self._street_address = ""
        self._other_address = ""
        self._po_box = ""
        self._city = ""
        self._state = ""
        self._zip = ""
        self._county = ""
        self._phone = ""
        self._sending_org = "AL3080"  # AL3080 is the organization code for White Bird Clinic
        self._immunization_obj = immunization_obj

    def set_race_info(self):
        """Uses the race parameter to set more specific details"""
        if self._race == "White":
            self._white = "Y"
        elif self._race == "American Indian or Alaska Native":
            self._native_american = "Y"
        elif self._race == "Black or African American":
            self._black = "Y"
        elif self._race == "Hawaiian or Pacific Islander":
            self._native_hawaiian = "Y"
        elif self._race == "Asian":
            self._asian = "Y"
        elif self._race == "Other":
            self._other_race = "Y"

    def get_record(self):
        return self._record

    def get_status(self):
        return self._status

    def get_first(self):
        return self._first

    def get_middle(self):
        return self._middle

    def get_last(self):
        return self._last

    def get_suffix(self):
        return self._suffix

    def get_birth_date(self):
        return format_date(self._birth_date)

    def get_death_date(self):
        return self._death_date

    def get_mother_first(self):
        return self._mother_first

    def get_mother_maiden(self):
        return self._mother_maiden

    def get_mother_HBsAG(self):
        return self._mother_HBsAG

    def get_sex(self):
        return format_sex(self._sex)

    def get_native_american(self):
        return self._native_american

    def get_asian(self):
        return self._asian

    def get_native_hawaiian(self):
        return self._native_hawaiian

    def get_black(self):
        return self._black

    def get_white(self):
        return self._white

    def get_other(self):
        return self._other_race

    def get_ethnicity(self):
        return format_ethnicity(self._ethnicity)

    def get_ssn(self):
        return self._ssn

    def get_contact(self):
        return self._contact

    def get_patient_id(self):
        return self._patient_id

    def get_medicaid_id(self):
        return self._medicaid_id

    def get_rp_first(self):
        return self._rp_first

    def get_rp_middle(self):
        return self._rp_middle

    def get_rp_last(self):
        return self._rp_last

    def get_rp_relation(self):
        return self._rp_relationship

    def get_street_address(self):
        return self._street_address

    def get_other_address(self):
        return self._other_address

    def get_po_box(self):
        return self._po_box

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_zip(self):
        return self._zip

    def get_county(self):
        return self._county

    def get_phone(self):
        return self._phone

    def get_sending_org(self):
        return self._sending_org

    def get_immunization(self):
        return self._immunization_obj


class Immunization:
    """Represents a COVID-19 immunization. We be used in the Patient class"""

    def __init__(self, manufacturer, vaccination_date, body_site, lot_number, giver):
        self._ndc = self._set_ndc(manufacturer)
        self._trade_name = self._set_trade_name(manufacturer)
        self._cpt = self._set_cpt(manufacturer)
        self._cvx = self._set_cvx(manufacturer)
        self._vaccine_group = "COVID-19"
        self._vaccination_date = vaccination_date
        self._route_code = "IM"  # intramuscular
        self._body_site = body_site
        self._reaction_code = ""
        self._manufacturer_code = ""  # this code is not required and supporting documentation is incomplete
        self._info_source = ""
        self._lot_number = lot_number
        self._provider_name = "White Bird Medical Clinic"
        self._giver = giver
        self._sending_org = "AL3080"
        self._eligibility = "O"  # "O" is the code for "Other State Supplied"

    @staticmethod
    def _set_ndc(manufacturer):
        manu = manufacturer.lower()
        if manu == "moderna":
            return "80777-0273-10"
        elif manu == "janssen" or manu == "j&j":
            return "59676-0580-05"
        elif manu == "pfizer":
            return "59267-1000-01"
        else:
            print("ERROR: check manufacturer column")
            return False

    @staticmethod
    def _set_cpt(manufacturer):
        manu = manufacturer.lower()
        if manu == "moderna":
            return "91301"
        elif manu == "janssen" or manu == "j&j":
            return "91303"
        elif manu == "pfizer":
            return "91300"
        else:
            print("ERROR: check manufacturer column (cpt)")
            return False

    @staticmethod
    def _set_trade_name(manufacturer):
        manu = manufacturer.lower()
        if manu == "moderna":
            return "Moderna COVID-19 Vaccine"
        elif manu == "janssen" or manu == "j&j":
            return "Janssen COVID-19 Vaccine"
        elif manu == "pfizer":
            return "Pfizer COVID-19 Vaccine"
        else:
            print("ERROR: check manufacturer column (trade)")
            print(manu)
            return False

    @staticmethod
    def _set_cvx(manufacturer):
        manu = manufacturer.lower()
        if manu == "moderna":
            return "207"
        elif manu == "janssen" or manu == "j&j":
            return "212"
        elif manu == "pfizer":
            return "208"
        else:
            print("ERROR: check manufacturer column (cvx)")
            print(manu)
            return False

    def get_reaction(self):
        return self._reaction_code

    def get_ndc(self):
        return self._ndc

    def get_trade_name(self):
        return self._trade_name

    def get_cpt(self):
        return self._cpt

    def get_cvx(self):
        return self._cvx

    def get_vaccine_group(self):
        return self._vaccine_group

    def get_vaccination_date(self):
        return format_date(self._vaccination_date)

    def get_route(self):
        return self._route_code

    def get_body_site(self):
        return format_body_site(self._body_site)

    def get_manufacturer_code(self):
        return self._manufacturer_code

    def get_info_source(self):
        return self._info_source

    def get_lot_number(self):
        return self._lot_number

    def get_provider_name(self):
        return self._provider_name

    def get_giver(self):
        return self._giver

    def get_sending_org(self):
        return self._sending_org

    def get_eligibility(self):
        return self._eligibility


if __name__ == "__main__":
    print(format_date("4/2/1951"))
