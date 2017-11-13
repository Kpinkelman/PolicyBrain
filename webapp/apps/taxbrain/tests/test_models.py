from django.test import TestCase
from django.test import Client
import json
import os
import numpy as np
from datetime import datetime

from ..models import TaxSaveInputs, JSONReformTaxCalculator, OutputUrl
from ..forms import PersonalExemptionForm
from ...test_assets.test_reform import test_coverage_fields as fields

START_YEAR = 2016

CURDIR = os.path.abspath(os.path.dirname(__file__))

class TaxBrainJSONReformModelTest(TestCase):
    """Test taxbrain JSONReformTaxCalculator."""

    def setUp(self):
        # Every test needs a client.
        self.test_string = "".join(["1" for x in range(100000)])

    def test_create_reforms(self):
        self.reforms = JSONReformTaxCalculator.objects.create(
            reform_text=self.test_string,
            raw_reform_text=self.test_string,
            assumption_text=self.test_string,
            raw_assumption_text=self.test_string
        )

class TaxBrainResultsTest(TestCase):

    def setUp(self):
        pass

    def get_taxbrain_model(self, first_year=2017, quick_calc=False,
                           taxcalc_version="0.13.0", webapp_vers="1.2.0",
                           exp_comp_datetime = "2017-10-10"):
        self.fields = fields.copy()
        del self.fields['_state']
        del self.fields['creation_date']
        del self.fields['id']
        for key in self.fields:
            if isinstance(self.fields[key], list):
                self.fields[key] = ','.join(map(str, self.fields[key]))
        personal_inputs = PersonalExemptionForm(first_year, self.fields)
        print(personal_inputs.errors)
        model = personal_inputs.save()
        model.job_ids = '1,2,3'
        model.json_text = None
        model.first_year = first_year
        model.quick_calc = quick_calc
        model.save()

        unique_url = OutputUrl()
        unique_url.taxcalc_version = taxcalc_version
        unique_url.webapp_vers = webapp_vers
        unique_url.unique_inputs = model
        unique_url.model_pk = model.pk
        unique_url.exp_comp_datetime = exp_comp_datetime
        unique_url.save()

        return unique_url

    def test_tc_lt_0130(self):
        old_path = os.path.join(CURDIR, "skelaton_res_lt_0130.json")
        with open(old_path) as js:
            old_labels = json.loads(js.read())

        new_path = os.path.join(CURDIR, "skelaton_res_gt_0130.json")
        with open(new_path) as js:
            new_labels = json.loads(js.read())

        unique_url = self.get_taxbrain_model(taxcalc_version="0.10.2",
                                             webapp_vers="1.1.1")

        model = unique_url.unique_inputs
        model.tax_result = old_labels
        model.creation_date = datetime.now()

        np.testing.assert_equal(model.tax_result, new_labels)


    def test_tc_gt_0130(self):
        old_path = os.path.join(CURDIR, "skelaton_res_gt_0130.json")
        with open(old_path) as js:
            old_labels = json.loads(js.read())

        new_path = os.path.join(CURDIR, "skelaton_res_gt_0130.json")
        with open(new_path) as js:
            new_labels = json.loads(js.read())

        unique_url = self.get_taxbrain_model(taxcalc_version="0.13.0",
                                             webapp_vers="1.2.0")

        model = unique_url.unique_inputs
        model.tax_result = old_labels
        model.creation_date = datetime.now()

        np.testing.assert_equal(model.tax_result, new_labels)
