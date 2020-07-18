from gradgpad.metrics.eer import eer
from gradgpad.metrics.indepth_error_rates_analysis import indepth_error_rates_analysis
from gradgpad.reproducible_research import Scores, List
from gradgpad.reproducible_research.scores.subset import Subset


def meta_label_info_provider(specific: bool = True):
    if specific:
        meta_label_info = {
            "print_low_quality": [1],
            "print_medium_quality": [2],
            "print_high_quality": [3],
            "replay_low_quality": [4],
            "replay_medium_quality": [5],
            "replay_high_quality": [6],
            "mask_paper": [7],
            "mask_rigid": [8],
            "mask_silicone": [9],
            "makeup_cosmetic": [10],
            "makeup_impersonation": [11],
            "makeup_obfuscation": [12],
            "partial_funny_eyes": [13],
            "partial_periocular": [14],
            "partial_paper_glasses": [15],
            "partial_upper_half": [16],
            "partial_lower_half": [17],
        }
    else:
        meta_label_info = {
            "print": [1, 2, 3],
            "replay": [4, 5, 6],
            "mask": [7, 8, 9],
            "makeup": [10, 11, 12],
            "partial": [13, 14, 15, 16, 17],
        }

    return meta_label_info


class Metrics:
    def __init__(self, devel_scores: Scores, test_scores: Scores):
        self.devel_scores = devel_scores
        self.test_scores = test_scores

    def get_eer(self, subset: Subset):
        scores = self.devel_scores if subset == Subset.DEVEL else self.test_scores
        eer_value, _ = eer(scores.get_numpy_scores(), scores.get_numpy_labels())
        return eer_value

    def get_indeepth_analysis(
        self,
        bpcer_fixing_working_points: List[float],
        apcer_fixing_working_points: List[float],
    ):
        _, eer_th = eer(
            self.devel_scores.get_numpy_scores(), self.devel_scores.get_numpy_labels()
        )

        analysis = {
            "specific"
            if specific
            else "aggregate": indepth_error_rates_analysis(
                self.test_scores.get_numpy_scores(),
                self.test_scores.get_numpy_specific_pai_labels(),
                {"eer": eer_th},
                meta_label_info_provider(specific),
                bpcer_fixing_working_points,
                apcer_fixing_working_points,
            )["eer"].to_dict(label_modificator="pai")
            for specific in [True, False]
        }

        return analysis