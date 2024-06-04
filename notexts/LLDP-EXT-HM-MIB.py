#
# PySNMP MIB module LLDP-EXT-HM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/lldp_hm.mib
# Produced by pysmi-1.1.12 at Tue Jun  4 08:54:10 2024
# On host fv-az2028-26 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
lldpRemTimeMark, lldpExtensions, lldpRemLocalPortNum, lldpRemIndex, lldpPortConfigEntry, lldpLocPortNum = mibBuilder.importSymbols("LLDP-MIB", "lldpRemTimeMark", "lldpExtensions", "lldpRemLocalPortNum", "lldpRemIndex", "lldpPortConfigEntry", "lldpLocPortNum")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, Gauge32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, ObjectIdentity, IpAddress, Integer32, iso, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Integer32", "iso", "TimeTicks", "Counter64")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
lldpXHmMIB = ModuleIdentity((1, 0, 8802, 1, 1, 2, 1, 5, 32867))
lldpXHmMIB.setRevisions(('2008-09-12 12:00',))
if mibBuilder.loadTexts: lldpXHmMIB.setLastUpdated('200809121200Z')
if mibBuilder.loadTexts: lldpXHmMIB.setOrganization('Hirschmann Automation & Control')
lldpXHmObjects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1))
lldpXHmConfig = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1))
lldpXHmLocalData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2))
lldpXHmRemoteData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3))
class LldpXHmLocGMRPServiceReqSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forwardAll", 1), ("forwardUnregistered", 2), ("notApplicable", 3))

class LldpXHmLocIGMPVersionSyntax(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("iGMPv1", 0), ("iGMPv2", 1), ("iGMPv3", 2))

class LldpXHmLocPortSecModeSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 1), ("forceAuthorized", 2), ("forceUnauthorized", 3), ("automatic", 4))

class LldpXHmLocPTPSupportSyntax(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("swsupport", 0), ("ptpv1capable", 1), ("ptpv2capable", 2), ("ptptccapable", 3))

class LldpXHmLocPTPStatusSyntax(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ptpv1enabled", 0), ("ptpv2enabled", 1))

class LldpXHmLocPTPv2DataTransferSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ptp2Ieee8023", 1), ("ptp2UdpIpv4", 2), ("ptp2UdpIpv6", 3), ("notApplicable", 4))

class LldpXHmLocPTPv2DelayMechanismSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("p2p", 1), ("e2e", 2), ("disabled", 3), ("notApplicable", 4))

class LldpXHmRemGMRPServiceReqSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forwardAll", 1), ("forwardUnregistered", 2), ("notApplicable", 3))

class LldpXHmRemPTPv2DataTransferSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ptp2Ieee8023", 1), ("ptp2UdpIpv4", 2), ("ptp2UdpIpv6", 3), ("notApplicable", 4))

class LldpXHmRemPTPv2DelayMechanismSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("p2p", 1), ("e2e", 2), ("disabled", 3), ("notApplicable", 4))

class LldpXHmRemPTPSupportSyntax(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("swsupport", 0), ("ptpv1capable", 1), ("ptpv2capable", 2), ("ptptccapable", 3))

class LldpXHmRemPTPStatusSyntax(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ptpv1enabled", 0), ("ptpv2enabled", 1))

class LldpXHmRemPortSecModeSyntax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 1), ("forceAuthorized", 2), ("forceUnauthorized", 3), ("automatic", 4))

class LldpXHmRemIGMPVersionSyntax(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("iGMPv1", 0), ("iGMPv2", 1), ("iGMPv3", 2))

lldpXHmConfigGMRPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 1), )
if mibBuilder.loadTexts: lldpXHmConfigGMRPTable.setStatus('current')
lldpXHmConfigGMRPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 1, 1), )
lldpPortConfigEntry.registerAugmentions(("LLDP-EXT-HM-MIB", "lldpXHmConfigGMRPEntry"))
lldpXHmConfigGMRPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXHmConfigGMRPEntry.setStatus('current')
lldpXHmConfigGMRPTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXHmConfigGMRPTxEnable.setStatus('current')
lldpXHmConfigIGMPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 2), )
if mibBuilder.loadTexts: lldpXHmConfigIGMPTable.setStatus('current')
lldpXHmConfigIGMPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 2, 1), )
lldpPortConfigEntry.registerAugmentions(("LLDP-EXT-HM-MIB", "lldpXHmConfigIGMPEntry"))
lldpXHmConfigIGMPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXHmConfigIGMPEntry.setStatus('current')
lldpXHmConfigIGMPTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXHmConfigIGMPTxEnable.setStatus('current')
lldpXHmConfigPortSecTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 3), )
if mibBuilder.loadTexts: lldpXHmConfigPortSecTable.setStatus('current')
lldpXHmConfigPortSecEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 3, 1), )
lldpPortConfigEntry.registerAugmentions(("LLDP-EXT-HM-MIB", "lldpXHmConfigPortSecEntry"))
lldpXHmConfigPortSecEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXHmConfigPortSecEntry.setStatus('current')
lldpXHmConfigPortSecTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 3, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXHmConfigPortSecTxEnable.setStatus('current')
lldpXHmConfigPTPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 4), )
if mibBuilder.loadTexts: lldpXHmConfigPTPTable.setStatus('current')
lldpXHmConfigPTPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 4, 1), )
lldpPortConfigEntry.registerAugmentions(("LLDP-EXT-HM-MIB", "lldpXHmConfigPTPEntry"))
lldpXHmConfigPTPEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXHmConfigPTPEntry.setStatus('current')
lldpXHmConfigPTPTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 1, 4, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXHmConfigPTPTxEnable.setStatus('current')
lldpXHmLocGMRPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1), )
if mibBuilder.loadTexts: lldpXHmLocGMRPTable.setStatus('current')
lldpXHmLocGMRPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXHmLocGMRPEntry.setStatus('current')
lldpXHmLocGMRPSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocGMRPSupport.setStatus('current')
lldpXHmLocGMRPStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocGMRPStatus.setStatus('current')
lldpXHmLocGMRPServiceReq = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 1, 1, 3), LldpXHmLocGMRPServiceReqSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocGMRPServiceReq.setStatus('current')
lldpXHmLocIGMPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2), )
if mibBuilder.loadTexts: lldpXHmLocIGMPTable.setStatus('current')
lldpXHmLocIGMPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXHmLocIGMPEntry.setStatus('current')
lldpXHmLocIGMPSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocIGMPSupport.setStatus('current')
lldpXHmLocIGMPStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocIGMPStatus.setStatus('current')
lldpXHmLocIGMPVersion = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 2, 1, 3), LldpXHmLocIGMPVersionSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocIGMPVersion.setStatus('current')
lldpXHmLocPortSecTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3), )
if mibBuilder.loadTexts: lldpXHmLocPortSecTable.setStatus('current')
lldpXHmLocPortSecEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXHmLocPortSecEntry.setStatus('current')
lldpXHmLocPortSecSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPortSecSupport.setStatus('current')
lldpXHmLocPortSecStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPortSecStatus.setStatus('current')
lldpXHmLocPortSecMode = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 3, 1, 3), LldpXHmLocPortSecModeSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPortSecMode.setStatus('current')
lldpXHmLocPTPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4), )
if mibBuilder.loadTexts: lldpXHmLocPTPTable.setStatus('current')
lldpXHmLocPTPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
if mibBuilder.loadTexts: lldpXHmLocPTPEntry.setStatus('current')
lldpXHmLocPTPSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 1), LldpXHmLocPTPSupportSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPSupport.setStatus('current')
lldpXHmLocPTPStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 2), LldpXHmLocPTPStatusSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPStatus.setStatus('current')
lldpXHmLocPTPSyncInterval = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPSyncInterval.setStatus('current')
lldpXHmLocPTPv2AnnounceInterval = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPv2AnnounceInterval.setStatus('current')
lldpXHmLocPTPv2DataTransfer = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 5), LldpXHmLocPTPv2DataTransferSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPv2DataTransfer.setStatus('current')
lldpXHmLocPTPv2DelayMechanism = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 6), LldpXHmLocPTPv2DelayMechanismSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPv2DelayMechanism.setStatus('current')
lldpXHmLocPTPClockValues = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 7), Bits().clone(namedValues=NamedValues(("slave", 0), ("master", 1), ("transparent", 2), ("boundary", 3), ("grandmaster", 4), ("multidomain", 5), ("simplemode", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPClockValues.setStatus('current')
lldpXHmLocPTPv2SubdomainNumber = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPv2SubdomainNumber.setStatus('current')
lldpXHmLocPTPv1SubdomainName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 2, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmLocPTPv1SubdomainName.setStatus('current')
lldpXHmRemGMRPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1), )
if mibBuilder.loadTexts: lldpXHmRemGMRPTable.setStatus('current')
lldpXHmRemGMRPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXHmRemGMRPEntry.setStatus('current')
lldpXHmRemGMRPSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemGMRPSupport.setStatus('current')
lldpXHmRemGMRPStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemGMRPStatus.setStatus('current')
lldpXHmRemGMRPServiceReq = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 1, 1, 3), LldpXHmRemGMRPServiceReqSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemGMRPServiceReq.setStatus('current')
lldpXHmRemIGMPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2), )
if mibBuilder.loadTexts: lldpXHmRemIGMPTable.setStatus('current')
lldpXHmRemIGMPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXHmRemIGMPEntry.setStatus('current')
lldpXHmRemIGMPSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemIGMPSupport.setStatus('current')
lldpXHmRemIGMPStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemIGMPStatus.setStatus('current')
lldpXHmRemIGMPVersion = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 2, 1, 3), LldpXHmRemIGMPVersionSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemIGMPVersion.setStatus('current')
lldpXHmRemPortSecTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3), )
if mibBuilder.loadTexts: lldpXHmRemPortSecTable.setStatus('current')
lldpXHmRemPortSecEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXHmRemPortSecEntry.setStatus('current')
lldpXHmRemPortSecSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPortSecSupport.setStatus('current')
lldpXHmRemPortSecStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPortSecStatus.setStatus('current')
lldpXHmRemPortSecMode = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 3, 1, 3), LldpXHmRemPortSecModeSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPortSecMode.setStatus('current')
lldpXHmRemPTPTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4), )
if mibBuilder.loadTexts: lldpXHmRemPTPTable.setStatus('current')
lldpXHmRemPTPEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: lldpXHmRemPTPEntry.setStatus('current')
lldpXHmRemPTPSupport = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 1), LldpXHmRemPTPSupportSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPSupport.setStatus('current')
lldpXHmRemPTPStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 2), LldpXHmRemPTPStatusSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPStatus.setStatus('current')
lldpXHmRemPTPSyncInterval = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPSyncInterval.setStatus('current')
lldpXHmRemPTPv2AnnounceInterval = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-128, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPv2AnnounceInterval.setStatus('current')
lldpXHmRemPTPv2DataTransfer = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 5), LldpXHmRemPTPv2DataTransferSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPv2DataTransfer.setStatus('current')
lldpXHmRemPTPv2DelayMechanism = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 6), LldpXHmRemPTPv2DelayMechanismSyntax()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPv2DelayMechanism.setStatus('current')
lldpXHmRemPTPClockValues = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 7), Bits().clone(namedValues=NamedValues(("slave", 0), ("master", 1), ("transparent", 2), ("boundary", 3), ("grandmaster", 4), ("multidomain", 5), ("simplemode", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPClockValues.setStatus('current')
lldpXHmRemPTPv2SubdomainNumber = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPv2SubdomainNumber.setStatus('current')
lldpXHmRemPTPv1SubdomainName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 5, 32867, 1, 3, 4, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpXHmRemPTPv1SubdomainName.setStatus('current')
mibBuilder.exportSymbols("LLDP-EXT-HM-MIB", lldpXHmConfigPortSecTxEnable=lldpXHmConfigPortSecTxEnable, LldpXHmRemPTPv2DataTransferSyntax=LldpXHmRemPTPv2DataTransferSyntax, lldpXHmLocIGMPVersion=lldpXHmLocIGMPVersion, lldpXHmRemPortSecEntry=lldpXHmRemPortSecEntry, lldpXHmRemPTPv2DelayMechanism=lldpXHmRemPTPv2DelayMechanism, lldpXHmRemoteData=lldpXHmRemoteData, lldpXHmConfigIGMPTxEnable=lldpXHmConfigIGMPTxEnable, lldpXHmRemIGMPEntry=lldpXHmRemIGMPEntry, LldpXHmRemPTPStatusSyntax=LldpXHmRemPTPStatusSyntax, lldpXHmLocIGMPEntry=lldpXHmLocIGMPEntry, lldpXHmLocGMRPSupport=lldpXHmLocGMRPSupport, lldpXHmLocPortSecStatus=lldpXHmLocPortSecStatus, lldpXHmConfig=lldpXHmConfig, lldpXHmRemGMRPSupport=lldpXHmRemGMRPSupport, lldpXHmLocPortSecTable=lldpXHmLocPortSecTable, lldpXHmLocIGMPStatus=lldpXHmLocIGMPStatus, LldpXHmRemGMRPServiceReqSyntax=LldpXHmRemGMRPServiceReqSyntax, lldpXHmObjects=lldpXHmObjects, lldpXHmLocPTPv2SubdomainNumber=lldpXHmLocPTPv2SubdomainNumber, LldpXHmRemPTPSupportSyntax=LldpXHmRemPTPSupportSyntax, LldpXHmLocIGMPVersionSyntax=LldpXHmLocIGMPVersionSyntax, lldpXHmRemIGMPSupport=lldpXHmRemIGMPSupport, lldpXHmRemPTPTable=lldpXHmRemPTPTable, lldpXHmRemGMRPTable=lldpXHmRemGMRPTable, LldpXHmLocPortSecModeSyntax=LldpXHmLocPortSecModeSyntax, lldpXHmLocGMRPStatus=lldpXHmLocGMRPStatus, lldpXHmLocPTPv1SubdomainName=lldpXHmLocPTPv1SubdomainName, lldpXHmLocPortSecMode=lldpXHmLocPortSecMode, LldpXHmRemPTPv2DelayMechanismSyntax=LldpXHmRemPTPv2DelayMechanismSyntax, lldpXHmLocPortSecEntry=lldpXHmLocPortSecEntry, lldpXHmRemPortSecStatus=lldpXHmRemPortSecStatus, lldpXHmLocGMRPTable=lldpXHmLocGMRPTable, lldpXHmLocPTPStatus=lldpXHmLocPTPStatus, LldpXHmRemPortSecModeSyntax=LldpXHmRemPortSecModeSyntax, lldpXHmLocPTPv2AnnounceInterval=lldpXHmLocPTPv2AnnounceInterval, lldpXHmRemPTPSyncInterval=lldpXHmRemPTPSyncInterval, lldpXHmRemGMRPStatus=lldpXHmRemGMRPStatus, lldpXHmRemGMRPServiceReq=lldpXHmRemGMRPServiceReq, lldpXHmRemIGMPVersion=lldpXHmRemIGMPVersion, lldpXHmConfigGMRPTxEnable=lldpXHmConfigGMRPTxEnable, lldpXHmConfigPTPTxEnable=lldpXHmConfigPTPTxEnable, lldpXHmRemPTPEntry=lldpXHmRemPTPEntry, lldpXHmRemIGMPTable=lldpXHmRemIGMPTable, lldpXHmRemIGMPStatus=lldpXHmRemIGMPStatus, lldpXHmLocPTPSupport=lldpXHmLocPTPSupport, lldpXHmConfigPTPTable=lldpXHmConfigPTPTable, lldpXHmRemGMRPEntry=lldpXHmRemGMRPEntry, lldpXHmRemPTPv2SubdomainNumber=lldpXHmRemPTPv2SubdomainNumber, lldpXHmLocGMRPEntry=lldpXHmLocGMRPEntry, LldpXHmLocPTPv2DataTransferSyntax=LldpXHmLocPTPv2DataTransferSyntax, lldpXHmLocIGMPTable=lldpXHmLocIGMPTable, lldpXHmRemPTPv2AnnounceInterval=lldpXHmRemPTPv2AnnounceInterval, lldpXHmConfigIGMPEntry=lldpXHmConfigIGMPEntry, lldpXHmRemPortSecTable=lldpXHmRemPortSecTable, lldpXHmRemPortSecSupport=lldpXHmRemPortSecSupport, lldpXHmLocPTPTable=lldpXHmLocPTPTable, lldpXHmConfigGMRPTable=lldpXHmConfigGMRPTable, lldpXHmConfigPortSecTable=lldpXHmConfigPortSecTable, LldpXHmLocPTPStatusSyntax=LldpXHmLocPTPStatusSyntax, LldpXHmRemIGMPVersionSyntax=LldpXHmRemIGMPVersionSyntax, lldpXHmConfigGMRPEntry=lldpXHmConfigGMRPEntry, lldpXHmMIB=lldpXHmMIB, lldpXHmLocPTPSyncInterval=lldpXHmLocPTPSyncInterval, lldpXHmConfigPTPEntry=lldpXHmConfigPTPEntry, LldpXHmLocPTPv2DelayMechanismSyntax=LldpXHmLocPTPv2DelayMechanismSyntax, lldpXHmLocPTPEntry=lldpXHmLocPTPEntry, lldpXHmConfigPortSecEntry=lldpXHmConfigPortSecEntry, lldpXHmLocPTPv2DataTransfer=lldpXHmLocPTPv2DataTransfer, lldpXHmLocIGMPSupport=lldpXHmLocIGMPSupport, lldpXHmRemPTPv1SubdomainName=lldpXHmRemPTPv1SubdomainName, lldpXHmRemPTPv2DataTransfer=lldpXHmRemPTPv2DataTransfer, lldpXHmLocalData=lldpXHmLocalData, LldpXHmLocGMRPServiceReqSyntax=LldpXHmLocGMRPServiceReqSyntax, lldpXHmRemPortSecMode=lldpXHmRemPortSecMode, lldpXHmLocPTPClockValues=lldpXHmLocPTPClockValues, LldpXHmLocPTPSupportSyntax=LldpXHmLocPTPSupportSyntax, lldpXHmRemPTPSupport=lldpXHmRemPTPSupport, lldpXHmLocGMRPServiceReq=lldpXHmLocGMRPServiceReq, lldpXHmRemPTPStatus=lldpXHmRemPTPStatus, lldpXHmLocPortSecSupport=lldpXHmLocPortSecSupport, lldpXHmConfigIGMPTable=lldpXHmConfigIGMPTable, lldpXHmLocPTPv2DelayMechanism=lldpXHmLocPTPv2DelayMechanism, PYSNMP_MODULE_ID=lldpXHmMIB, lldpXHmRemPTPClockValues=lldpXHmRemPTPClockValues)
