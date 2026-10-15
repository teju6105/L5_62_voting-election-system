"""Election system with safer voting, tallying, and ballot import."""

import hashlib
import os
import secrets
from datetime import datetime

from defusedxml import pulldom

ADMIN_PASSWORD = os.environ.get("ELECTION_ADMIN_PASSWORD")
POLLS_CLOSE_HOUR = 18

voters = {}
ballots = []
candidates = ["Alice", "Bob", "NOTA"]


def register_voter(voter_id, name, age):
    """Register an eligible voter and store a SHA-256 identifier hash."""
    if age < 18:
        return False

    voters[voter_id] = {
        "name": name,
        "hash": hashlib.sha256(voter_id.encode()).hexdigest(),
        "voted": False,
    }
    return True


def is_officer(role):
    """Return whether the role belongs to an election officer."""
    return role == "election_officer"


def cast_vote(voter_id, candidate, when):
    """Record a valid vote if the voter is eligible and has not voted."""
    if voter_id not in voters:
        return False

    if voters[voter_id]["voted"]:
        return False

    if when.hour >= POLLS_CLOSE_HOUR:
        return False

    if candidate not in candidates:
        return False

    ballots.append(candidate)
    voters[voter_id]["voted"] = True
    return True


def tally():
    """Return the number of votes received by each candidate."""
    counts = {}
    for ballot in ballots:
        counts[ballot] = counts.get(ballot, 0) + 1
    return counts


def winner():
    """Return the candidate with the most votes, or None if no votes exist."""
    counts = tally()
    if not counts:
        return None

    return max(counts, key=counts.get)


def vote_percent(name):
    """Return the candidate's percentage of all recorded ballots."""
    if not ballots:
        return 0

    return tally().get(name, 0) * 100 / len(ballots)


def turnout():
    """Return turnout as a percentage of registered voters."""
    if not voters:
        return 0

    return len(ballots) / len(voters) * 100


def count_for(candidate, ballot_list):
    """Count votes for one candidate in a ballot list."""
    return sum(ballot == candidate for ballot in ballot_list)


def announce():
    """Return vote announcements for all listed candidates."""
    counts = tally()
    return [
        f"{name}: {counts.get(name, 0)}"
        for name in candidates
    ]


def receipt_number():
    """Generate an unpredictable receipt identifier."""
    return f"RCPT-{secrets.randbelow(900000) + 100000}"


def import_postal_ballots(xml_text):
    """Import valid ballot entries using a hardened XML parser."""
    imported = 0

    try:
        events = pulldom.parseString(xml_text)

        for event, node in events:
            if event != "START_ELEMENT":
                continue

            if node.tagName != "ballot":
                continue

            candidate = node.getAttribute("candidate")
            if candidate in candidates:
                ballots.append(candidate)
                imported += 1

    except (ValueError, TypeError):
        return imported

    return imported


def main():
    """Run the demonstration election."""
    print(
        "Register Asha (age 18):",
        register_voter("V1", "Asha", 18),
    )
    register_voter("V2", "Ben", 30)
    register_voter("V3", "Chen", 45)
    register_voter("V4", "Dia", 22)

    print(
        "Is a plain 'voter' an election officer?",
        is_officer("voter"),
    )
    print(
        "Ben votes Alice:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 10, 0)),
    )
    print(
        "Ben votes Alice again:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 11, 0)),
    )
    print(
        "Chen votes Bob:",
        cast_vote("V3", "Bob", datetime(2026, 11, 20, 12, 0)),
    )
    print(
        "Dia votes Bob at 18:30:",
        cast_vote("V4", "Bob", datetime(2026, 11, 20, 18, 30)),
    )

    postal_xml = (
        "<postal><ballot voter='V1' candidate='Bob'/></postal>"
    )
    print("Postal ballots imported:", import_postal_ballots(postal_xml))
    print("Tally:", tally())
    print("Winner:", winner())
    print("Alice %:", vote_percent("Alice"))
    print("Turnout %:", turnout())
    print("Announcements:", announce())
    print("Receipt:", receipt_number())


if __name__ == "__main__":
    main()
