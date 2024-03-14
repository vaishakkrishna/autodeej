from __future__ import print_function
import msaf


def detect_sections(song_filename:str):
    # 1. Select audio file
    # song_filename = "../datasets/Sargon/audio/01-Sargon-Mindless.mp3"

    # 2. Segment the file using the default MSAF parameters (this might take a few seconds)
    boundaries, labels = msaf.process(song_filename)
    print('Estimated boundaries:', boundaries)

    # 3. Save segments using the MIREX format
    out_file = 'segments.txt'
    print('Saving output to %s' % out_file)
    msaf.io.write_mirex(boundaries, labels, out_file)

    # 4. Evaluate the results
    evals = None
    try:
        evals = msaf.eval.process(song_filename)
        print(evals)
    except msaf.exceptions.NoReferencesError:
        file_struct = msaf.input_output.FileStruct(song_filename)
        print("No references found in {}. No evaluation performed.".format(
            file_struct.ref_file))
    return boundaries
    