import os

import pytest

from gradgpad import (
    Approach,
    CombinedScenario,
    PadRadarPaiPlotter,
    Protocol,
    ResultsProvider,
    WorkingPoint,
)

APPROACH_RESULTS = {
    "Quality SVM RBF": ResultsProvider.get(
        Approach.QUALITY_RBF, protocol=Protocol.GRANDTEST
    ),
    "Auxiliary": ResultsProvider.get(Approach.AUXILIARY, protocol=Protocol.GRANDTEST),
}


@pytest.mark.unit
@pytest.mark.parametrize(
    "working_point,approach_results",
    [
        (WorkingPoint.BPCER_5, APPROACH_RESULTS),
        (WorkingPoint.BPCER_10, APPROACH_RESULTS),
    ],
)
def test_should_save_a_pad_radar_pai_plotter(working_point, approach_results):
    os.makedirs("output", exist_ok=True)
    output_filename = "output/radar.png"
    radar = PadRadarPaiPlotter(
        title="My Title",
        working_point=working_point,
        combined_scenario=CombinedScenario.PAS_I_AND_II,
    )
    radar.save(output_filename=output_filename, results=approach_results)

    assert os.path.isfile(output_filename)
