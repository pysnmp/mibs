#
# PySNMP MIB module CTRON-ETWMIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ETWMIM-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ctPModuleETWMIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPModuleETWMIM")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etwDbExist = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exists", 1), ("no-exists", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwDbExist.setStatus('mandatory')
etwDbEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etwDbEnabled.setStatus('mandatory')
etwDbFracToggle = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("update-table", 1), ("display-new", 2), ("display-old", 3), ("restore-old", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etwDbFracToggle.setStatus('mandatory')
etwFWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwFWRev.setStatus('mandatory')
etwHWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwHWRev.setStatus('mandatory')
etwEpimEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwEpimEnabled.setStatus('mandatory')
etwEpimType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwEpimType.setStatus('mandatory')
etwEpimLink = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("link-established", 1), ("link-not-established", 2), ("link-unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwEpimLink.setStatus('mandatory')
etwClearNvramOnBoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etwClearNvramOnBoot.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ETWMIM-MIB", etwDbEnabled=etwDbEnabled, etwFWRev=etwFWRev, etwEpimType=etwEpimType, etwEpimEnabled=etwEpimEnabled, etwHWRev=etwHWRev, etwEpimLink=etwEpimLink, etwDbExist=etwDbExist, etwClearNvramOnBoot=etwClearNvramOnBoot, etwDbFracToggle=etwDbFracToggle)
