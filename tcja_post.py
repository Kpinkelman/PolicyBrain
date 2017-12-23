from post_reform import (LOCAL_BASE_URL, TEST_BASE_URL,
                         get_session, post_reform)


data = {
    u'start_year': str(2018),
    u'csrfmiddlewaretoken': None,
    u'has_errors': [u'False']
}

# PolicyBrain post format
tcja_fields = {
    "II_rt1": ["0.1,*,*,*,*,*,*,*,0.1"],
    "II_rt2": ["0.12,*,*,*,*,*,*,*,0.15"],
    "II_rt3": ["0.22,*,*,*,*,*,*,*,0.25"],
    "II_rt4": ["0.24,*,*,*,*,*,*,*,0.28"],
    "II_rt5": ["0.32,*,*,*,*,*,*,*,0.33"],
    "II_rt6": ["0.35,*,*,*,*,*,*,*,0.35"],
    "II_rt7": ["0.37,*,*,*,*,*,*,*,0.396"],

    "II_brk1_0": ["9525,*,*,*,*,*,*,*,11242"],
    "II_brk1_1": ["19050,*,*,*,*,*,*,*,22484"],
    "II_brk1_2": ["9525,*,*,*,*,*,*,*,11242"],
    "II_brk1_3": ["13600,*,*,*,*,*,*,*,16094"],

    "II_brk2_0": ["38700,*,*,*,*,*,*,*,45751"],
    "II_brk2_1": ["77400,*,*,*,*,*,*,*,91502"],
    "II_brk2_2": ["38700,*,*,*,*,*,*,*,45751"],
    "II_brk2_3": ["51800,*,*,*,*,*,*,*,61242"],

    "II_brk3_0": ["82500,*,*,*,*,*,*,*,110791"],
    "II_brk3_1": ["165000,*,*,*,*,*,*,*,184571"],
    "II_brk3_2": ["82500,*,*,*,*,*,*,*,92286"],
    "II_brk3_3": ["82500,*,*,*,*,*,*,*,158169"],

    "II_brk4_0": ["157500,*,*,*,*,*,*,*,231045"],
    "II_brk4_1": ["315000,*,*,*,*,*,*,*,281317"],
    "II_brk4_2": ["157500,*,*,*,*,*,*,*,140659"],
    "II_brk4_3": ["157500,*,*,*,*,*,*,*,256181"],

    "II_brk5_0": ["200000,*,*,*,*,*,*,*,502356"],
    "II_brk5_1": ["400000,*,*,*,*,*,*,*,502356"],
    "II_brk5_2": ["200000,*,*,*,*,*,*,*,251178"],
    "II_brk5_3": ["200000,*,*,*,*,*,*,*,502356"],

    "II_brk6_0": ["500000,*,*,*,*,*,*,*,504406"],
    "II_brk6_1": ["600000,*,*,*,*,*,*,*,567457"],
    "II_brk6_2": ["300000,*,*,*,*,*,*,*,283728"],
    "II_brk6_3": ["500000,*,*,*,*,*,*,*,535931"],

    "PT_rt1": ["0.1,*,*,*,*,*,*,*,0.1"],
    "PT_rt2": ["0.12,*,*,*,*,*,*,*,0.15"],
    "PT_rt3": ["0.22,*,*,*,*,*,*,*,0.25"],
    "PT_rt4": ["0.24,*,*,*,*,*,*,*,0.28"],
    "PT_rt5": ["0.32,*,*,*,*,*,*,*,0.33"],
    "PT_rt6": ["0.35,*,*,*,*,*,*,*,0.35"],
    "PT_rt7": ["0.37,*,*,*,*,*,*,*,0.396"],

    "PT_brk1_0": ["9525,*,*,*,*,*,*,*,11242"],
    "PT_brk1_1": ["19050,*,*,*,*,*,*,*,22484"],
    "PT_brk1_2": ["9525,*,*,*,*,*,*,*,11242"],
    "PT_brk1_3": ["13600,*,*,*,*,*,*,*,16094"],

    "PT_brk2_0": ["38700,*,*,*,*,*,*,*,45751"],
    "PT_brk2_1": ["77400,*,*,*,*,*,*,*,91502"],
    "PT_brk2_2": ["38700,*,*,*,*,*,*,*,45751"],
    "PT_brk2_3": ["51800,*,*,*,*,*,*,*,61242"],

    "PT_brk3_0": ["82500,*,*,*,*,*,*,*,110791"],
    "PT_brk3_1": ["165000,*,*,*,*,*,*,*,184571"],
    "PT_brk3_2": ["82500,*,*,*,*,*,*,*,92286"],
    "PT_brk3_3": ["82500,*,*,*,*,*,*,*,158169"],

    "PT_brk4_0": ["157500,*,*,*,*,*,*,*,231045"],
    "PT_brk4_1": ["315000,*,*,*,*,*,*,*,281317"],
    "PT_brk4_2": ["157500,*,*,*,*,*,*,*,140659"],
    "PT_brk4_3": ["157500,*,*,*,*,*,*,*,256181"],

    "PT_brk5_0": ["200000,*,*,*,*,*,*,*,502356"],
    "PT_brk5_1": ["400000,*,*,*,*,*,*,*,502356"],
    "PT_brk5_2": ["200000,*,*,*,*,*,*,*,251178"],
    "PT_brk5_3": ["200000,*,*,*,*,*,*,*,502356"],

    "PT_brk6_0": ["500000,*,*,*,*,*,*,*,504406"],
    "PT_brk6_1": ["600000,*,*,*,*,*,*,*,567457"],
    "PT_brk6_2": ["300000,*,*,*,*,*,*,*,283728"],
    "PT_brk6_3": ["500000,*,*,*,*,*,*,*,535931"],

    "PT_exclusion_rt": ["0.2,*,*,*,*,*,*,*,0.0"],
    "PT_exclusion_wage_limit": ["0.5,*,*,*,*,*,*,*,9e99"],

    "STD_0": ["12000,*,*,*,*,*,*,*,7655"],
    "STD_1": ["24000,*,*,*,*,*,*,*,15311"],
    "STD_2": ["12000,*,*,*,*,*,*,*,7655"],
    "STD_3": ["18000,*,*,*,*,*,*,*,11272"],

    "II_em": ["0,*,*,*,*,*,*,*,4883"],

    "CTC_ps_0": ["200000,*,*,*,*,*,*,*,75000"],
    "CTC_ps_1": ["400000,*,*,*,*,*,*,*,110000"],
    "CTC_ps_2": ["200000,*,*,*,*,*,*,*,55000"],
    "CTC_ps_3": ["200000,*,*,*,*,*,*,*,75000"],

    "CTC_c": ["1400,*,*,*,1500,*,*,1600,1000"],

    "DependentCredit_Child_c": ["600,*,*,*,500,*,*,400,0"],
    "DependentCredit_Nonchild_c": ["500,*,*,*,*,*,*,*,0"],
    "DependentCredit_before_CTC": ["True"],

    "ACTC_Income_thd": ["2500,*,*,*,*,*,*,*,3000"],

    "AMT_em_0": ["70300,*,*,*,*,*,*,*,65462"],
    "AMT_em_1": ["109400,*,*,*,*,*,*,*,101870"],
    "AMT_em_2": ["54700,*,*,*,*,*,*,*,50935"],
    "AMT_em_3": ["70300,*,*,*,*,*,*,*,65461"],

    "AMT_em_ps_0": ["500000,*,*,*,*,*,*,*,145511"],
    "AMT_em_ps_1": ["1000000,*,*,*,*,*,*,*,193974"],
    "AMT_em_ps_2": ["500000,*,*,*,*,*,*,*,96987"],
    "AMT_em_ps_3": ["500000,*,*,*,*,*,*,*,145511"],

    "ALD_DomesticProduction_hc": ["1,*,*,*,*,*,*,*,0"],
    "ALD_Alimony_hc": ["*,1,*,*,*,*,*,*,0"],

    "ID_prt": ["0,*,*,*,*,*,*,*,0.03"],
    "ID_crt": ["1,*,*,*,*,*,*,*,0.8"],
    "ID_Charity_crt_all": ["0.6,*,*,*,*,*,*,*,0.5"],
    "ID_Casualty_hc": ["1,*,*,*,*,*,*,*,0"],

    "ID_AllTaxes_c_0": ["10000,*,*,*,*,*,*,*,9e99"],
    "ID_AllTaxes_c_1": ["10000,*,*,*,*,*,*,*,9e99"],
    "ID_AllTaxes_c_2": ["5000,*,*,*,*,*,*,*,9e99"],
    "ID_AllTaxes_c_3": ["10000,*,*,*,*,*,*,*,9e99"],

    "ID_Miscellaneous_hc": ["1,*,*,*,*,*,*,*,0"],
    "ID_Medical_frt": ["0.075,0.1"],
    "cpi_offset": ["<,-0.0025"]
}

data.update(tcja_fields)

post_url = TEST_BASE_URL

# do first post
session, csrftoken = get_session(url=post_url)
data[u'csrfmiddlewaretoken'] = csrftoken

result = post_reform(session, data, url=post_url)
print(result)

# reform gives warnings; get token and resubmit
if result[1] == "taxbrain":
    next_session, pk, response = result
    next_token = str(next_session.cookies['csrftoken'])

    data['csrfmiddlewaretoken'] = next_token
    # keep track of context data
    data['has_errors'] = [u'True']
    # resubmit params and should be good to go if only warnings are thrown
    result = post_reform(next_session, data, url=post_url)
    print(result)
