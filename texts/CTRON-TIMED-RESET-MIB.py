#
# PySNMP MIB module CTRON-TIMED-RESET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-TIMED-RESET-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 13:31:48 2021
# On host fv-az74-779 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ctDevice, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDevice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Bits, IpAddress, NotificationType, Integer32, TimeTicks, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Bits", "IpAddress", "NotificationType", "Integer32", "TimeTicks", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CTRON-TIMED-RESET-MIB", ctTimedResetTimeEntered=ctTimedResetTimeEntered, ctTimedResetStatus=ctTimedResetStatus, ctTimedResetMIB=ctTimedResetMIB, ctTimedResetNVRamReset=ctTimedResetNVRamReset, ctTimedResetOperationalMode=ctTimedResetOperationalMode, ctTimedResetTimeRemaining=ctTimedResetTimeRemaining)
