"""Scoring and progress analysis.

The number that matters is not accuracy alone and not speed alone. Under a hard
clock the binding metric is correct answers per minute, because a slow perfect
run and a fast sloppy run both fail.
"""

from __future__ import annotations

from statistics import median

from .generator import CATEGORIES
from .session import Session


def rate_per_minute(session: Session) -> float:
    if session.elapsed_seconds <= 0:
        return 0.0
    return session.correct / (session.elapsed_seconds / 60)


def projected_score(session: Session) -> float:
    """Correct answers if the observed rate held for the full time limit."""
    return rate_per_minute(session) * (session.limit_seconds / 60)


def by_category(session: Session) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for category in CATEGORIES:
        rows = [a for a in session.attempts if a.category == category]
        if not rows:
            continue
        out[category] = {
            "attempted": len(rows),
            "accuracy": sum(1 for a in rows if a.correct) / len(rows),
            "median_seconds": median(a.seconds for a in rows),
        }
    return out


def summarize(session: Session) -> str:
    lines = [
        "",
        f"attempted     {len(session.attempts)}/{session.question_count}",
        f"correct       {session.correct}",
        f"accuracy      {session.accuracy:.0%}",
        f"elapsed       {session.elapsed_seconds:.0f}s of {session.limit_seconds}s",
        f"rate          {rate_per_minute(session):.1f} correct/min",
        f"projected     {projected_score(session):.0f} at the full time limit",
        "",
        f"{'category':<10} {'n':>4} {'acc':>6} {'median':>8}",
    ]
    for category, row in sorted(
        by_category(session).items(), key=lambda kv: -kv[1]["median_seconds"]
    ):
        lines.append(
            f"{category:<10} {row['attempted']:>4.0f} "
            f"{row['accuracy']:>5.0%} {row['median_seconds']:>7.1f}s"
        )

    wrong = [a for a in session.attempts if not a.correct]
    if wrong:
        lines.append("")
        lines.append(f"missed ({len(wrong)}):")
        for a in wrong[:12]:
            given = a.given or "-"
            lines.append(f"  {a.prompt} = {a.expected}   you: {given}")
        if len(wrong) > 12:
            lines.append(f"  ... and {len(wrong) - 12} more")
    return "\n".join(lines)


def progress(sessions: list[Session]) -> str:
    """One line per session, oldest first, so the trend is visible at a glance."""
    if not sessions:
        return "No sessions recorded yet."
    lines = [f"{'date':<12} {'n':>4} {'acc':>6} {'rate':>7} {'proj':>6}"]
    for s in sessions:
        lines.append(
            f"{s.started_at[:10]:<12} {len(s.attempts):>4} "
            f"{s.accuracy:>5.0%} {rate_per_minute(s):>6.1f} "
            f"{projected_score(s):>6.0f}"
        )
    slowest = _weakest_category(sessions)
    if slowest:
        lines.append("")
        lines.append(f"slowest category across all sessions: {slowest}")
    return "\n".join(lines)


def _weakest_category(sessions: list[Session]) -> str | None:
    pooled: dict[str, list[float]] = {}
    for s in sessions:
        for a in s.attempts:
            pooled.setdefault(a.category, []).append(a.seconds)
    if not pooled:
        return None
    category, times = max(pooled.items(), key=lambda kv: median(kv[1]))
    return f"{category} ({median(times):.1f}s median, n={len(times)})"
