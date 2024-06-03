from fastapi import HTTPException, status


USERALREADYEXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exists",
)

INCORRECTDATA = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Incorrect data",
)

INCORRECTCREDENTIALS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect email or password",
)

EXPIREDACCESS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Access token expired",
)

ACCESSDENIED = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Access denied",
)

TOKENINVALID = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
)

ROOMCANNOTBEBOOKED = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Not enough rooms",
)