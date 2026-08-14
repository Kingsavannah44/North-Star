Team Charter
North-Star sprint. Agreed Thu 13 Aug. Deadline Sat 15 Aug 11:59pm. We submit 6pm Sat so we're not rushing at midnight.
ibrahim (ibrahim.warsame - Team Lead
Brian (Kingsavannah44) - backend. Seed data, order lookup, intent router, order status flow.
Ursula (MACCUE) - frontend. Chat UI, returns/refunds flow, handoff display.
Eric (Emyrseric) - QA. Test cases, running tests, results log.
Batula - README, go-live note, demo script.

Who owns which files
Nobody edits someone else's files. This is what stops merge conflicts.

CHARTER.md, SCOPE.md, standup/, audit/ - Ibrahim
data/, app/ - Brian
ui/ - Ursula
tests/, TESTING.md - Eric
README.md, GO-LIVE.md, demo-script.md -batula  documentation
Rules
Everyone commits at least once a day, Thu/Fri/Sat. Small commits are fine. An empty day can't be fixed later, the timestamps are what we're marked on.
Standup 11am(sat). Three lines each: what I did, what I'm doing, what's blocking me.
Move your board card the same day you do the work. Not all at once on Saturday.
Answer direct questions within 2 hrs during the day.
Git
Work on your own branch: feat/name-thing
Merge into main before you stop for the day. If it's not on main it's not in our history.
No force pushing to main. Protection is on.
Conflict? Don't force it, bring it to Ibrahim.

Commit messages
Format: type: what changed - why it matters

Types: feat, fix, docs, test, refactor, chore

Good: feat: add order status lookup - lets customers check without opening a ticket Not allowed: wip, update, changes, final
Done means
Committed and merged to main
Board card moved same day
The card's "done" sentence is actually true

If the "done" sentence needs an "and" plus a "but", the task is too big. Split it.
If someone goes quiet
Agreed now so it isn't awkward later.

Day 1 no activity - Ibrahim messages you privately. Not a telling off, just checking if you're stuck.
Day 2 - raised in the group, task gets reassigned or cut down. You keep a smaller piece so you can rejoin.
Day 2 same day - we tell the facilitator. Not on Saturday.

Nobody gets kicked out for going quiet. We just can't find out about it on Saturday morning.
Plan
Thu: repo, charter, scope, seed data, UI shell, test cases, README
Fri am: lock the stack, build router + order status
Fri pm: returns flow, handoff, QA full test pass by 6pm
Fri 6pm: FEATURE FREEZE. Nothing new after this, only fixes.
Sat am: fix, retest, go-live note
Sat 2pm: demo rehearsal, under 3 mins
Sat 6pm: submit
Peer ratings
Done individually on Saturday, confidential. We don't share what we wrote about each other.
Signed
Ibrahim Warsame
Brian Kipkemoi
Ursula Immaculate
Eric Kamau
Batula Abdullahi
