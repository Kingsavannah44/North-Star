# Mid-sprint audit - Fri 14 Aug

## Who's in the history

All five of us committed today. This morning main showed one author because everyone else's work was either unmerged or removed by force pushes. Fixed over Friday evening.

- Brian - backend, seed data, tests, static mount, start command
- Ursula - frontend code
- Eric - testing plan, 10 test cases, stock availability update
- Batula - README overview, go-live note attempted
- Ibrahim - charter, scope, standups, this audit, board

## Force pushes

Two force pushes to main removed other people's commits.

Thu 13 Aug - removed the testing plan and the first chat UI. Restored the same evening. Asked for branch protection.

Fri 14 Aug - removed the PM documents. Restored on a branch so a repeat can't delete them.

Writing these down rather than quietly fixing them. Protection was asked for twice; the second one happened because it wasn't turned on after the first.

## Rules check

- Commit format - mostly met. A couple of exceptions, one contributor commit and one auto-generated merge message. Not rewriting history to fix cosmetics.
- Tasks under 4 hrs with a checkable done sentence - met, 26 cards on the board.
- Board same-day - partly. Board was created Friday so Thursday and most of Friday were backfilled rather than tracked live.
- Escalate within 2 days - met. Batula chased Thursday night, frontend chased Friday evening.
- No standup Friday. Charter says we check in daily and we didn't.

## Risks going into Saturday

1. Frontend and backend aren't connected yet. Until they are we have two halves and no demo.
2. Test results not recorded, all 10 still Pending.
3. App needs MySQL to start. SQLite fallback requested so the demo doesn't depend on database setup.
4. Go-live note doesn't exist yet after the first attempt was removed.

## Actions

- Integration to happen before the meeting, not during it
- Branch protection requested again
- No new features from tonight
- Submitting Saturday evening with buffer, not at midnight
