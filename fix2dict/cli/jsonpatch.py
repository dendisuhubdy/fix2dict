import json
import jsonpatch
import click

from fix2dict.cli import cli
from fix2dict.cli.utils.json import read_json, DEFAULT_INDENT
from fix2dict.patch import apply_patch


@cli.command("jsonpatch")
@click.argument("src", nargs=1, type=click.Path(exists=True))
@click.argument("path-to-patch", nargs=1, type=click.Path(exists=True))
def patch(src, path_to_patch):
    """
    Apply a JSON Patch file.
    """
    patch = jsonpatch.JsonPatch(read_json(path_to_patch))
    data = apply_patch(read_json(src), patch)
    print(json.dumps(data, indent=DEFAULT_INDENT))
