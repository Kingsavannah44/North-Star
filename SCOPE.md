# Scope

Decided Thu 13 Aug. Delivery Sat 15 Aug 6pm.

## The problem

Northstar Retail's support team answers the same three questions all day: where's my order, how do I return this, is this in stock. Every one of those is a ticket someone has to open and answer by hand.

## What we're building

A chatbot that answers those questions without a human, so the ticket never gets opened.

## In scope

**Order status** - "where is my order", "has it shipped"
Returns the status, ship date, tracking number if there is one, and estimated delivery.

**Returns and refunds** - "how do I return this", "when do I get my refund"
Checks the 30 day window, gives the return steps, and gives refund status if a refund is already running.

**Stock availability** - "is this in stock"
Added Fri 14 Aug. Was originally out of scope, but Brian built it with tests so we kept the working code rather than delete it. The brief asks for a minimum of two flows.

## Not building

- login or accounts
- real payments or refunds
- hosting, it runs locally
- chat history between sessions

Anything the bot can't answer gets passed to a human with a ticket reference instead of guessing.

## Data

Mock data seeded from seed.py - customers, orders, products, inventory. Includes deliberately awkward cases like an order with no tracking number and one delivered outside the return window, so we're testing against real mess and not just the happy path.

## Done means

Someone can ask about any of the three flows in their own words and get a correct useful answer with no human involved. Anything else reaches a human rather than getting a wrong answer.

## Changes

Scope frozen Thu 13 Aug evening. Feature freeze Fri 6pm. Anything suggested after that goes in GO-LIVE.md as a next step, we don't build it.
