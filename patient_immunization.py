"""
Lucas Jensen
Patient class and Immunization class for main.py of the Solv -> ALERT program
Last updated: 12/15/2021
"""

class Patient:
    """Represents an immunization given, intended for COVID-19 vaccines"""
    def __init__(self, record, first, middle, last, birth_date, maiden, sex, native_american, asian, native_hawaiian, black,
                 white, other_race, ethnicity):
        self._record = record
        self._status = "A"
        self._first = first
        self._middle = middle
        self._last = last
        self._suffix = None
        self._birth_date = birth_date
        self._death_date = None
        self._mother_maiden = maiden
        self._mother_HBsAG = None
        self._sex = sex
        self._native_american = native_american
        self._asian = asian
        self._native_hawaiian = native_hawaiian
        self._black = black
        self._white = white
        self._other_race = other_race
        self._ethnicity = ethnicity
        self._ssn = None
        self._contact = None
        self._patient_id = None
        self._medicaid_id = None
        self._rp_first = None  # responsible party first name
        self._rp_middle = None
        self._rp_last = None
        self._rp_relationship = None
        self._street_address = None
        self._other_address = None
        self._po_box = None
        self._city = None
        self._state = None
        self._zip = None
        self._county = None
        self._phone = None
        self._sending_org = "AL3080"  # AL3080 is the organization code for White Bird Clinic
        # self._immunization = Immunization()

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
        return self._birth_date

    def get_death_date(self):
        return self._death_date

    def get_mother_maiden(self):
        return self._mother_maiden

    def get_mother_HBsAG(self):
        return self._mother_HBsAG

    def get_sex(self):
        return self._sex

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
        return self._ethnicity

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
