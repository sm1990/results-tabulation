from config import db, ma
from models import Election, TallySheet, TallySheetVersion, TallySheet_PRE_41, TallySheet_PRE_41__party, Invoice, \
    InvoiceItem, Invoice_InvoiceItem

from marshmallow import Schema, fields, validates_schema, ValidationError


class ElectionSchema(ma.ModelSchema):
    class Meta:
        model = Election
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session


class TallySheetVersionSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "tallySheetId",
            "code",
            "electionId",
            "officeId",
            "latestVersionId",

            "tallySheetVersionId",
            "createdBy",
            "createdAt"
        )

        model = TallySheetVersion
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session


class TallySheetSchema(ma.ModelSchema):
    class Meta:
        model = TallySheet
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session

    latestVersion = ma.Nested(TallySheetVersionSchema)


class TallySheet_PRE_41__party_Schema(ma.ModelSchema):
    class Meta:
        fields = ("partyId", "voteCount")

        model = TallySheet_PRE_41__party
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session


class TallySheet_PRE_41_Schema(ma.ModelSchema):
    class Meta:
        fields = (
            "tallySheetId",
            "code",
            "electionId",
            "officeId",
            "latestVersionId",

            "tallySheetVersionId",
            "createdBy",
            "createdAt",

            "electoralDistrictId",
            "pollingDivisionId",
            "countingCentreId",
            "party_wise_results",
        )

        model = TallySheet_PRE_41
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session

    createdBy = ma.Integer()
    createdAt = ma.String()

    party_wise_results = ma.Nested(TallySheet_PRE_41__party_Schema, many=True)


class InvoiceItem_Schema(ma.ModelSchema):
    class Meta:
        fields = (
            "invoiceId",
            "invoiceItemType"
        )

        model = Invoice
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session


class Invoice_InvoiceItem_Schema(ma.ModelSchema):
    class Meta:
        fields = (
            "invoiceId",
            "invoiceItemId",
            "receivedBy",
            "receivedFrom",
            "receivedAt"
        )

        model = Invoice_InvoiceItem
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session


class Invoice_Schema(ma.ModelSchema):
    class Meta:
        fields = (
            "invoiceId",
            "electionId",
            "issuingOfficeId",
            "receivingOfficeId",
            "issuedBy",
            "issuedTo",
            "issuedAt",
            "invoiceItems"
        )

        model = Invoice
        # optionally attach a Session
        # to use for deserialization
        sqla_session = db.session

    invoiceItems = ma.Nested(Invoice_InvoiceItem_Schema, many=True)
