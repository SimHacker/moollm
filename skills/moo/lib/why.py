# --why: caller-provided reason for invoking. Moo does not answer "why";
# use standard Python CLI help (moo --help, moo read --help) for command docs.
# This module exists so callers (person, LLM, script) can pass a reason string;
# moo accepts it (args.why) for traceability / passing to an executor. No output.
