#
# PySNMP MIB module CTRON-ETWMIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ETWMIM-MIB
# Produced by pysmi-1.1.8 at Thu Sep 15 10:03:22 2022
# On host fv-az196-500 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ctPModuleETWMIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPModuleETWMIM")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, iso, Bits, Integer32, Gauge32, IpAddress, MibIdentifier, TimeTicks, Counter64, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "iso", "Bits", "Integer32", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CTRON-ETWMIM-MIB", etwHWRev=etwHWRev, etwEpimLink=etwEpimLink, etwDbExist=etwDbExist, etwEpimEnabled=etwEpimEnabled, etwClearNvramOnBoot=etwClearNvramOnBoot, etwFWRev=etwFWRev, etwEpimType=etwEpimType, etwDbFracToggle=etwDbFracToggle, etwDbEnabled=etwDbEnabled)
