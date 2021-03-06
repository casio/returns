from typing import Callable, TypeVar, overload

from returns.context import (
    RequiresContext,
    RequiresContextIOResult,
    RequiresContextResult,
)
from returns.future import Future, FutureResult
from returns.io import IO, IOResult
from returns.maybe import Maybe
from returns.result import Result

_ValueType = TypeVar('_ValueType')
_ErrorType = TypeVar('_ErrorType')
_NewValueType = TypeVar('_NewValueType')
_EnvType = TypeVar('_EnvType')


# Apply:

@overload
def _apply(
    container: Maybe[Callable[[_ValueType], _NewValueType]],
) -> Callable[[Maybe[_ValueType]], Maybe[_NewValueType]]:
    ...


@overload
def _apply(
    container: IO[Callable[[_ValueType], _NewValueType]],
) -> Callable[[IO[_ValueType]], IO[_NewValueType]]:
    ...


@overload
def _apply(
    container: RequiresContext[_EnvType, Callable[[_ValueType], _NewValueType]],
) -> Callable[
    [RequiresContext[_EnvType, _ValueType]],
    RequiresContext[_EnvType, _NewValueType],
]:
    ...


@overload
def _apply(
    container: RequiresContextResult[
        _EnvType,
        Callable[[_ValueType], _NewValueType],
        _ErrorType,
    ],
) -> Callable[
    [RequiresContextResult[_EnvType, _ValueType, _ErrorType]],
    RequiresContextResult[_EnvType, _NewValueType, _ErrorType],
]:
    ...


@overload
def _apply(
    container: RequiresContextIOResult[
        _EnvType,
        Callable[[_ValueType], _NewValueType],
        _ErrorType,
    ],
) -> Callable[
    [RequiresContextIOResult[_EnvType, _ValueType, _ErrorType]],
    RequiresContextIOResult[_EnvType, _NewValueType, _ErrorType],
]:
    ...


@overload
def _apply(
    container: Result[
        Callable[[_ValueType], _NewValueType],
        _ErrorType,
    ],
) -> Callable[
    [Result[_ValueType, _ErrorType]],
    Result[_NewValueType, _ErrorType],
]:
    ...


@overload
def _apply(
    container: IOResult[
        Callable[[_ValueType], _NewValueType],
        _ErrorType,
    ],
) -> Callable[
    [IOResult[_ValueType, _ErrorType]],
    IOResult[_NewValueType, _ErrorType],
]:
    ...


@overload
def _apply(
    container: Future[Callable[[_ValueType], _NewValueType]],
) -> Callable[
    [Future[_ValueType]],
    Future[_NewValueType],
]:
    ...


@overload
def _apply(
    container: FutureResult[
        Callable[[_ValueType], _NewValueType],
        _ErrorType,
    ],
) -> Callable[
    [FutureResult[_ValueType, _ErrorType]],
    FutureResult[_NewValueType, _ErrorType],
]:
    ...


# Apply by:

@overload
def _apply_by(
    container: Maybe[_ValueType],
) -> Callable[
    [Maybe[Callable[[_ValueType], _NewValueType]]],
    Maybe[_NewValueType],
]:
    ...


@overload
def _apply_by(
    container: IO[_ValueType],
) -> Callable[
    [IO[Callable[[_ValueType], _NewValueType]]],
    IO[_NewValueType],
]:
    ...


@overload
def _apply_by(
    container: RequiresContext[_EnvType, _ValueType],
) -> Callable[
    [RequiresContext[_EnvType, Callable[[_ValueType], _NewValueType]]],
    RequiresContext[_EnvType, _NewValueType],
]:
    ...


@overload
def _apply_by(
    container: RequiresContextResult[
        _EnvType,
        _ValueType,
        _ErrorType,
    ],
) -> Callable[
    [
        RequiresContextResult[
            _EnvType,
            Callable[[_ValueType], _NewValueType],
            _ErrorType,
        ],
    ],
    RequiresContextResult[_EnvType, _NewValueType, _ErrorType],
]:
    ...


@overload
def _apply_by(
    container: RequiresContextIOResult[
        _EnvType,
        _ValueType,
        _ErrorType,
    ],
) -> Callable[
    [
        RequiresContextIOResult[
            _EnvType,
            Callable[[_ValueType], _NewValueType],
            _ErrorType,
        ],
    ],
    RequiresContextIOResult[_EnvType, _NewValueType, _ErrorType],
]:
    ...


@overload
def _apply_by(
    container: Result[_ValueType, _ErrorType],
) -> Callable[
    [Result[Callable[[_ValueType], _NewValueType], _ErrorType]],
    Result[_NewValueType, _ErrorType],
]:
    ...


@overload
def _apply_by(
    container: IOResult[_ValueType, _ErrorType],
) -> Callable[
    [IOResult[Callable[[_ValueType], _NewValueType], _ErrorType]],
    IOResult[_NewValueType, _ErrorType],
]:
    ...


@overload
def _apply_by(
    container: Future[_ValueType],
) -> Callable[
    [Future[Callable[[_ValueType], _NewValueType]]],
    Future[_NewValueType],
]:
    ...


@overload
def _apply_by(
    container: FutureResult[_ValueType, _ErrorType],
) -> Callable[
    [FutureResult[Callable[[_ValueType], _NewValueType], _ErrorType]],
    FutureResult[_NewValueType, _ErrorType],
]:
    ...
