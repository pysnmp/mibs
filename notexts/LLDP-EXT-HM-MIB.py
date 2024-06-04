#
# PySNMP MIB module LLDP-EXT-HM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hirschmann/lldp_hm.mib
# Produced by pysmi-1.1.12 at Tue Jun  4 08:30:38 2024
# On host fv-az1117-967 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
lldpRemTimeMark, lldpExtensions, lldpRemIndex, lldpLocPortNum, lldpRemLocalPortNum, lldpPortConfigEntry = mibBuilder.importSymbols("LLDP-MIB", "lldpRemTimeMark", "lldpExtensions", "lldpRemIndex", "lldpLocPortNum", "lldpRemLocalPortNum", "lldpPortConfigEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, iso, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, ModuleIdentity, Counter32, Bits, Gauge32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "iso", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Counter32", "Bits", "Gauge32", "Integer32", "TimeTicks")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("LLDP-EXT-HM-MIB", lldpXHmLocIGMPStatus=lldpXHmLocIGMPStatus, lldpXHmRemGMRPTable=lldpXHmRemGMRPTable, lldpXHmRemPTPSyncInterval=lldpXHmRemPTPSyncInterval, lldpXHmLocPTPSyncInterval=lldpXHmLocPTPSyncInterval, lldpXHmConfigIGMPTxEnable=lldpXHmConfigIGMPTxEnable, LldpXHmRemPTPStatusSyntax=LldpXHmRemPTPStatusSyntax, lldpXHmLocalData=lldpXHmLocalData, lldpXHmLocPTPv2DelayMechanism=lldpXHmLocPTPv2DelayMechanism, LldpXHmRemPTPSupportSyntax=LldpXHmRemPTPSupportSyntax, lldpXHmLocIGMPTable=lldpXHmLocIGMPTable, lldpXHmObjects=lldpXHmObjects, lldpXHmRemGMRPSupport=lldpXHmRemGMRPSupport, PYSNMP_MODULE_ID=lldpXHmMIB, LldpXHmRemGMRPServiceReqSyntax=LldpXHmRemGMRPServiceReqSyntax, lldpXHmRemIGMPEntry=lldpXHmRemIGMPEntry, LldpXHmLocPortSecModeSyntax=LldpXHmLocPortSecModeSyntax, lldpXHmConfigPTPTxEnable=lldpXHmConfigPTPTxEnable, lldpXHmRemPTPEntry=lldpXHmRemPTPEntry, lldpXHmLocGMRPEntry=lldpXHmLocGMRPEntry, lldpXHmLocPortSecTable=lldpXHmLocPortSecTable, lldpXHmConfigIGMPEntry=lldpXHmConfigIGMPEntry, LldpXHmLocIGMPVersionSyntax=LldpXHmLocIGMPVersionSyntax, lldpXHmRemPTPv2DataTransfer=lldpXHmRemPTPv2DataTransfer, LldpXHmLocGMRPServiceReqSyntax=LldpXHmLocGMRPServiceReqSyntax, lldpXHmConfigPortSecEntry=lldpXHmConfigPortSecEntry, lldpXHmLocPTPStatus=lldpXHmLocPTPStatus, lldpXHmLocPTPv2DataTransfer=lldpXHmLocPTPv2DataTransfer, lldpXHmConfigPTPTable=lldpXHmConfigPTPTable, lldpXHmLocIGMPEntry=lldpXHmLocIGMPEntry, LldpXHmLocPTPv2DataTransferSyntax=LldpXHmLocPTPv2DataTransferSyntax, lldpXHmRemPortSecEntry=lldpXHmRemPortSecEntry, lldpXHmRemPTPv2SubdomainNumber=lldpXHmRemPTPv2SubdomainNumber, lldpXHmRemPTPv2DelayMechanism=lldpXHmRemPTPv2DelayMechanism, lldpXHmLocGMRPStatus=lldpXHmLocGMRPStatus, lldpXHmRemPortSecMode=lldpXHmRemPortSecMode, lldpXHmConfigGMRPEntry=lldpXHmConfigGMRPEntry, lldpXHmRemIGMPTable=lldpXHmRemIGMPTable, lldpXHmLocPTPClockValues=lldpXHmLocPTPClockValues, lldpXHmLocPortSecSupport=lldpXHmLocPortSecSupport, lldpXHmConfigIGMPTable=lldpXHmConfigIGMPTable, lldpXHmRemGMRPServiceReq=lldpXHmRemGMRPServiceReq, lldpXHmRemPortSecSupport=lldpXHmRemPortSecSupport, lldpXHmLocPTPv1SubdomainName=lldpXHmLocPTPv1SubdomainName, lldpXHmRemPortSecStatus=lldpXHmRemPortSecStatus, LldpXHmLocPTPv2DelayMechanismSyntax=LldpXHmLocPTPv2DelayMechanismSyntax, LldpXHmRemIGMPVersionSyntax=LldpXHmRemIGMPVersionSyntax, lldpXHmMIB=lldpXHmMIB, LldpXHmLocPTPStatusSyntax=LldpXHmLocPTPStatusSyntax, lldpXHmRemPTPStatus=lldpXHmRemPTPStatus, lldpXHmRemPTPTable=lldpXHmRemPTPTable, lldpXHmLocPortSecStatus=lldpXHmLocPortSecStatus, lldpXHmLocIGMPVersion=lldpXHmLocIGMPVersion, lldpXHmConfigGMRPTable=lldpXHmConfigGMRPTable, lldpXHmRemoteData=lldpXHmRemoteData, LldpXHmRemPTPv2DelayMechanismSyntax=LldpXHmRemPTPv2DelayMechanismSyntax, lldpXHmConfigGMRPTxEnable=lldpXHmConfigGMRPTxEnable, lldpXHmLocIGMPSupport=lldpXHmLocIGMPSupport, lldpXHmRemIGMPVersion=lldpXHmRemIGMPVersion, lldpXHmLocPortSecMode=lldpXHmLocPortSecMode, lldpXHmLocGMRPTable=lldpXHmLocGMRPTable, lldpXHmLocPTPv2SubdomainNumber=lldpXHmLocPTPv2SubdomainNumber, lldpXHmLocPTPEntry=lldpXHmLocPTPEntry, lldpXHmLocGMRPSupport=lldpXHmLocGMRPSupport, lldpXHmLocPTPSupport=lldpXHmLocPTPSupport, lldpXHmRemIGMPStatus=lldpXHmRemIGMPStatus, lldpXHmRemIGMPSupport=lldpXHmRemIGMPSupport, lldpXHmRemPTPSupport=lldpXHmRemPTPSupport, lldpXHmLocGMRPServiceReq=lldpXHmLocGMRPServiceReq, lldpXHmRemPTPv1SubdomainName=lldpXHmRemPTPv1SubdomainName, lldpXHmConfigPortSecTxEnable=lldpXHmConfigPortSecTxEnable, lldpXHmRemPTPClockValues=lldpXHmRemPTPClockValues, lldpXHmRemPTPv2AnnounceInterval=lldpXHmRemPTPv2AnnounceInterval, lldpXHmLocPTPv2AnnounceInterval=lldpXHmLocPTPv2AnnounceInterval, lldpXHmConfig=lldpXHmConfig, lldpXHmRemPortSecTable=lldpXHmRemPortSecTable, LldpXHmRemPTPv2DataTransferSyntax=LldpXHmRemPTPv2DataTransferSyntax, lldpXHmLocPTPTable=lldpXHmLocPTPTable, LldpXHmRemPortSecModeSyntax=LldpXHmRemPortSecModeSyntax, lldpXHmLocPortSecEntry=lldpXHmLocPortSecEntry, lldpXHmConfigPortSecTable=lldpXHmConfigPortSecTable, LldpXHmLocPTPSupportSyntax=LldpXHmLocPTPSupportSyntax, lldpXHmRemGMRPEntry=lldpXHmRemGMRPEntry, lldpXHmRemGMRPStatus=lldpXHmRemGMRPStatus, lldpXHmConfigPTPEntry=lldpXHmConfigPTPEntry)
