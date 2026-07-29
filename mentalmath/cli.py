"""Command line entry point."""

from __future__ import annotations

import argparse

from . import session as session_mod
from . import stats
from .generator import CATEGORIES


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mental-math",
        description="Timed arithmetic drill with per-category tracking.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    drill = sub.add_parser("drill", help="run a timed session")
    drill.add_argument("-n", "--count", type=int, default=80)
    drill.add_argument("-t", "--seconds", type=int, default=480)
    drill.add_argument("--seed", type=int, default=None)
    drill.add_argument(
        "-c",
        "--category",
        action="append",
        choices=CATEGORIES,
        help="restrict to one or more categories (repeatable)",
    )
    drill.add_argument("--no-save", action="store_true")

    sub.add_parser("progress", help="show all recorded sessions")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "progress":
        print(stats.progress(session_mod.load_sessions()))
        return 0

    result = session_mod.run(
        count=args.count,
        limit_seconds=args.seconds,
        seed=args.seed,
        categories=args.category,
    )
    print(stats.summarize(result))
    if not args.no_save and result.attempts:
        path = result.save()
        print(f"\nsaved {path.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
