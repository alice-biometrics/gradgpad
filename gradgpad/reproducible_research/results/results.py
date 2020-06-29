import os

from gradgpad.tools.open_result_json import open_result_json

REPRODUCIBLE_RESEARCH_RESULTS_DIR = os.path.abspath(os.path.dirname(__file__))


quality_results = open_result_json(
    f"{REPRODUCIBLE_RESEARCH_RESULTS_DIR}/quality_results.json"
)
quality_linear_results = open_result_json(
    f"{REPRODUCIBLE_RESEARCH_RESULTS_DIR}/quality_linear_results.json"
)

quality_results_gender = {k: v for k, v in quality_results.items() if "Gender" in k}
quality_linear_results_gender = {
    k: v for k, v in quality_linear_results.items() if "Gender" in k
}

quality_results_skin_tone = {
    k: v for k, v in quality_results.items() if "Skin Tone" in k
}
quality_linear_results_skin_tone = {
    k: v for k, v in quality_linear_results.items() if "Skin Tone" in k
}

quality_results_age = {k: v for k, v in quality_results.items() if "Age" in k}
quality_linear_results_age = {
    k: v for k, v in quality_linear_results.items() if "Age" in k
}