# Fri 14 Aug

No standup today, we went straight into building. Coordinated over WhatsApp.

## Done today

- Brian - full backend. Models, services and routes for all three flows, seed data, 20 pytest tests. Added the static folder and start.py so the whole thing runs from one command. Also invited me onto the repo.
- Ursula - frontend code added to the static folder.
- Eric - testing plan merged to main, 10 test cases with expected results, updated the stock case after we changed the scope.
- Batula - README overview. First attempt at GO-LIVE.md had errors so we removed it, redoing it properly tomorrow.
- Ibrahim - charter, scope, Thursday standup notes, task board with 26 cards updated

## Decided

- Stock availability is in scope now. Brian built all three flows with tests so we kept the working code instead of deleting it. Brief only asks for two minimum.
- Asked Brian for a SQLite fallback so the app runs without installing MySQL - Eric can't test otherwise and the demo shouldn't depend on a database being set up on whatever laptop we present from.
- No new features from tonight. Tomorrow is connect, test, document, submit.
- Meeting moved to Saturday. Integration to be done before then, not in the meeting.

## Problems

- Frontend and backend still aren't talking to each other. That's tomorrow's biggest job and the one that can eat the whole day.
- Main got force pushed again and my PM files came off. Second time this week. Restored on a branch.
- Test results still say Pending, Eric needs the backend running first.
- Didn't do a standup today.
## Tomorrow

Ursula and Brian connect the page to the API before 5pm. Eric runs the full test pass. Batula redoes the go-live note using Eric's results. 5pm we meet, demo, do reflections and peer ratings, submit by 9pm.
