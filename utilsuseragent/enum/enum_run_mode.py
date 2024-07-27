from enum import Enum


class EnumRunMode(Enum, str):
    SYNC = "SYNC"
    ASYNC = "ASYNC"
