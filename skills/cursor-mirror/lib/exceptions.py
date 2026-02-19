# Exceptions for cursor-mirror. Import and catch these when using as library.

class CursorMirrorError(Exception):
    """Base exception for cursor-mirror errors."""
    pass

class NotFoundError(CursorMirrorError):
    """Entity not found (workspace, composer, etc.)."""
    pass

class DatabaseError(CursorMirrorError):
    """Database access or query error."""
    pass

class ValidationError(CursorMirrorError):
    """Invalid input or argument."""
    pass
