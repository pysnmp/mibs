#
# PySNMP MIB module CISCOSB-SECURITY-SUITE (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-SECURITY-SUITE
# Source digest sha256:74254b5a892f4b258ad6dce6f5a3172ccf5c900ae81943252979050c41b9e13b
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
Percents, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "Percents", "switch001")
InterfaceIndex, InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowPointer, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowPointer", "RowStatus", "TextualConvention", "TruthValue")
rlSecuritySuiteMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120))
rlSecuritySuiteMib.setRevisions(('2006-01-09 00:00',))
if mibBuilder.loadTexts: rlSecuritySuiteMib.setLastUpdated('2006-04-08 00:00')
if mibBuilder.loadTexts: rlSecuritySuiteMib.setOrganization('Cisco Systems, Inc.')
class RlsecuritySuiteGlobalEnableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("enable-global-rules-only", 1), ("enable-all-rules-types", 2), ("disable", 3), ("enable-interface-rules-only", 4))

class RlSecuritySuiteKnownDosAttackType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("stacheldraht", 1), ("invasor-Trojan", 2), ("back-orifice-Trojan", 3))

class RlSecuritySuiteKnownDosAttackProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("tcp", 1), ("upd", 2))

class RlSecuritySuiteAllMartianEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("reserved", 1), ("static", 2))

class RlSecuritySuiteDenyAttackType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("syn", 1), ("icmp-echo-request", 2), ("fragmented", 3))

class RlSecuritySuiteDenySynFinTcp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("deny", 1), ("permit", 2))

class RlSecuritySuiteSynProtectionMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("report", 2), ("block", 3))

class RlSecuritySuiteSynProtectionPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("attacked", 2), ("blocked", 3))

rlSecuritySuiteGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 1), RlsecuritySuiteGlobalEnableType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteGlobalEnable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksTable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"))
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksEntry.setStatus('current')
rlSecuritySuiteKnownDoSAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2, 1, 1), RlSecuritySuiteKnownDosAttackType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttack.setStatus('current')
rlSecuritySuiteKnownDoSAttackEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackEnable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsTable.setStatus('current')
rlSecuritySuiteKnownDoSAttacksDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteKnownDoSAttack"))
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttacksDetailsEntry.setStatus('current')
rlSecuritySuiteKnownDoSAttackProtocl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1, 1), RlSecuritySuiteKnownDosAttackProtocolType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackProtocl.setStatus('current')
rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort.setStatus('current')
rlSecuritySuiteKnownDoSAttackDestTcpUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteKnownDoSAttackDestTcpUdpPort.setStatus('current')
rlSecuritySuiteReservedMartianAddresses = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteReservedMartianAddresses.setStatus('current')
rlSecuritySuiteMartianAddrAllTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllTable.setStatus('current')
rlSecuritySuiteMartianAddrAllEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrAllEntry.setStatus('current')
rlSecuritySuiteMartianAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1, 1), IpAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddr.setStatus('current')
rlSecuritySuiteMartianAddrNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1, 2), IpAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrNetMask.setStatus('current')
rlSecuritySuiteAllMartianEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 5, 1, 3), RlSecuritySuiteAllMartianEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteAllMartianEntryType.setStatus('current')
rlSecuritySuiteMartianAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 6), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrTable.setStatus('current')
rlSecuritySuiteMartianAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 6, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteMartianAddrNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrEntry.setStatus('current')
rlSecuritySuiteMartianAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 6, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteMartianAddrStatus.setStatus('current')
rlSecuritySuiteDoSSynAttackTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackTable.setStatus('current')
rlSecuritySuiteDoSSynAttackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackIfIndex"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDoSSynAttackNetMask"))
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackEntry.setStatus('current')
rlSecuritySuiteDoSSynAttackIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackIfIndex.setStatus('current')
rlSecuritySuiteDoSSynAttackAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 2), IpAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackAddr.setStatus('current')
rlSecuritySuiteDoSSynAttackNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 3), IpAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackNetMask.setStatus('current')
rlSecuritySuiteDoSSynAttackSynRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackSynRate.setStatus('current')
rlSecuritySuiteDoSSynAttackStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 7, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDoSSynAttackStatus.setStatus('current')
rlSecuritySuiteDenyTypesTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesTable.setStatus('current')
rlSecuritySuiteDenyTypesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyIfIndex"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyAttackType"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyDestAddr"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyNetMask"), (0, "CISCOSB-SECURITY-SUITE", "rlSecuritySuiteDenyDestPort"))
if mibBuilder.loadTexts: rlSecuritySuiteDenyTypesEntry.setStatus('current')
rlSecuritySuiteDenyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 1), InterfaceIndex()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDenyIfIndex.setStatus('current')
rlSecuritySuiteDenyAttackType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 2), RlSecuritySuiteDenyAttackType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDenyAttackType.setStatus('current')
rlSecuritySuiteDenyDestAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 3), IpAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestAddr.setStatus('current')
rlSecuritySuiteDenyNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 4), IpAddress()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDenyNetMask.setStatus('current')
rlSecuritySuiteDenyDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 5), Integer32()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteDenyDestPort.setStatus('current')
rlSecuritySuiteDenyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 8, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSecuritySuiteDenyStatus.setStatus('current')
rlSecuritySuiteDenySynFinTcp = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 9), RlSecuritySuiteDenySynFinTcp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteDenySynFinTcp.setStatus('current')
rlSecuritySuiteSynProtectionMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 10), RlSecuritySuiteSynProtectionMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionMode.setStatus('current')
rlSecuritySuiteSynProtectionTreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionTreshold.setStatus('current')
rlSecuritySuiteSynProtectionRecoveryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionRecoveryTimeout.setStatus('current')
rlSecuritySuiteSynProtectionPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortTable.setStatus('current')
rlSecuritySuiteSynProtectionPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortEntry.setStatus('current')
rlSecuritySuiteSynProtectionPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1, 1), RlSecuritySuiteSynProtectionPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortMode.setStatus('current')
rlSecuritySuiteSynProtectionPortModeLastTimeAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1, 2), RlSecuritySuiteSynProtectionPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortModeLastTimeAttack.setStatus('current')
rlSecuritySuiteSynProtectionPortLastTimeAttack = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 120, 13, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecuritySuiteSynProtectionPortLastTimeAttack.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SECURITY-SUITE", PYSNMP_MODULE_ID=rlSecuritySuiteMib, RlSecuritySuiteAllMartianEntryType=RlSecuritySuiteAllMartianEntryType, RlSecuritySuiteDenyAttackType=RlSecuritySuiteDenyAttackType, RlSecuritySuiteDenySynFinTcp=RlSecuritySuiteDenySynFinTcp, RlSecuritySuiteKnownDosAttackProtocolType=RlSecuritySuiteKnownDosAttackProtocolType, RlSecuritySuiteKnownDosAttackType=RlSecuritySuiteKnownDosAttackType, RlSecuritySuiteSynProtectionMode=RlSecuritySuiteSynProtectionMode, RlSecuritySuiteSynProtectionPortMode=RlSecuritySuiteSynProtectionPortMode, RlsecuritySuiteGlobalEnableType=RlsecuritySuiteGlobalEnableType, rlSecuritySuiteAllMartianEntryType=rlSecuritySuiteAllMartianEntryType, rlSecuritySuiteDenyAttackType=rlSecuritySuiteDenyAttackType, rlSecuritySuiteDenyDestAddr=rlSecuritySuiteDenyDestAddr, rlSecuritySuiteDenyDestPort=rlSecuritySuiteDenyDestPort, rlSecuritySuiteDenyIfIndex=rlSecuritySuiteDenyIfIndex, rlSecuritySuiteDenyNetMask=rlSecuritySuiteDenyNetMask, rlSecuritySuiteDenyStatus=rlSecuritySuiteDenyStatus, rlSecuritySuiteDenySynFinTcp=rlSecuritySuiteDenySynFinTcp, rlSecuritySuiteDenyTypesEntry=rlSecuritySuiteDenyTypesEntry, rlSecuritySuiteDenyTypesTable=rlSecuritySuiteDenyTypesTable, rlSecuritySuiteDoSSynAttackAddr=rlSecuritySuiteDoSSynAttackAddr, rlSecuritySuiteDoSSynAttackEntry=rlSecuritySuiteDoSSynAttackEntry, rlSecuritySuiteDoSSynAttackIfIndex=rlSecuritySuiteDoSSynAttackIfIndex, rlSecuritySuiteDoSSynAttackNetMask=rlSecuritySuiteDoSSynAttackNetMask, rlSecuritySuiteDoSSynAttackStatus=rlSecuritySuiteDoSSynAttackStatus, rlSecuritySuiteDoSSynAttackSynRate=rlSecuritySuiteDoSSynAttackSynRate, rlSecuritySuiteDoSSynAttackTable=rlSecuritySuiteDoSSynAttackTable, rlSecuritySuiteGlobalEnable=rlSecuritySuiteGlobalEnable, rlSecuritySuiteKnownDoSAttack=rlSecuritySuiteKnownDoSAttack, rlSecuritySuiteKnownDoSAttackDestTcpUdpPort=rlSecuritySuiteKnownDoSAttackDestTcpUdpPort, rlSecuritySuiteKnownDoSAttackEnable=rlSecuritySuiteKnownDoSAttackEnable, rlSecuritySuiteKnownDoSAttackProtocl=rlSecuritySuiteKnownDoSAttackProtocl, rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort=rlSecuritySuiteKnownDoSAttackSrcTcpUdpPort, rlSecuritySuiteKnownDoSAttacksDetailsEntry=rlSecuritySuiteKnownDoSAttacksDetailsEntry, rlSecuritySuiteKnownDoSAttacksDetailsTable=rlSecuritySuiteKnownDoSAttacksDetailsTable, rlSecuritySuiteKnownDoSAttacksEntry=rlSecuritySuiteKnownDoSAttacksEntry, rlSecuritySuiteKnownDoSAttacksTable=rlSecuritySuiteKnownDoSAttacksTable, rlSecuritySuiteMartianAddr=rlSecuritySuiteMartianAddr, rlSecuritySuiteMartianAddrAllEntry=rlSecuritySuiteMartianAddrAllEntry, rlSecuritySuiteMartianAddrAllTable=rlSecuritySuiteMartianAddrAllTable, rlSecuritySuiteMartianAddrEntry=rlSecuritySuiteMartianAddrEntry, rlSecuritySuiteMartianAddrNetMask=rlSecuritySuiteMartianAddrNetMask, rlSecuritySuiteMartianAddrStatus=rlSecuritySuiteMartianAddrStatus, rlSecuritySuiteMartianAddrTable=rlSecuritySuiteMartianAddrTable, rlSecuritySuiteMib=rlSecuritySuiteMib, rlSecuritySuiteReservedMartianAddresses=rlSecuritySuiteReservedMartianAddresses, rlSecuritySuiteSynProtectionMode=rlSecuritySuiteSynProtectionMode, rlSecuritySuiteSynProtectionPortEntry=rlSecuritySuiteSynProtectionPortEntry, rlSecuritySuiteSynProtectionPortLastTimeAttack=rlSecuritySuiteSynProtectionPortLastTimeAttack, rlSecuritySuiteSynProtectionPortMode=rlSecuritySuiteSynProtectionPortMode, rlSecuritySuiteSynProtectionPortModeLastTimeAttack=rlSecuritySuiteSynProtectionPortModeLastTimeAttack, rlSecuritySuiteSynProtectionPortTable=rlSecuritySuiteSynProtectionPortTable, rlSecuritySuiteSynProtectionRecoveryTimeout=rlSecuritySuiteSynProtectionRecoveryTimeout, rlSecuritySuiteSynProtectionTreshold=rlSecuritySuiteSynProtectionTreshold)
