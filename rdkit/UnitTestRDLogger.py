from   contextlib import redirect_stderr
import io
from   rdkit import Chem, RDLogger

with io.StringIO() as buf, redirect_stderr(buf), RDLogger.log_level('warn'):
    Chem.MolFromSmiles('BrBrBr')
    output = buf.getvalue()
assert len(output)

with io.StringIO() as buf, redirect_stderr(buf), RDLogger.log_level('crit'):
    Chem.MolFromSmiles('BrBrBr')
    output = buf.getvalue()
assert not len(output)
