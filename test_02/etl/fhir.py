

class FHIRDataTransformer(object):
    """Transform data in postgres into Patient/Encounter resources"""

    def get_patient_resources(self):
        ## Query data in postgres, produce array of Patient FHIR resources
        return []

    def get_encounter_resources(self):
        ## Query data in postgres, produce array of Encounter FHIR resources
        return []