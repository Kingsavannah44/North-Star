from fastapi import HTTPException


class AppError(HTTPException):
    def __init__(self, status_code: int, code: str, message: str):
        super().__init__(status_code=status_code, detail={"code": code, "message": message})


class OrderNotFoundError(AppError):
    def __init__(self, order_number: str):
        super().__init__(
            status_code=404,
            code="ORDER_NOT_FOUND",
            message=f"Order {order_number} was not found.",
        )


class ProductNotFoundError(AppError):
    def __init__(self, product_id: int):
        super().__init__(
            status_code=404,
            code="PRODUCT_NOT_FOUND",
            message=f"Product with ID {product_id} was not found.",
        )


class SizeNotFoundError(AppError):
    def __init__(self, size: str, product_name: str):
        super().__init__(
            status_code=404,
            code="SIZE_NOT_FOUND",
            message=f'Size "{size}" is not available for product "{product_name}".',
        )
