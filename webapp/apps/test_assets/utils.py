

def do_micro_sim(client, reform):
    '''do the proper sequence of HTTP calls to run a microsim'''
    #Monkey patch to mock out running of compute jobs
    import sys
    from webapp.apps.taxbrain import views
    webapp_views = sys.modules['webapp.apps.taxbrain.views']
    webapp_views.dropq_compute = MockCompute()
    from webapp.apps.dynamic import views
    dynamic_views = sys.modules['webapp.apps.dynamic.views']
    dynamic_views.dropq_compute = MockCompute(num_times_to_wait=1)

    response = client.post('/taxbrain/', reform)
    # Check that redirect happens
    assert response.status_code == 302
    idx = response.url[:-1].rfind('/')
    assert response.url[:idx].endswith("taxbrain")
    return response


def do_micro_sim_from_file(client, reform_text, assumptions_text):
    #Monkey patch to mock out running of compute jobs
    import sys
    from webapp.apps.taxbrain import views
    webapp_views = sys.modules['webapp.apps.taxbrain.views']
    webapp_views.dropq_compute = MockCompute()

    tc_file = SimpleUploadedFile("test_reform.json", reform_text)
    tc_file2 = SimpleUploadedFile("test_assumptions.json", assumptions_text)
    data = {u'docfile': tc_file,
            u'assumpfile': tc_file2,
            u'has_errors': [u'False'],
            u'start_year': unicode(START_YEAR), 'csrfmiddlewaretoken':'abc123'}

    response = client.post('/taxbrain/file/', data)
    # Check that redirect happens
    assert response.status_code == 302
    return response


def check_posted_params(mock_compute, params_to_check, start_year):
    """
    Make sure posted params match expected results
    user_mods: parameters that are actually passed to taxcalc
    params_to_check: gives truth value for parameters that we want to check
                     (formatted as taxcalc dict style reform)
    """
    last_posted = mock_compute.last_posted
    user_mods = json.loads(last_posted["user_mods"])
    assert last_posted["first_budget_year"] == start_year
    for year in params_to_check:
        for param in params_to_check[year]:
            assert user_mods[str(year)][param] == params_to_check[year][param]
