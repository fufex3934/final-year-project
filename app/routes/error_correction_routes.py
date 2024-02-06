from flask import jsonify, Blueprint, request
from app.error_correction.error_correction import ErrorCorrection
from app.knowledge_base.knowledge_base import KnowledgeBase
from app.morphological_analyzer.morphological_analyzer import MorphologicalAnalyzer

error_correction_routes = Blueprint('error_correction_routes', __name__)

@error_correction_routes.route('/correct_errors', methods=['POST'])
def correct_errors():
    data = request.get_json()
    errors = data.get('errors', [])
    print(f"Errors from error detection: {errors}")
    kb = KnowledgeBase('app/knowledge_base/resources/dictionary.dic', 'app/knowledge_base/resources/dictionary.aff')
    ma = MorphologicalAnalyzer(kb)
    error_correction = ErrorCorrection(kb, ma)
   

    corrections = []
    for error in errors:
        correction = error_correction.correct_error(error) 
        #
        corrections.append(correction)
        print(f"Corrections word: {corrections}")

    return jsonify({'corrections': corrections})