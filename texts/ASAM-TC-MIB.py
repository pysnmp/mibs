#
# PySNMP MIB module ASAM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ASAM-TC-MIB
# Source digest sha256:cdf613ad984b12f4ae2f9d8692344606ec9938b3a4979f7c3cf01ffe0f3bea2a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
asam, = mibBuilder.importSymbols("SYSTEM-MIB", "asam")
class AsamProfileIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class AsamProfileIndexOrZero(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AsamNextProfileIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AsamMaxProfileIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AsamProfilePointer(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AsamProfileName(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class AsamProfileScope(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("localScope", 1), ("networkScope", 2))

class AsamProfileRefCount(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AsamProfileRefCount32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class LogLastEntry(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class LogReset(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("resetCompleted", 1), ("reset", 2))

class LogBufferSize(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class LogFullAction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("wrap", 1), ("halt", 2))

class LogOverflowed(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("notoverflowed", 1), ("overflowed", 2))

class LogIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Uint32(Gauge32):
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NetworkTimeInSeconds(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class NetworkTimeInMiliSeconds(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("ASAM-TC-MIB", AsamMaxProfileIndex=AsamMaxProfileIndex, AsamNextProfileIndex=AsamNextProfileIndex, AsamProfileIndex=AsamProfileIndex, AsamProfileIndexOrZero=AsamProfileIndexOrZero, AsamProfileName=AsamProfileName, AsamProfilePointer=AsamProfilePointer, AsamProfileRefCount32=AsamProfileRefCount32, AsamProfileRefCount=AsamProfileRefCount, AsamProfileScope=AsamProfileScope, LogBufferSize=LogBufferSize, LogFullAction=LogFullAction, LogIndex=LogIndex, LogLastEntry=LogLastEntry, LogOverflowed=LogOverflowed, LogReset=LogReset, NetworkTimeInMiliSeconds=NetworkTimeInMiliSeconds, NetworkTimeInSeconds=NetworkTimeInSeconds, Uint32=Uint32)
