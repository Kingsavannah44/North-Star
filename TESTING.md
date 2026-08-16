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
- **Feature being tested:** Stock Availability
- **Test steps:** Ask whether a known product and size are currently in stock.
- **Expected result:** The system should return the correct stock availability for the requested product and size using the available inventory data.
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


- Corrected features will be retested before final submission.
## Backend/API Testing Results

Backend testing was performed using the FastAPI Swagger interface at `http://localhost:8000/docs` against the available seeded mock data.

### Test Case 1: Valid Order Status Request
- **Test input:** Order `NS1001`
- **Actual result:** The API successfully returned the order information for NS1001.
- **Status:** PASS
- **Issues identified:** None.

### Test Case 2: Shipped Order With Tracking Information
- **Test input:** Order `NS1001`
- **Actual result:** The API returned the order as Shipped with tracking number `TRK98231` and estimated delivery date `2026-08-16`.
- **Status:** PASS
- **Issues identified:** None.

### Test Case 3: Shipped Order Without Tracking Number
- **Actual result:** No seeded order exists with status Shipped and `tracking_number=None`.
- **Status:** BLOCKED / NOT TESTABLE
- **Issues identified:** Required test data is not available in the seeded dataset.

### Test Case 4: Unknown Order Reference
- **Test input:** Order `NS9999`
- **Actual result:** The API returned a 404 response with `ORDER_NOT_FOUND` rather than inventing order information.
- **Status:** PASS
- **Issues identified:** None.

### Test Case 5: Return Request Within 30-Day Window
- **Actual result:** The return request was not handled as a returns flow and fell back to the support/unknown response.
- **Status:** FAIL
- **Issues identified:** Returns functionality was not available through the tested backend support flow.

### Test Case 6: Return Request Outside 30-Day Window
- **Actual result:** The required sample order delivered 55 days ago was not available in the provided mock data.
- **Status:** BLOCKED / NOT TESTABLE
- **Issues identified:** Required test data is missing.

### Test Case 7: Refund Status Request
- **Actual result:** No refund-in-progress data was available in the provided mock dataset.
- **Status:** BLOCKED / NOT TESTABLE
- **Issues identified:** Required refund test data is missing.

### Test Case 8: Natural-Language Returns or Refunds Query
- **Actual result:** The natural-language returns/refund request was not correctly recognized as a returns/refunds request.
- **Status:** FAIL
- **Issues identified:** Returns/refunds intent classification did not behave as expected.

### Test Case 9: Stock Availability Query
- **Actual result:** Stock availability was correctly returned from the seeded inventory. Nike Air Max size 42 was available with quantity 8, while size 43 was unavailable with quantity 0.
- **Status:** PASS
- **Issues identified:** None.

### Test Case 10: Unsupported or Unclear Support Query
- **Test input:** Unsupported password-related support query.
- **Actual result:** The query was classified as unknown and returned the support fallback instead of inventing an answer.
- **Status:** PASS
- **Issues identified:** None.

### Backend Testing Summary
- **Passed:** 5
- **Failed:** 2
- **Blocked / Not Testable:** 3

## End-to-End Chatbot Testing Results

End-to-end testing was performed using the Northstar Support Bot frontend at `http://localhost:8000/` while the FastAPI backend was running. These tests verified the complete flow from the user interface to the backend and back to the displayed chatbot response.

### Test Case 1: Valid Order Status Request
- **Test input:** `Where is my order NS1001?`
- **Actual result:** The chatbot classified the request as `ORDER STATUS` and reported that order NS1001 had shipped with tracking number `TRK98231` and expected arrival date `2026-08-16`.
- **Status:** PASS
- **Issues identified:** None.

### Test Case 2: Shipped Order With Tracking Information
- **Test input:** `Where is my order NS1005?`
- **Actual result:** The chatbot classified the request as `ORDER STATUS` and reported that NS1005 had shipped with tracking number `TRK44512` and expected arrival date `2026-08-18`.
- **Status:** PASS
- **Issues identified:** None.

### Test Case 3: Shipped Order Without Tracking Number
- **Actual result:** No shipped order without a tracking number exists in the seeded test data. All seeded shipped orders contain tracking numbers.
- **Status:** BLOCKED / NOT TESTABLE
- **Issues identified:** Required test data is missing.

### Test Case 4: Unknown Order Reference
- **Test input:** `Where is my order NS9999?`
- **Actual result:** The chatbot classified the request as `ORDER STATUS` and responded that order NS9999 could not be found. It advised the user to double-check the number or contact Northstar Support.
- **Status:** PASS
- **Issues identified:** None. The chatbot did not invent order information.

### Test Case 5: Return Request Within 30-Day Window
- **Test input:** `How do I return order NS1003?`
- **Actual result:** The chatbot classified the request as `UNKNOWN` and responded that it could not find an automated answer and that the user should contact Northstar Support.
- **Status:** FAIL
- **Issues identified:** The chatbot did not recognize or process the return request as a Returns and Refunds query.

### Test Case 6: Return Request Outside 30-Day Window
- **Actual result:** The required sample order delivered 55 days ago was not available in the provided mock data.
- **Status:** BLOCKED / NOT TESTABLE
- **Issues identified:** Required test data is missing.

### Test Case 7: Refund Status Request
- **Actual result:** No refund-in-progress test data was available in the provided mock dataset.
- **Status:** BLOCKED / NOT TESTABLE
- **Issues identified:** Required refund test data is missing.

### Test Case 8: Natural-Language Returns or Refunds Query
- **Test input:** `How do I send this back?`
- **Actual result:** The chatbot classified the request as `UNKNOWN` and directed the user to Northstar Support.
- **Status:** FAIL
- **Issues identified:** Natural-language return intent was not recognized by the chatbot.

### Test Case 9: Stock Availability Query
- **Test input:** `Is Nike Air Max size 43 available?`
- **Actual result:** The chatbot classified the request as `STOCK AVAILABILITY` and correctly reported that Nike Air Max size 43 was out of stock. This matched the seeded inventory quantity of `0`.
- **Status:** PASS
- **Issues identified:** None.

### Test Case 10: Unsupported or Unclear Support Query
- **Test input:** `Can I change my account password?`
- **Actual result:** The chatbot classified the query as `UNKNOWN` and directed the user to Northstar Support instead of inventing an answer.
- **Status:** PASS
- **Issues identified:** None.

### End-to-End Testing Summary
- **Passed:** 5
- **Failed:** 2
- **Blocked / Not Testable:** 3
- **Total planned test cases:** 10
