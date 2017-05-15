from sqlalchemy import Column, Integer, Text, Numeric, Index, Boolean, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from dataactcore.models.baseModel import Base
from dataactcore.models.domainModels import concat_tas


class FlexField(Base):
    """Model for the flex field table."""
    __tablename__ = "flex_field"

    flex_field_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer,
                           ForeignKey("submission.submission_id", ondelete="CASCADE",
                                      name="fk_flex_field_submission_id"),
                           nullable=False, index=True)
    submission = relationship("Submission", uselist=False, cascade="delete")
    job_id = Column(Integer, nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    header = Column(Text)
    cell = Column(Text)
    file_type_id = Column(Integer)


class Appropriation(Base):
    """Model for the appropriation table."""
    __tablename__ = "appropriation"

    appropriation_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer,
                           ForeignKey("submission.submission_id", ondelete="CASCADE",
                                      name="fk_appropriation_submission_id"),
                           nullable=False, index=True)
    submission = relationship("Submission", uselist=False, cascade="delete")
    job_id = Column(Integer, nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    adjustments_to_unobligated_cpe = Column(Numeric)
    agency_identifier = Column(Text)
    allocation_transfer_agency = Column(Text)
    availability_type_code = Column(Text)
    beginning_period_of_availa = Column(Text)
    borrowing_authority_amount_cpe = Column(Numeric)
    budget_authority_appropria_cpe = Column(Numeric)
    budget_authority_available_cpe = Column(Numeric)
    budget_authority_unobligat_fyb = Column(Numeric)
    contract_authority_amount_cpe = Column(Numeric)
    deobligations_recoveries_r_cpe = Column(Numeric)
    ending_period_of_availabil = Column(Text)
    gross_outlay_amount_by_tas_cpe = Column(Numeric)
    main_account_code = Column(Text)
    obligations_incurred_total_cpe = Column(Numeric)
    other_budgetary_resources_cpe = Column(Numeric)
    spending_authority_from_of_cpe = Column(Numeric)
    status_of_budgetary_resour_cpe = Column(Numeric)
    sub_account_code = Column(Text)
    unobligated_balance_cpe = Column(Numeric)
    tas = Column(Text, index=True, nullable=False, default=concat_tas)
    tas_id = Column(Integer, nullable=True)

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(Appropriation, self).__init__(**clean_kwargs)


class ObjectClassProgramActivity(Base):
    """Model for the object_class_program_activity table."""
    __tablename__ = "object_class_program_activity"

    object_class_program_activity_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer,
                           ForeignKey("submission.submission_id", ondelete="CASCADE",
                                      name="fk_object_class_program_activity_submission_id"),
                           nullable=False, index=True)
    submission = relationship("Submission", uselist=False, cascade="delete")
    job_id = Column(Integer, nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    agency_identifier = Column(Text)
    allocation_transfer_agency = Column(Text)
    availability_type_code = Column(Text)
    beginning_period_of_availa = Column(Text)
    by_direct_reimbursable_fun = Column(Text)
    deobligations_recov_by_pro_cpe = Column(Numeric)
    ending_period_of_availabil = Column(Text)
    gross_outlay_amount_by_pro_cpe = Column(Numeric)
    gross_outlay_amount_by_pro_fyb = Column(Numeric)
    gross_outlays_delivered_or_cpe = Column(Numeric)
    gross_outlays_delivered_or_fyb = Column(Numeric)
    gross_outlays_undelivered_cpe = Column(Numeric)
    gross_outlays_undelivered_fyb = Column(Numeric)
    main_account_code = Column(Text)
    object_class = Column(Text)
    obligations_delivered_orde_cpe = Column(Numeric)
    obligations_delivered_orde_fyb = Column(Numeric)
    obligations_incurred_by_pr_cpe = Column(Numeric)
    obligations_undelivered_or_cpe = Column(Numeric)
    obligations_undelivered_or_fyb = Column(Numeric)
    program_activity_code = Column(Text)
    program_activity_name = Column(Text)
    sub_account_code = Column(Text)
    ussgl480100_undelivered_or_cpe = Column(Numeric)
    ussgl480100_undelivered_or_fyb = Column(Numeric)
    ussgl480200_undelivered_or_cpe = Column(Numeric)
    ussgl480200_undelivered_or_fyb = Column(Numeric)
    ussgl483100_undelivered_or_cpe = Column(Numeric)
    ussgl483200_undelivered_or_cpe = Column(Numeric)
    ussgl487100_downward_adjus_cpe = Column(Numeric)
    ussgl487200_downward_adjus_cpe = Column(Numeric)
    ussgl488100_upward_adjustm_cpe = Column(Numeric)
    ussgl488200_upward_adjustm_cpe = Column(Numeric)
    ussgl490100_delivered_orde_cpe = Column(Numeric)
    ussgl490100_delivered_orde_fyb = Column(Numeric)
    ussgl490200_delivered_orde_cpe = Column(Numeric)
    ussgl490800_authority_outl_cpe = Column(Numeric)
    ussgl490800_authority_outl_fyb = Column(Numeric)
    ussgl493100_delivered_orde_cpe = Column(Numeric)
    ussgl497100_downward_adjus_cpe = Column(Numeric)
    ussgl497200_downward_adjus_cpe = Column(Numeric)
    ussgl498100_upward_adjustm_cpe = Column(Numeric)
    ussgl498200_upward_adjustm_cpe = Column(Numeric)
    tas = Column(Text, nullable=False, default=concat_tas)
    tas_id = Column(Integer, nullable=True)

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(ObjectClassProgramActivity, self).__init__(**clean_kwargs)

Index("ix_oc_pa_tas_oc_pa",
      ObjectClassProgramActivity.tas,
      ObjectClassProgramActivity.object_class,
      ObjectClassProgramActivity.program_activity_code,
      unique=False)


class AwardFinancial(Base):
    """Corresponds to entries in File C"""
    __tablename__ = "award_financial"

    award_financial_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer,
                           ForeignKey("submission.submission_id", ondelete="CASCADE",
                                      name="fk_award_financial_submission_id"),
                           nullable=False, index=True)
    submission = relationship("Submission", uselist=False, cascade="delete")
    job_id = Column(Integer, nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    agency_identifier = Column(Text)
    allocation_transfer_agency = Column(Text)
    availability_type_code = Column(Text)
    beginning_period_of_availa = Column(Text)
    by_direct_reimbursable_fun = Column(Text)
    deobligations_recov_by_awa_cpe = Column(Numeric)
    ending_period_of_availabil = Column(Text)
    fain = Column(Text, index=True)
    gross_outlay_amount_by_awa_cpe = Column(Numeric)
    gross_outlay_amount_by_awa_fyb = Column(Numeric)
    gross_outlays_delivered_or_cpe = Column(Numeric)
    gross_outlays_delivered_or_fyb = Column(Numeric)
    gross_outlays_undelivered_cpe = Column(Numeric)
    gross_outlays_undelivered_fyb = Column(Numeric)
    main_account_code = Column(Text)
    object_class = Column(Text)
    obligations_delivered_orde_cpe = Column(Numeric)
    obligations_delivered_orde_fyb = Column(Numeric)
    obligations_incurred_byawa_cpe = Column(Numeric)
    obligations_undelivered_or_cpe = Column(Numeric)
    obligations_undelivered_or_fyb = Column(Numeric)
    parent_award_id = Column(Text)
    piid = Column(Text, index=True)
    program_activity_code = Column(Text)
    program_activity_name = Column(Text)
    sub_account_code = Column(Text)
    transaction_obligated_amou = Column(Numeric)
    uri = Column(Text, index=True)
    ussgl480100_undelivered_or_cpe = Column(Numeric)
    ussgl480100_undelivered_or_fyb = Column(Numeric)
    ussgl480200_undelivered_or_cpe = Column(Numeric)
    ussgl480200_undelivered_or_fyb = Column(Numeric)
    ussgl483100_undelivered_or_cpe = Column(Numeric)
    ussgl483200_undelivered_or_cpe = Column(Numeric)
    ussgl487100_downward_adjus_cpe = Column(Numeric)
    ussgl487200_downward_adjus_cpe = Column(Numeric)
    ussgl488100_upward_adjustm_cpe = Column(Numeric)
    ussgl488200_upward_adjustm_cpe = Column(Numeric)
    ussgl490100_delivered_orde_cpe = Column(Numeric)
    ussgl490100_delivered_orde_fyb = Column(Numeric)
    ussgl490200_delivered_orde_cpe = Column(Numeric)
    ussgl490800_authority_outl_cpe = Column(Numeric)
    ussgl490800_authority_outl_fyb = Column(Numeric)
    ussgl493100_delivered_orde_cpe = Column(Numeric)
    ussgl497100_downward_adjus_cpe = Column(Numeric)
    ussgl497200_downward_adjus_cpe = Column(Numeric)
    ussgl498100_upward_adjustm_cpe = Column(Numeric)
    ussgl498200_upward_adjustm_cpe = Column(Numeric)
    tas = Column(Text, nullable=False, default=concat_tas)
    tas_id = Column(Integer, nullable=True)

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(AwardFinancial, self).__init__(**clean_kwargs)

Index("ix_award_financial_tas_oc_pa",
      AwardFinancial.tas,
      AwardFinancial.object_class,
      AwardFinancial.program_activity_code,
      unique=False)


class AwardFinancialAssistance(Base):
    """Model for D2-Award (Financial Assistance)."""
    __tablename__ = "award_financial_assistance"

    award_financial_assistance_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer,
                           ForeignKey("submission.submission_id", ondelete="CASCADE",
                                      name="fk_award_financial_assistance_submission_id"),
                           nullable=False, index=True)
    submission = relationship("Submission", uselist=False, cascade="delete")
    job_id = Column(Integer, nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    action_date = Column(Text)
    action_type = Column(Text)
    assistance_type = Column(Text)
    award_description = Column(Text)
    awardee_or_recipient_legal = Column(Text)
    awardee_or_recipient_uniqu = Column(Text)
    awarding_agency_code = Column(Text)
    awarding_agency_name = Column(Text)
    awarding_office_code = Column(Text)
    awarding_office_name = Column(Text)
    awarding_sub_tier_agency_c = Column(Text)
    awarding_sub_tier_agency_n = Column(Text)
    award_modification_amendme = Column(Text)
    business_funds_indicator = Column(Text)
    business_types = Column(Text)
    cfda_number = Column(Text)
    cfda_title = Column(Text)
    correction_late_delete_ind = Column(Text)
    face_value_loan_guarantee = Column(Text)
    fain = Column(Text, index=True)
    federal_action_obligation = Column(Numeric)
    fiscal_year_and_quarter_co = Column(Text)
    funding_agency_code = Column(Text)
    funding_agency_name = Column(Text)
    funding_office_name = Column(Text)
    funding_office_code = Column(Text)
    funding_sub_tier_agency_co = Column(Text)
    funding_sub_tier_agency_na = Column(Text)
    legal_entity_address_line1 = Column(Text)
    legal_entity_address_line2 = Column(Text)
    legal_entity_address_line3 = Column(Text)
    legal_entity_city_code = Column(Text)
    legal_entity_city_name = Column(Text)
    legal_entity_congressional = Column(Text)
    legal_entity_country_code = Column(Text)
    legal_entity_county_code = Column(Text)
    legal_entity_county_name = Column(Text)
    legal_entity_foreign_city = Column(Text)
    legal_entity_foreign_posta = Column(Text)
    legal_entity_foreign_provi = Column(Text)
    legal_entity_state_code = Column(Text)
    legal_entity_state_name = Column(Text)
    legal_entity_zip5 = Column(Text)
    legal_entity_zip_last4 = Column(Text)
    non_federal_funding_amount = Column(Text)
    original_loan_subsidy_cost = Column(Text)
    period_of_performance_curr = Column(Text)
    period_of_performance_star = Column(Text)
    place_of_performance_city = Column(Text)
    place_of_performance_code = Column(Text)
    place_of_performance_congr = Column(Text)
    place_of_perform_country_c = Column(Text)
    place_of_perform_county_na = Column(Text)
    place_of_performance_forei = Column(Text)
    place_of_perform_state_nam = Column(Text)
    place_of_performance_zip4a = Column(Text)
    record_type = Column(Text)
    sai_number = Column(Text)
    total_funding_amount = Column(Text)
    uri = Column(Text, index=True)

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(AwardFinancialAssistance, self).__init__(**clean_kwargs)


class AwardProcurement(Base):
    """Model for D1-Award (Procurement)."""
    __tablename__ = "award_procurement"
    award_procurement_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer,
                           ForeignKey("submission.submission_id", ondelete="CASCADE",
                                      name="fk_award_procurement_submission_id"),
                           nullable=False, index=True)
    submission = relationship("Submission", uselist=False, cascade="delete")
    job_id = Column(Integer, nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    piid = Column(Text)
    awarding_sub_tier_agency_c = Column(Text)
    awarding_sub_tier_agency_n = Column(Text)
    awarding_agency_code = Column(Text)
    awarding_agency_name = Column(Text)
    parent_award_id = Column(Text)
    award_modification_amendme = Column(Text)
    type_of_contract_pricing = Column(Text)
    contract_award_type = Column(Text)
    naics = Column(Text)
    naics_description = Column(Text)
    awardee_or_recipient_uniqu = Column(Text)
    ultimate_parent_legal_enti = Column(Text)
    ultimate_parent_unique_ide = Column(Text)
    award_description = Column(Text)
    place_of_performance_zip4a = Column(Text)
    place_of_perform_city_name = Column(Text)
    place_of_performance_congr = Column(Text)
    awardee_or_recipient_legal = Column(Text)
    legal_entity_city_name = Column(Text)
    legal_entity_state_code = Column(Text)
    legal_entity_state_descrip = Column(Text)
    legal_entity_zip4 = Column(Text)
    legal_entity_congressional = Column(Text)
    legal_entity_address_line1 = Column(Text)
    legal_entity_address_line2 = Column(Text)
    legal_entity_address_line3 = Column(Text)
    legal_entity_country_code = Column(Text)
    legal_entity_country_name = Column(Text)
    period_of_performance_star = Column(Text)
    period_of_performance_curr = Column(Text)
    period_of_perf_potential_e = Column(Text)
    ordering_period_end_date = Column(Text)
    action_date = Column(Text)
    action_type = Column(Text)
    federal_action_obligation = Column(Numeric)
    current_total_value_award = Column(Text)
    potential_total_value_awar = Column(Text)
    funding_sub_tier_agency_co = Column(Text)
    funding_sub_tier_agency_na = Column(Text)
    funding_office_code = Column(Text)
    funding_office_name = Column(Text)
    awarding_office_code = Column(Text)
    awarding_office_name = Column(Text)
    referenced_idv_agency_iden = Column(Text)
    funding_agency_code = Column(Text)
    funding_agency_name = Column(Text)
    place_of_performance_locat = Column(Text)
    place_of_performance_state = Column(Text)
    place_of_perform_country_c = Column(Text)
    idv_type = Column(Text)
    referenced_idv_type = Column(Text)
    vendor_doing_as_business_n = Column(Text)
    vendor_phone_number = Column(Text)
    vendor_fax_number = Column(Text)
    multiple_or_single_award_i = Column(Text)
    referenced_mult_or_single = Column(Text)
    type_of_idc = Column(Text)
    a_76_fair_act_action = Column(Text)
    dod_claimant_program_code = Column(Text)
    clinger_cohen_act_planning = Column(Text)
    commercial_item_acquisitio = Column(Text)
    commercial_item_test_progr = Column(Text)
    consolidated_contract = Column(Text)
    contingency_humanitarian_o = Column(Text)
    contract_bundling = Column(Text)
    contract_financing = Column(Text)
    contracting_officers_deter = Column(Text)
    cost_accounting_standards = Column(Text)
    cost_or_pricing_data = Column(Text)
    country_of_product_or_serv = Column(Text)
    davis_bacon_act = Column(Text)
    evaluated_preference = Column(Text)
    extent_competed = Column(Text)
    fed_biz_opps = Column(Text)
    foreign_funding = Column(Text)
    government_furnished_equip = Column(Text)
    information_technology_com = Column(Text)
    interagency_contracting_au = Column(Text)
    local_area_set_aside = Column(Text)
    major_program = Column(Text)
    purchase_card_as_payment_m = Column(Text)
    multi_year_contract = Column(Text)
    national_interest_action = Column(Text)
    number_of_actions = Column(Text)
    number_of_offers_received = Column(Text)
    other_statutory_authority = Column(Text)
    performance_based_service = Column(Text)
    place_of_manufacture = Column(Text)
    price_evaluation_adjustmen = Column(Text)
    product_or_service_code = Column(Text)
    program_acronym = Column(Text)
    other_than_full_and_open_c = Column(Text)
    recovered_materials_sustai = Column(Text)
    research = Column(Text)
    sea_transportation = Column(Text)
    service_contract_act = Column(Text)
    small_business_competitive = Column(Text)
    solicitation_identifier = Column(Text)
    solicitation_procedures = Column(Text)
    fair_opportunity_limited_s = Column(Text)
    subcontracting_plan = Column(Text)
    program_system_or_equipmen = Column(Text)
    type_set_aside = Column(Text)
    epa_designated_product = Column(Text)
    walsh_healey_act = Column(Text)
    transaction_number = Column(Text)
    sam_exception = Column(Text)
    city_local_government = Column(Text)
    county_local_government = Column(Text)
    inter_municipal_local_gove = Column(Text)
    local_government_owned = Column(Text)
    municipality_local_governm = Column(Text)
    school_district_local_gove = Column(Text)
    township_local_government = Column(Text)
    us_state_government = Column(Text)
    us_federal_government = Column(Text)
    federal_agency = Column(Text)
    federally_funded_research = Column(Text)
    us_tribal_government = Column(Text)
    foreign_government = Column(Text)
    community_developed_corpor = Column(Text)
    labor_surplus_area_firm = Column(Text)
    corporate_entity_not_tax_e = Column(Text)
    corporate_entity_tax_exemp = Column(Text)
    partnership_or_limited_lia = Column(Text)
    sole_proprietorship = Column(Text)
    small_agricultural_coopera = Column(Text)
    international_organization = Column(Text)
    us_government_entity = Column(Text)
    emerging_small_business = Column(Text)
    c8a_program_participant = Column(Text)
    sba_certified_8_a_joint_ve = Column(Text)
    dot_certified_disadvantage = Column(Text)
    self_certified_small_disad = Column(Text)
    historically_underutilized = Column(Text)
    small_disadvantaged_busine = Column(Text)
    the_ability_one_program = Column(Text)
    historically_black_college = Column(Text)
    c1862_land_grant_college = Column(Text)
    c1890_land_grant_college = Column(Text)
    c1994_land_grant_college = Column(Text)
    minority_institution = Column(Text)
    private_university_or_coll = Column(Text)
    school_of_forestry = Column(Text)
    state_controlled_instituti = Column(Text)
    tribal_college = Column(Text)
    veterinary_college = Column(Text)
    educational_institution = Column(Text)
    alaskan_native_servicing_i = Column(Text)
    community_development_corp = Column(Text)
    native_hawaiian_servicing = Column(Text)
    domestic_shelter = Column(Text)
    manufacturer_of_goods = Column(Text)
    hospital_flag = Column(Text)
    veterinary_hospital = Column(Text)
    hispanic_servicing_institu = Column(Text)
    foundation = Column(Text)
    woman_owned_business = Column(Text)
    minority_owned_business = Column(Text)
    women_owned_small_business = Column(Text)
    economically_disadvantaged = Column(Text)
    joint_venture_women_owned = Column(Text)
    joint_venture_economically = Column(Text)
    veteran_owned_business = Column(Text)
    service_disabled_veteran_o = Column(Text)
    contracts = Column(Text)
    grants = Column(Text)
    receives_contracts_and_gra = Column(Text)
    airport_authority = Column(Text)
    council_of_governments = Column(Text)
    housing_authorities_public = Column(Text)
    interstate_entity = Column(Text)
    planning_commission = Column(Text)
    port_authority = Column(Text)
    transit_authority = Column(Text)
    subchapter_s_corporation = Column(Text)
    limited_liability_corporat = Column(Text)
    foreign_owned_and_located = Column(Text)
    american_indian_owned_busi = Column(Text)
    alaskan_native_owned_corpo = Column(Text)
    indian_tribe_federally_rec = Column(Text)
    native_hawaiian_owned_busi = Column(Text)
    tribally_owned_business = Column(Text)
    asian_pacific_american_own = Column(Text)
    black_american_owned_busin = Column(Text)
    hispanic_american_owned_bu = Column(Text)
    native_american_owned_busi = Column(Text)
    subcontinent_asian_asian_i = Column(Text)
    other_minority_owned_busin = Column(Text)
    for_profit_organization = Column(Text)
    nonprofit_organization = Column(Text)
    other_not_for_profit_organ = Column(Text)
    us_local_government = Column(Text)
    referenced_idv_modificatio = Column(Text)
    undefinitized_action = Column(Text)
    domestic_or_foreign_entity = Column(Text)

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(AwardProcurement, self).__init__(**clean_kwargs)


class DetachedAwardProcurement(Base):
    """Model for D1-Award (Procurement)."""
    __tablename__ = "detached_award_procurement"
    detached_award_procurement_id = Column(Integer, primary_key=True)
    piid = Column(Text)
    awarding_sub_tier_agency_c = Column(Text)
    awarding_sub_tier_agency_n = Column(Text)
    awarding_agency_code = Column(Text)
    awarding_agency_name = Column(Text)
    parent_award_id = Column(Text)
    award_modification_amendme = Column(Text)
    type_of_contract_pricing = Column(Text)
    type_of_contract_pric_desc = Column(Text)
    contract_award_type = Column(Text)
    contract_award_type_desc = Column(Text)
    naics = Column(Text)
    naics_description = Column(Text)
    awardee_or_recipient_uniqu = Column(Text)
    ultimate_parent_legal_enti = Column(Text)
    ultimate_parent_unique_ide = Column(Text)
    award_description = Column(Text)
    place_of_performance_zip4a = Column(Text)
    place_of_perform_city_name = Column(Text)
    place_of_perform_county_na = Column(Text)
    place_of_performance_congr = Column(Text)
    awardee_or_recipient_legal = Column(Text)
    legal_entity_city_name = Column(Text)
    legal_entity_state_code = Column(Text)
    legal_entity_state_descrip = Column(Text)
    legal_entity_zip4 = Column(Text)
    legal_entity_congressional = Column(Text)
    legal_entity_address_line1 = Column(Text)
    legal_entity_address_line2 = Column(Text)
    legal_entity_address_line3 = Column(Text)
    legal_entity_country_code = Column(Text)
    legal_entity_country_name = Column(Text)
    period_of_performance_star = Column(Text)
    period_of_performance_curr = Column(Text)
    period_of_perf_potential_e = Column(Text)
    ordering_period_end_date = Column(Text)
    action_date = Column(Text)
    action_type = Column(Text)
    action_type_description = Column(Text)
    federal_action_obligation = Column(Numeric)
    current_total_value_award = Column(Text)
    potential_total_value_awar = Column(Text)
    funding_sub_tier_agency_co = Column(Text)
    funding_sub_tier_agency_na = Column(Text)
    funding_office_code = Column(Text)
    funding_office_name = Column(Text)
    awarding_office_code = Column(Text)
    awarding_office_name = Column(Text)
    referenced_idv_agency_iden = Column(Text)
    referenced_idv_agency_desc = Column(Text)
    funding_agency_code = Column(Text)
    funding_agency_name = Column(Text)
    place_of_performance_locat = Column(Text)
    place_of_performance_state = Column(Text)
    place_of_perfor_state_desc = Column(Text)
    place_of_perform_country_c = Column(Text)
    place_of_perf_country_desc = Column(Text)
    idv_type = Column(Text)
    idv_type_description = Column(Text)
    referenced_idv_type = Column(Text)
    referenced_idv_type_desc = Column(Text)
    vendor_doing_as_business_n = Column(Text)
    vendor_phone_number = Column(Text)
    vendor_fax_number = Column(Text)
    multiple_or_single_award_i = Column(Text)
    multiple_or_single_aw_desc = Column(Text)
    referenced_mult_or_single = Column(Text)
    referenced_mult_or_si_desc = Column(Text)
    type_of_idc = Column(Text)
    type_of_idc_description = Column(Text)
    a_76_fair_act_action = Column(Text)
    a_76_fair_act_action_desc = Column(Text)
    dod_claimant_program_code = Column(Text)
    dod_claimant_prog_cod_desc = Column(Text)
    clinger_cohen_act_planning = Column(Text)
    clinger_cohen_act_pla_desc = Column(Text)
    commercial_item_acquisitio = Column(Text)
    commercial_item_acqui_desc = Column(Text)
    commercial_item_test_progr = Column(Text)
    commercial_item_test_desc = Column(Text)
    consolidated_contract = Column(Text)
    consolidated_contract_desc = Column(Text)
    contingency_humanitarian_o = Column(Text)
    contingency_humanitar_desc = Column(Text)
    contract_bundling = Column(Text)
    contract_bundling_descrip = Column(Text)
    contract_financing = Column(Text)
    contract_financing_descrip = Column(Text)
    contracting_officers_deter = Column(Text)
    contracting_officers_desc = Column(Text)
    cost_accounting_standards = Column(Text)
    cost_accounting_stand_desc = Column(Text)
    cost_or_pricing_data = Column(Text)
    cost_or_pricing_data_desc = Column(Text)
    country_of_product_or_serv = Column(Text)
    country_of_product_or_desc = Column(Text)
    davis_bacon_act = Column(Text)
    davis_bacon_act_descrip = Column(Text)
    evaluated_preference = Column(Text)
    evaluated_preference_desc = Column(Text)
    extent_competed = Column(Text)
    extent_compete_description = Column(Text)
    fed_biz_opps = Column(Text)
    fed_biz_opps_description = Column(Text)
    foreign_funding = Column(Text)
    foreign_funding_desc = Column(Text)
    government_furnished_equip = Column(Text)
    government_furnished_desc = Column(Text)
    information_technology_com = Column(Text)
    information_technolog_desc = Column(Text)
    interagency_contracting_au = Column(Text)
    interagency_contract_desc = Column(Text)
    local_area_set_aside = Column(Text)
    local_area_set_aside_desc = Column(Text)
    major_program = Column(Text)
    purchase_card_as_payment_m = Column(Text)
    purchase_card_as_paym_desc = Column(Text)
    multi_year_contract = Column(Text)
    multi_year_contract_desc = Column(Text)
    national_interest_action = Column(Text)
    national_interest_desc = Column(Text)
    number_of_actions = Column(Text)
    number_of_offers_received = Column(Text)
    other_statutory_authority = Column(Text)
    performance_based_service = Column(Text)
    performance_based_se_desc = Column(Text)
    place_of_manufacture = Column(Text)
    place_of_manufacture_desc = Column(Text)
    price_evaluation_adjustmen = Column(Text)
    product_or_service_code = Column(Text)
    product_or_service_co_desc = Column(Text)
    program_acronym = Column(Text)
    other_than_full_and_open_c = Column(Text)
    other_than_full_and_o_desc = Column(Text)
    recovered_materials_sustai = Column(Text)
    recovered_materials_s_desc = Column(Text)
    research = Column(Text)
    research_description = Column(Text)
    sea_transportation = Column(Text)
    sea_transportation_desc = Column(Text)
    service_contract_act = Column(Text)
    service_contract_act_desc = Column(Text)
    small_business_competitive = Column(Text)
    solicitation_identifier = Column(Text)
    solicitation_procedures = Column(Text)
    solicitation_procedur_desc = Column(Text)
    fair_opportunity_limited_s = Column(Text)
    fair_opportunity_limi_desc = Column(Text)
    subcontracting_plan = Column(Text)
    subcontracting_plan_desc = Column(Text)
    program_system_or_equipmen = Column(Text)
    program_system_or_equ_desc = Column(Text)
    type_set_aside = Column(Text)
    type_set_aside_description = Column(Text)
    epa_designated_product = Column(Text)
    epa_designated_produc_desc = Column(Text)
    walsh_healey_act = Column(Text)
    walsh_healey_act_descrip = Column(Text)
    transaction_number = Column(Text)
    sam_exception = Column(Text)
    sam_exception_description = Column(Text)
    city_local_government = Column(Text)
    county_local_government = Column(Text)
    inter_municipal_local_gove = Column(Text)
    local_government_owned = Column(Text)
    municipality_local_governm = Column(Text)
    school_district_local_gove = Column(Text)
    township_local_government = Column(Text)
    us_state_government = Column(Text)
    us_federal_government = Column(Text)
    federal_agency = Column(Text)
    federally_funded_research = Column(Text)
    us_tribal_government = Column(Text)
    foreign_government = Column(Text)
    community_developed_corpor = Column(Text)
    labor_surplus_area_firm = Column(Text)
    corporate_entity_not_tax_e = Column(Text)
    corporate_entity_tax_exemp = Column(Text)
    partnership_or_limited_lia = Column(Text)
    sole_proprietorship = Column(Text)
    small_agricultural_coopera = Column(Text)
    international_organization = Column(Text)
    us_government_entity = Column(Text)
    emerging_small_business = Column(Text)
    c8a_program_participant = Column(Text)
    sba_certified_8_a_joint_ve = Column(Text)
    dot_certified_disadvantage = Column(Text)
    self_certified_small_disad = Column(Text)
    historically_underutilized = Column(Text)
    small_disadvantaged_busine = Column(Text)
    the_ability_one_program = Column(Text)
    historically_black_college = Column(Text)
    c1862_land_grant_college = Column(Text)
    c1890_land_grant_college = Column(Text)
    c1994_land_grant_college = Column(Text)
    minority_institution = Column(Text)
    private_university_or_coll = Column(Text)
    school_of_forestry = Column(Text)
    state_controlled_instituti = Column(Text)
    tribal_college = Column(Text)
    veterinary_college = Column(Text)
    educational_institution = Column(Text)
    alaskan_native_servicing_i = Column(Text)
    community_development_corp = Column(Text)
    native_hawaiian_servicing = Column(Text)
    domestic_shelter = Column(Text)
    manufacturer_of_goods = Column(Text)
    hospital_flag = Column(Text)
    veterinary_hospital = Column(Text)
    hispanic_servicing_institu = Column(Text)
    foundation = Column(Text)
    woman_owned_business = Column(Text)
    minority_owned_business = Column(Text)
    women_owned_small_business = Column(Text)
    economically_disadvantaged = Column(Text)
    joint_venture_women_owned = Column(Text)
    joint_venture_economically = Column(Text)
    veteran_owned_business = Column(Text)
    service_disabled_veteran_o = Column(Text)
    contracts = Column(Text)
    grants = Column(Text)
    receives_contracts_and_gra = Column(Text)
    airport_authority = Column(Text)
    council_of_governments = Column(Text)
    housing_authorities_public = Column(Text)
    interstate_entity = Column(Text)
    planning_commission = Column(Text)
    port_authority = Column(Text)
    transit_authority = Column(Text)
    subchapter_s_corporation = Column(Text)
    limited_liability_corporat = Column(Text)
    foreign_owned_and_located = Column(Text)
    american_indian_owned_busi = Column(Text)
    alaskan_native_owned_corpo = Column(Text)
    indian_tribe_federally_rec = Column(Text)
    native_hawaiian_owned_busi = Column(Text)
    tribally_owned_business = Column(Text)
    asian_pacific_american_own = Column(Text)
    black_american_owned_busin = Column(Text)
    hispanic_american_owned_bu = Column(Text)
    native_american_owned_busi = Column(Text)
    subcontinent_asian_asian_i = Column(Text)
    other_minority_owned_busin = Column(Text)
    for_profit_organization = Column(Text)
    nonprofit_organization = Column(Text)
    other_not_for_profit_organ = Column(Text)
    us_local_government = Column(Text)
    referenced_idv_modificatio = Column(Text)
    undefinitized_action = Column(Text)
    undefinitized_action_desc = Column(Text)
    domestic_or_foreign_entity = Column(Text)
    domestic_or_foreign_e_desc = Column(Text)
    pulled_from = Column(Text)
    last_modified = Column(Text)

    __table_args__ = (UniqueConstraint('awarding_sub_tier_agency_c', 'piid', 'award_modification_amendme',
                                       'parent_award_id', 'referenced_idv_modificatio', 'transaction_number',
                                       name='uniq_det_award_proc_key'),)

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(DetachedAwardProcurement, self).__init__(**clean_kwargs)


class DetachedAwardFinancialAssistance(Base):
    """Model for D2-Award (Financial Assistance)."""
    __tablename__ = "detached_award_financial_assistance"

    detached_award_financial_assistance_id = Column(Integer, primary_key=True)
    submission_id = Column(Integer,
                           ForeignKey("submission.submission_id", ondelete="CASCADE",
                                      name="fk_detached_award_financial_assistance_submission_id"),
                           nullable=False, index=True)
    submission = relationship("Submission", uselist=False, cascade="delete")
    job_id = Column(Integer, nullable=False, index=True)
    row_number = Column(Integer, nullable=False)
    action_date = Column(Text)
    action_type = Column(Text)
    assistance_type = Column(Text)
    award_description = Column(Text)
    awardee_or_recipient_legal = Column(Text)
    awardee_or_recipient_uniqu = Column(Text)
    awarding_agency_code = Column(Text)
    awarding_office_code = Column(Text)
    awarding_sub_tier_agency_c = Column(Text)
    award_modification_amendme = Column(Text)
    business_funds_indicator = Column(Text)
    business_types = Column(Text)
    cfda_number = Column(Text)
    correction_late_delete_ind = Column(Text)
    face_value_loan_guarantee = Column(Numeric)
    fain = Column(Text, index=True)
    federal_action_obligation = Column(Numeric)
    fiscal_year_and_quarter_co = Column(Text)
    funding_agency_code = Column(Text)
    funding_office_code = Column(Text)
    funding_sub_tier_agency_co = Column(Text)
    legal_entity_address_line1 = Column(Text)
    legal_entity_address_line2 = Column(Text)
    legal_entity_address_line3 = Column(Text)
    legal_entity_congressional = Column(Text)
    legal_entity_country_code = Column(Text)
    legal_entity_foreign_city = Column(Text)
    legal_entity_foreign_posta = Column(Text)
    legal_entity_foreign_provi = Column(Text)
    legal_entity_zip5 = Column(Text)
    legal_entity_zip_last4 = Column(Text)
    non_federal_funding_amount = Column(Numeric)
    original_loan_subsidy_cost = Column(Numeric)
    period_of_performance_curr = Column(Text)
    period_of_performance_star = Column(Text)
    place_of_performance_code = Column(Text)
    place_of_performance_congr = Column(Text)
    place_of_perform_country_c = Column(Text)
    place_of_performance_forei = Column(Text)
    place_of_performance_zip4a = Column(Text)
    record_type = Column(Integer)
    sai_number = Column(Text)
    uri = Column(Text, index=True)
    is_valid = Column(Boolean, nullable=False, default="False", server_default="False")

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(DetachedAwardFinancialAssistance, self).__init__(**clean_kwargs)


class PublishedAwardFinancialAssistance(Base):
    """Model for D2-Award (Financial Assistance)."""
    __tablename__ = "published_award_financial_assistance"

    published_award_financial_assistance_id = Column(Integer, primary_key=True)
    action_date = Column(Text)
    action_type = Column(Text)
    assistance_type = Column(Text)
    award_description = Column(Text)
    awardee_or_recipient_legal = Column(Text)
    awardee_or_recipient_uniqu = Column(Text)
    awarding_agency_code = Column(Text)
    awarding_office_code = Column(Text)
    awarding_sub_tier_agency_c = Column(Text, index=True)
    award_modification_amendme = Column(Text, index=True)
    business_funds_indicator = Column(Text)
    business_types = Column(Text)
    cfda_number = Column(Text)
    correction_late_delete_ind = Column(Text)
    face_value_loan_guarantee = Column(Numeric)
    fain = Column(Text, index=True)
    federal_action_obligation = Column(Numeric)
    fiscal_year_and_quarter_co = Column(Text)
    funding_agency_code = Column(Text)
    funding_office_code = Column(Text)
    funding_sub_tier_agency_co = Column(Text)
    legal_entity_address_line1 = Column(Text)
    legal_entity_address_line2 = Column(Text)
    legal_entity_address_line3 = Column(Text)
    legal_entity_congressional = Column(Text)
    legal_entity_country_code = Column(Text)
    legal_entity_foreign_city = Column(Text)
    legal_entity_foreign_posta = Column(Text)
    legal_entity_foreign_provi = Column(Text)
    legal_entity_zip5 = Column(Text)
    legal_entity_zip_last4 = Column(Text)
    non_federal_funding_amount = Column(Numeric)
    original_loan_subsidy_cost = Column(Numeric)
    period_of_performance_curr = Column(Text)
    period_of_performance_star = Column(Text)
    place_of_performance_code = Column(Text)
    place_of_performance_congr = Column(Text)
    place_of_perform_country_c = Column(Text)
    place_of_performance_forei = Column(Text)
    place_of_performance_zip4a = Column(Text)
    record_type = Column(Integer)
    sai_number = Column(Text)
    total_funding_amount = Column(Text)
    uri = Column(Text, index=True)

    __table_args__ = (UniqueConstraint('awarding_sub_tier_agency_c', 'award_modification_amendme', 'fain', 'uri',
                                       name='uniq_award_mod_sub_tier_fain_uri'),)

    def __init__(self, **kwargs):
        # broker is set up to ignore extra columns in submitted data
        # so get rid of any extraneous kwargs before instantiating
        clean_kwargs = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super(PublishedAwardFinancialAssistance, self).__init__(**clean_kwargs)
