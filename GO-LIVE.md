# Go-Live Readiness Note

Northstar Support Deflection MVP
North-Star team, 15 August 2026

## 1. What works

**Order status**
Give the bot an order number and it returns the current status, the ship date, the tracking number where one exists, and the estimated delivery date. Works for every order in the seeded data.

**Returns and refunds**
Answers how to return an item, whether an order is still inside the return window, and where an existing refund has got to.

**Stock availability**
Answers whether a product is currently in stock.

**Human handoff**
Anything outside those three areas is passed to a human with a ticket reference rather than guessed at. The bot does not invent answers.

**How it runs**
One command starts the whole thing - `python start.py` - which serves both the chat page and the API on port 8000. No separate frontend server needed.

**What's behind it**
A FastAPI backend with SQLAlchemy models for customers, orders, products and inventory. Seeded with 10 customers, 15 orders, 10 products and 35 inventory rows. 20 automated tests covering the three endpoints, plus 10 written manual test cases covering normal use, edge cases and the handoff.

## 2. What is known-broken or limited

**The data is not real.** Everything runs off a seed script with made-up orders. There is no connection to any real order system.

**It runs locally only.** Nothing is hosted. Whoever wants to use it has to run it on their own machine.

**The bot has no memory.** Each question is answered on its own. It does not remember what you asked a moment ago, so follow-up questions have to repeat the order number.

**No accounts or login.** Anyone who opens the page can look up any order number. There is no check that the person asking is the person who placed the order.

**Handoff is a message, not a ticket.** When the bot passes a question to a human it returns a reference number, but nothing is actually created in a support system. A person would have to pick it up manually.

**Database setup.** The application expects database configuration in a `.env` file. Without it the app will not start.

## 3. What Northstar needs to run this without us

**Connect real order data.** Replace the seed script with a connection to the live order system. The database models are already shaped for customers, orders, products and inventory, so the structure is there.

**Wire the handoff into the real ticketing tool.** At the moment the bot returns a reference number. That should create an actual support ticket so nothing gets lost.

**Host it.** It needs to run somewhere permanent rather than on a laptop, and the chat page needs to sit on the Northstar website.

**Add identity checks** before real customers use it, so people can only see their own orders.

**A person to own the answers.** The wording the bot gives for returns and refunds reflects a 30-day policy. If that policy changes, someone has to update it.

## What we would build next

1. Conversation memory, so customers do not have to repeat the order number
2. A record of which questions get handed off, so Northstar can see what to automate next
3. Better handling of questions phrased in unusual ways

## A note on the timeline

This was built over three days rather than the five in the brief. We handled that by keeping the scope narrow and finishing what we started rather than half-building more. All three ticket types work end to end. The limits above are deliberate decisions about what to leave out, not things we ran out of time for and hoped nobody would notice.
