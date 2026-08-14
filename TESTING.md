# MVP Testing Plan

## Purpose
The purpose of this testing plan is to verify that the North-Star Support Deflection MVP works according to the agreed project scope and provides clear and useful responses to users.

## Testing Responsibilities
As the QA tester, I will:
- Test the completed MVP features against the agreed scope.
- Test both normal cases and edge cases.
- Check whether each feature produces the expected result.
- Identify functional errors, bugs, and usability issues.
- Record the expected and actual results of each test.
- Report failed tests and identified issues to the team.
- Retest corrected features before final submission.

## Features to Test
According to the project scope, the MVP will be tested in the following areas:
- Order Status
- Returns and Refunds
- Human handoff for unsupported queries such as Stock Availability

The MVP uses mock order data rather than a real production database.

## Test Cases

### Test Case 1: Valid Order Status Request
- **Feature being tested:** Order Status
- **Test steps:** Ask for the status of a valid order using an order reference from the provided mock order data.
- **Expected result:** The system should return the correct order status and relevant order information.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 2: Shipped Order With Tracking Information
- **Feature being tested:** Order Status
- **Test steps:** Ask for the status of a shipped order that has a tracking number.
- **Expected result:** The system should return the order status, shipping information, tracking number, and estimated delivery information where available.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 3: Shipped Order Without Tracking Number
- **Feature being tested:** Order Status
- **Test steps:** Ask for the status of the sample shipped order that does not have a tracking number.
- **Expected result:** The system should correctly report that the order has shipped without inventing a tracking number.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 4: Unknown Order Reference
- **Feature being tested:** Order Status
- **Test steps:** Ask for the status of an order using an order reference that does not exist in the mock order data.
- **Expected result:** The system should not invent order information and should provide an appropriate response or clarification.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 5: Return Request Within 30-Day Window
- **Feature being tested:** Returns and Refunds
- **Test steps:** Ask how to return an order that is still within the 30-day return window.
- **Expected result:** The system should identify that the order is eligible for return and provide the appropriate return steps.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 6: Return Request Outside 30-Day Window
- **Feature being tested:** Returns and Refunds
- **Test steps:** Ask to return the sample order that was delivered 55 days ago.
- **Expected result:** The system should identify that the order is outside the 30-day return window and should not incorrectly approve the return.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 7: Refund Status Request
- **Feature being tested:** Returns and Refunds
- **Test steps:** Ask for the refund status of an order where a refund is already in progress.
- **Expected result:** The system should return the available refund status accurately.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 8: Natural-Language Returns or Refunds Query
- **Feature being tested:** Returns and Refunds
- **Test steps:** Ask a returns or refunds question using normal conversational wording, such as "How do I send this back?" or "When will I get my money back?"
- **Expected result:** The system should correctly recognize the user's intent and provide the appropriate returns or refund response.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 9: Stock Availability Query
- **Feature being tested:** Human Handoff
- **Test steps:** Ask whether a product is currently in stock.
- **Expected result:** The system should not guess or provide an unsupported stock answer. The query should be handed off to a human with a ticket reference.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 10: Unsupported or Unclear Support Query
- **Feature being tested:** Human Handoff
- **Test steps:** Ask a support question that does not clearly belong to either the Order Status or Returns and Refunds flow.
- **Expected result:** The system should avoid giving an incorrect answer and should route the query to a human instead.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

## Final Testing
Before final submission, the completed MVP will be tested end-to-end using the available mock order data.

For each test case:
- The actual result will be recorded.
- The test will be marked Pass or Fail.
- Any bugs or unexpected behaviour will be documented.
- Failed tests will be reported to the appropriate team member.
- Corrected features will be retested before final submission.
