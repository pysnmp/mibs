#
# PySNMP MIB module CTRON-SFPS-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 09:30:02 2024
# On host fv-az1146-179 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
sfpsChassisRipTable, sfpsChassisRipAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsChassisRipTable", "sfpsChassisRipAPI")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, MibIdentifier, Bits, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter32, Counter64, NotificationType, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sfpsChassisRipChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipChassisMac.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipChassisMac.setDescription('')
sfpsChassisRipFPPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipFPPortMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipFPPortMask.setDescription('')
sfpsChassisRipINBPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipINBPortMask.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipINBPortMask.setDescription('')
sfpsChassisRipModifiedTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipModifiedTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipModifiedTime.setDescription('')
sfpsChassisRipStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("dead", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipStatus.setDescription('')
sfpsChassisRipAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("add", 2), ("delete", 3), ("purgePort", 4), ("sendUpdate", 5), ("clearTable", 6), ("setTimer", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipAPIVerb.setDescription('')
sfpsChassisRipAPIChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 2), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIChassisMac.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipAPIChassisMac.setDescription('')
sfpsChassisRipAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipAPIPort.setDescription('')
sfpsChassisRipAPITimer = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPITimer.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipAPITimer.setDescription('')
sfpsChassisRipAPINumInTable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipAPINumInTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsChassisRipAPINumInTable.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-CHASSIS-MIB", sfpsChassisRipAPIVerb=sfpsChassisRipAPIVerb, sfpsChassisRipAPINumInTable=sfpsChassisRipAPINumInTable, sfpsChassisRipAPIChassisMac=sfpsChassisRipAPIChassisMac, sfpsChassisRipModifiedTime=sfpsChassisRipModifiedTime, sfpsChassisRipAPITimer=sfpsChassisRipAPITimer, sfpsChassisRipFPPortMask=sfpsChassisRipFPPortMask, sfpsChassisRipStatus=sfpsChassisRipStatus, SfpsAddress=SfpsAddress, sfpsChassisRipAPIPort=sfpsChassisRipAPIPort, sfpsChassisRipChassisMac=sfpsChassisRipChassisMac, sfpsChassisRipINBPortMask=sfpsChassisRipINBPortMask)
