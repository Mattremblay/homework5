import os
import analysis

def test_average():
    avg = analysis.average_inflammations(0)
    assert(avg == 5.45)

def test_max():
    max = analysis.max_inflammations(0)
    assert(max == 18)

def test_acute_patient():
    patient_id = analysis.acute_patient()
    assert(patient_id == 46)
