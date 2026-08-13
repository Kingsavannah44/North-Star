# MVP Testing Plan

## Purpose
The purpose of this testing plan is to verify that the North-Star Support Deflection MVP works as expected and provides a clear and usable experience for users.

## Testing Responsibilities
As the tester, I will:
- Test the features developed by the frontend and backend team members.
- Check whether each feature works as expected.
- Identify errors, bugs, or usability issues.
- Record the expected and actual results of each test.
- Report identified issues to the team for correction.
- Retest corrected features before final submission.

## Features to Test
The MVP will be tested in the following areas:
- Order Status
- Stock Availability
- Support Query Clarification, including Returns and Refunds

## Test Cases

### Test Case 1: Valid Order Status Request
- **Feature being tested:** Order Status
- **Test steps:** Submit a valid order-status query with a valid order reference.
- **Expected result:** The system should return the correct status of the order.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 2: Invalid Order Reference
- **Feature being tested:** Order Status
- **Test steps:** Submit an order-status request using an invalid or unknown order reference.
- **Expected result:** The system should inform the user that the order cannot be found and provide clear guidance.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 3: Missing Order Information
- **Feature being tested:** Order Status
- **Test steps:** Ask for an order status without providing the required order reference.
- **Expected result:** The system should request the missing order information instead of failing.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 4: Clear Order Status Response
- **Feature being tested:** Order Status
- **Test steps:** Submit a valid order-status query and review the response displayed to the user.
- **Expected result:** The response should clearly communicate the current order status in an understandable format.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 5: Product in Stock
- **Feature being tested:** Stock Availability
- **Test steps:** Ask whether an available product is currently in stock.
- **Expected result:** The system should correctly confirm that the product is available.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 6: Product Out of Stock
- **Feature being tested:** Stock Availability
- **Test steps:** Ask about a product that is currently unavailable.
- **Expected result:** The system should clearly indicate that the product is out of stock.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 7: Unclear Stock Query
- **Feature being tested:** Stock Availability
- **Test steps:** Submit a stock query without enough information to identify the product.
- **Expected result:** The system should ask the user for clarification or additional product details.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 8: Return Query
- **Feature being tested:** Support Query Clarification
- **Test steps:** Ask how to return a purchased item.
- **Expected result:** The system should recognize the request as a return-related query and provide or direct the user to relevant return information.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 9: Refund Query
- **Feature being tested:** Support Query Clarification
- **Test steps:** Ask when a refund will be received.
- **Expected result:** The system should recognize the request as a refund-related query and provide the appropriate refund information or guidance.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

### Test Case 10: Ambiguous Support Query
- **Feature being tested:** Support Query Clarification
- **Test steps:** Submit an unclear support message that does not clearly indicate whether the user is asking about an order, stock, return, or refund.
- **Expected result:** The system should ask an appropriate clarification question instead of giving an unrelated answer.
- **Actual result:** To be completed during testing.
- **Status:** Pending
- **Issues identified:** To be completed during testing.

## Final Testing
Before final submission, the completed MVP will be tested end-to-end. Each pending test case will be updated with the actual result, Pass/Fail status, and any identified issues. Failed tests will be reported to the development team and retested after correction.
