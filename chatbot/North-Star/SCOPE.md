Scope
Decided Thu 13 Aug. Delivery Sat 15 Aug 6pm.
Problem
Northstar Retail's support team answers the same three questions all day: order status, returns/refunds, stock availability. Every one of those is a ticket a person has to open and answer manually.
What we're building
A chatbot that answers two of the three without a human, so the ticket never gets opened.
In scope
Order status - "where is my order", "has it shipped" Gives back status, ship date, tracking number if there is one, and estimated delivery.

Returns and refunds - "how do I return this", "when do I get my refund" Checks the 30 day window, gives the return steps, and gives refund status if a refund is already running.
Out of scope
Stock availability. Not building it. It needs inventory data the other two flows don't use, and with 3 days we'd rather have two flows that fully work than three that half work. Stock questions get passed to a human with a ticket reference so they don't get a wrong answer.

Also not building:

login / accounts
real payments or refunds
a real database (orders come from a mock JSON file)
hosting or deployment, it runs locally
chat history between sessions
Data
12 fake orders in seed-orders.json. Covers every status, plus 2 deliberately awkward ones:

one shipped but the courier gave us no tracking number
one delivered 55 days ago, so outside the 30 day return window

Those two exist so we test against real mess, not just the happy path.
Done means
Someone can ask about either of the two flows, in their own words, and get a correct useful answer with no human involved. Anything else reaches a human instead of getting a wrong answer.
Changes
Scope frozen Thu 13 Aug 7:30pm. Feature freeze Fri 6pm. Anything suggested after that goes in GO-LIVE.md as a next step, we don't build it.
