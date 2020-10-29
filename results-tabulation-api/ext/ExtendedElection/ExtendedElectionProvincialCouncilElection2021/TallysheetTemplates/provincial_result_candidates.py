from orm.entities import Template
from ext.ExtendedElection.ExtendedElectionProvincialCouncilElection2021.TALLY_SHEET_CODES import PCE_CE_RO_PR_2, \
    PROVINCIAL_RESULT_CANDIDATES, PCE_R2
from constants.TALLY_SHEET_COLUMN_SOURCE import TALLY_SHEET_COLUMN_SOURCE_META as SOURCE_META, \
    TALLY_SHEET_COLUMN_SOURCE_CONTENT as SOURCE_CONTENT, TALLY_SHEET_COLUMN_SOURCE_QUERY as SOURCE_QUERY
from ext.ExtendedElection.ExtendedElectionProvincialCouncilElection2021.TEMPLATE_ROW_TYPE import \
    TEMPLATE_ROW_TYPE_SEATS_ALLOCATED, TEMPLATE_ROW_TYPE_ELECTED_CANDIDATE, TEMPLATE_ROW_TYPE_DRAFT_ELECTED_CANDIDATE


def create_template():
    return Template.create(
        templateName=PROVINCIAL_RESULT_CANDIDATES,
        templateRowTypesMap={
            "CANDIDATE_FIRST_PREFERENCE": {
                "hasMany": True,
                "isDerived": True,
                "columns": [
                    {"columnName": "electionId", "grouped": True, "func": None, "source": SOURCE_QUERY},
                    {"columnName": "areaId", "grouped": True, "func": None, "source": SOURCE_QUERY},
                    {"columnName": "partyId", "grouped": True, "func": None, "source": SOURCE_QUERY},
                    {"columnName": "candidateId", "grouped": True, "func": None, "source": SOURCE_QUERY},
                    {"columnName": "numValue", "grouped": False, "func": "sum", "source": SOURCE_QUERY}
                ],
                "derivativeRows": [
                    {"templateName": PCE_CE_RO_PR_2, "templateRowType": "CANDIDATE_FIRST_PREFERENCE"}
                ]
            },
            TEMPLATE_ROW_TYPE_SEATS_ALLOCATED: {
                "hasMany": True,
                "isDerived": True,
                "columns": [
                    {"columnName": "electionId", "grouped": True, "func": None, "source": SOURCE_META},
                    {"columnName": "areaId", "grouped": True, "func": None, "source": SOURCE_META},
                    {"columnName": "partyId", "grouped": True, "func": None, "source": SOURCE_QUERY},
                    {"columnName": "numValue", "grouped": False, "func": "sum", "source": SOURCE_QUERY}
                ],
                "derivativeRows": [
                    {"templateName": PCE_R2, "templateRowType": TEMPLATE_ROW_TYPE_SEATS_ALLOCATED}
                ]
            },
            TEMPLATE_ROW_TYPE_ELECTED_CANDIDATE: {
                "hasMany": True,
                "isDerived": False,
                "columns": [
                    {"columnName": "electionId", "grouped": True, "func": None, "source": SOURCE_META},
                    {"columnName": "areaId", "grouped": True, "func": None, "source": SOURCE_META},
                    {"columnName": "partyId", "grouped": True, "func": None, "source": SOURCE_CONTENT},
                    {"columnName": "candidateId", "grouped": True, "func": None, "source": SOURCE_CONTENT}
                ]
            },
            TEMPLATE_ROW_TYPE_DRAFT_ELECTED_CANDIDATE: {
                "hasMany": True,
                "isDerived": False,
                "columns": [
                    {"columnName": "electionId", "grouped": True, "func": None, "source": SOURCE_META},
                    {"columnName": "areaId", "grouped": True, "func": None, "source": SOURCE_META},
                    {"columnName": "partyId", "grouped": True, "func": None, "source": SOURCE_CONTENT},
                    {"columnName": "candidateId", "grouped": True, "func": None, "source": SOURCE_CONTENT}
                ]
            }
        }
    )
