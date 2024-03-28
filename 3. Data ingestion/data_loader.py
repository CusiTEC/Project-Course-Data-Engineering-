from mage_ai.io.file import FileIO
import pandas as pd 
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    month_start=1
    month_end=12
    data_frames = []
    for month in range(month_start, month_end + 1):
        filepath = f'data_afiliados_2023{month:02d}.csv' 
        data_frames.append(FileIO().load(filepath))
    return pd.concat(data_frames, ignore_index=True)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'