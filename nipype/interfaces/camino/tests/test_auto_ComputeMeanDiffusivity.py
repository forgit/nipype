# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.dti import ComputeMeanDiffusivity

def test_ComputeMeanDiffusivity_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='< %s',
    mandatory=True,
    position=1,
    ),
    inputdatatype=dict(argstr='-inputdatatype %s',
    ),
    inputmodel=dict(argstr='-inputmodel %s',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    outputdatatype=dict(argstr='-outputdatatype %s',
    ),
    scheme_file=dict(argstr='%s',
    position=2,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = ComputeMeanDiffusivity.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ComputeMeanDiffusivity_outputs():
    output_map = dict(md=dict(),
    )
    outputs = ComputeMeanDiffusivity.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

