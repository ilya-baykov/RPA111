from database.base_crud import BaseCRUD
from database.report.model import Candidate
from database.core import db_candidates


class CandidateCRUD(BaseCRUD):
    model = Candidate
    db = db_candidates
    schema = 'communication_candidates'
