# Team Charter

North-Star. Group formed Tue 11 Aug, chatted Tue and Wed to get organised.
Kickoff meeting Thu 13 Aug 11am, charter agreed there.
Deadline Sat 15th 11:59pm. Aiming to submit 6pm so we're not panicking at midnight.

## Team

- Ibrahim - team lead / PM
- Brian - backend
- Ursula - frontend
- Eric - QA
- Batula - documentation

## Who touches what

Don't edit someone else's files, that's how we get conflicts.

- Ibrahim: CHARTER.md, SCOPE.md, standup/, audit/
- Brian: app/, seed.py
- Ursula: static/
- Eric: tests/, TESTING.md
- Batula: README.md, GO-LIVE.md, demo script

## How we work

- Team meeting Thu 11am was the kickoff. Saturday we meet again at 11am before final delivery.
- In between we check in over WhatsApp during the day, no fixed standup time.
- Commit something every day Thu/Fri/Sat. Doesn't have to be big. We're marked on the history so an empty day can't be fixed later.
- Move your board card the same day you do the work, not all at once at the end.

## Git

- Work on your own branch, then merge into main before you finish for the day. If it's not on main it doesn't count.
- No force pushing to main. We lost work twice this week doing that.
- Conflict? Don't force it, send it to me.
- No PR reviews, no time for that.

## Commit messages

`type: what changed - why it matters`

types: feat, fix, docs, test, chore

good: `feat: add order status lookup - lets customers check without opening a ticket`
not ok: wip, update, changes, final

## Done means

Committed to main, board card moved the same day, and the "done" sentence on the card is actually true. If the done sentence needs an "and" plus a "but" the task is too big, split it.

## If someone goes quiet

Agreed now so it's not awkward later.

- Day 1 - I message you privately. Not a telling off, just checking you're not stuck.
- Day 2 - raised in the group, task gets split or reassigned. You keep a smaller bit so you can come back in.
- Day 2 also - we tell the facilitator. Not on Saturday.

Nobody gets kicked out for going quiet. We just can't find out about it on Saturday morning.

## Arguments

10 mins. If still stuck, whoever owns that area decides, writes one line in the repo saying what and why, and we move on.

## Plan

- Thu: kickoff meeting, repo, charter, scope, backend started, test plan
- Fri: build day. Backend finished, QA writes test cases.
- Fri night: no new features after this, only fixes
- Sat 11am: standup, then integration, testing, go-live note
- Sat 4pm: demo run-through, under 3 mins
- Sat 6pm: submit

## Peer ratings

Saturday, done individually, confidential. We don't show each other what we wrote.

## Agreed by

Ibrahim, Brian, Ursula, Eric, Batula
