#
# PySNMP MIB module CTRON-TIMED-RESET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-TIMED-RESET-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:42:11 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, iso, TimeTicks, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ModuleIdentity, Gauge32, IpAddress, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "iso", "TimeTicks", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ModuleIdentity", "Gauge32", "IpAddress", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctTimedResetMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2))
ctTimedResetStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("softEnabled", 1), ("hardEnabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetStatus.setStatus('deprecated')
if mibBuilder.loadTexts: ctTimedResetStatus.setDescription('softEnabled(1) - soft reset in ctTimedResetTimeEntered seconds.\n           hardEnabled(2) - hard reset in ctTimedResetTimeEntered seconds.\n\n           A zero value in ctTimedResetTimeEntered will cause an immediate\n           reset.\n\n           Setting this to disabled(0) will cause any currently enabled \n           timed reset will be disabled.')
ctTimedResetTimeEntered = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetTimeEntered.setStatus('deprecated')
if mibBuilder.loadTexts: ctTimedResetTimeEntered.setDescription('The time, in seconds, from the time ctTimedResetStatus \n           is set to softEnabled(1) or hardEnabled(2), until the \n           board will reset.')
ctTimedResetTimeRemaining = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTimedResetTimeRemaining.setStatus('deprecated')
if mibBuilder.loadTexts: ctTimedResetTimeRemaining.setDescription('The time, in seconds, remaining until a reset will occur.\n           The time is not meaningful if ctTimedResetStatus is\n           disabled(0).')
ctTimedResetOperationalMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("currentMode", 0), ("ieee8021Q", 1), ("secureFast", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetOperationalMode.setStatus('deprecated')
if mibBuilder.loadTexts: ctTimedResetOperationalMode.setDescription('The operational mode to run in when a timed reset occurs. \n           When set to currentMode(0), the operational mode will remain \n           unchanged.  When set to ieee8021Q(1), the operational mode\n           will be 802.1Q Switching.  When set to secureFast(2),\n           the operational mode will be Secure Fast VLAN.')
ctTimedResetNVRamReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dontResetNVRam", 0), ("resetNVRam", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTimedResetNVRamReset.setStatus('deprecated')
if mibBuilder.loadTexts: ctTimedResetNVRamReset.setDescription('dontResetNVRam(0) - NVRAM will not be cleared on timed reset.\n          resetNVRam(1)     - NVRAM will be cleared on timed reset.')
mibBuilder.exportSymbols("CTRON-TIMED-RESET-MIB", ctTimedResetMIB=ctTimedResetMIB, ctTimedResetOperationalMode=ctTimedResetOperationalMode, ctTimedResetNVRamReset=ctTimedResetNVRamReset, ctTimedResetStatus=ctTimedResetStatus, ctTimedResetTimeRemaining=ctTimedResetTimeRemaining, ctTimedResetTimeEntered=ctTimedResetTimeEntered)
