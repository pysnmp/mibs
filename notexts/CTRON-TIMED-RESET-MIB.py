#
# PySNMP MIB module CTRON-TIMED-RESET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-TIMED-RESET-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 16:42:30 2024
# On host fv-az1437-189 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, TimeTicks, iso, Counter64, ModuleIdentity, Integer32, ObjectIdentity, Unsigned32, IpAddress, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "Counter64", "ModuleIdentity", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctTimedResetMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2))
ctTimedResetStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("softEnabled", 1), ("hardEnabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetStatus.setStatus('deprecated')
ctTimedResetTimeEntered = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetTimeEntered.setStatus('deprecated')
ctTimedResetTimeRemaining = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTimedResetTimeRemaining.setStatus('deprecated')
ctTimedResetOperationalMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("currentMode", 0), ("ieee8021Q", 1), ("secureFast", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetOperationalMode.setStatus('deprecated')
ctTimedResetNVRamReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dontResetNVRam", 0), ("resetNVRam", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetNVRamReset.setStatus('deprecated')
mibBuilder.exportSymbols("CTRON-TIMED-RESET-MIB", ctTimedResetTimeEntered=ctTimedResetTimeEntered, ctTimedResetNVRamReset=ctTimedResetNVRamReset, ctTimedResetTimeRemaining=ctTimedResetTimeRemaining, ctTimedResetStatus=ctTimedResetStatus, ctTimedResetOperationalMode=ctTimedResetOperationalMode, ctTimedResetMIB=ctTimedResetMIB)
