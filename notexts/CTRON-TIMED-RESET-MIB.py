#
# PySNMP MIB module CTRON-TIMED-RESET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-TIMED-RESET-MIB
# Produced by pysmi-1.1.12 at Wed May 29 10:05:14 2024
# On host fv-az775-27 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, Unsigned32, IpAddress, Integer32, ModuleIdentity, MibIdentifier, Counter64, Gauge32, iso, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Unsigned32", "IpAddress", "Integer32", "ModuleIdentity", "MibIdentifier", "Counter64", "Gauge32", "iso", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
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
mibBuilder.exportSymbols("CTRON-TIMED-RESET-MIB", ctTimedResetTimeEntered=ctTimedResetTimeEntered, ctTimedResetMIB=ctTimedResetMIB, ctTimedResetOperationalMode=ctTimedResetOperationalMode, ctTimedResetTimeRemaining=ctTimedResetTimeRemaining, ctTimedResetStatus=ctTimedResetStatus, ctTimedResetNVRamReset=ctTimedResetNVRamReset)
