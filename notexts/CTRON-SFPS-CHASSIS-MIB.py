#
# PySNMP MIB module CTRON-SFPS-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 10:00:37 2023
# On host fv-az351-613 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
sfpsChassisRipTable, sfpsChassisRipAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsChassisRipTable", "sfpsChassisRipAPI")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, MibIdentifier, Counter64, ModuleIdentity, Unsigned32, Gauge32, ObjectIdentity, Bits, Counter32, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "MibIdentifier", "Counter64", "ModuleIdentity", "Unsigned32", "Gauge32", "ObjectIdentity", "Bits", "Counter32", "IpAddress", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sfpsChassisRipChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipChassisMac.setStatus('mandatory')
sfpsChassisRipFPPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipFPPortMask.setStatus('mandatory')
sfpsChassisRipINBPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipINBPortMask.setStatus('mandatory')
sfpsChassisRipModifiedTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipModifiedTime.setStatus('mandatory')
sfpsChassisRipStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("dead", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipStatus.setStatus('mandatory')
sfpsChassisRipAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("add", 2), ("delete", 3), ("purgePort", 4), ("sendUpdate", 5), ("clearTable", 6), ("setTimer", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIVerb.setStatus('mandatory')
sfpsChassisRipAPIChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 2), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIChassisMac.setStatus('mandatory')
sfpsChassisRipAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIPort.setStatus('mandatory')
sfpsChassisRipAPITimer = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPITimer.setStatus('mandatory')
sfpsChassisRipAPINumInTable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipAPINumInTable.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-CHASSIS-MIB", sfpsChassisRipAPIPort=sfpsChassisRipAPIPort, sfpsChassisRipChassisMac=sfpsChassisRipChassisMac, sfpsChassisRipAPINumInTable=sfpsChassisRipAPINumInTable, SfpsAddress=SfpsAddress, sfpsChassisRipINBPortMask=sfpsChassisRipINBPortMask, sfpsChassisRipFPPortMask=sfpsChassisRipFPPortMask, sfpsChassisRipModifiedTime=sfpsChassisRipModifiedTime, sfpsChassisRipAPIVerb=sfpsChassisRipAPIVerb, sfpsChassisRipAPITimer=sfpsChassisRipAPITimer, sfpsChassisRipAPIChassisMac=sfpsChassisRipAPIChassisMac, sfpsChassisRipStatus=sfpsChassisRipStatus)
