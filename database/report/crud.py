from database.base_crud import BaseCRUD
from database.report.model import Report
from database.core import db_report


class ReportCRUD(BaseCRUD):
    model = Report
    db = db_report
    schema = 'public'
