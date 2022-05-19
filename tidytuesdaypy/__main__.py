import argparse
import logging
import os
import sys
from pathlib import Path

from gooey import Gooey, GooeyParser
from rich.logging import RichHandler

log = logging.getLogger(__name__)

_TEMPLATES_PATH = Path(__file__).parent / "templates"
TEMPLATES_CHOICES = {t.stem: t for t in _TEMPLATES_PATH.glob("*.ipynb")}

if len(sys.argv) >= 2 and "--ignore-gooey" not in sys.argv:
    sys.argv.append("--ignore-gooey")


@Gooey(
    program_name="TidyTuesday",
    optional_cols=1,
    required_cols=1,
    tabbed_groups=True,
    )
def parse_args():
    cwd = os.getcwd()

    parser = GooeyParser(description="TidyTuesday")
    parser.add_argument(
        "dest-folder",
        type=Path,
        help="Destination folder",
        widget="DirChooser",
        default=cwd,
        gooey_options={
            "wildcard": "All files (*.*)|*.*",
            "message": "Pick a folder for the TidyTuesday",
            "default_path": cwd,
        },
    )
    parser.add_argument(
        "template",
        choices=TEMPLATES_CHOICES.keys(),
        help="ipynb Template to use",
        default=list(TEMPLATES_CHOICES.keys())[0],
    )
    parser.add_argument(
        "--verbose",
        type=int,
        help="Verbosity (0=CRITICAL, 1=ERROR, 2=WARN, 3=WARN, 4=DEBUG)",
        default=4,
        dest="verbosity",
        widget="IntegerField",
    )
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        level="WARN",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )

    args = parse_args()
    log.setLevel(max(5 - args.verbosity, 1) * 10)

    log.info("Starting tidytuesdaypy")
