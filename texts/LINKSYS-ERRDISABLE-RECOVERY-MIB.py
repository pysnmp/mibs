#
# PySNMP MIB module LINKSYS-ERRDISABLE-RECOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-ERRDISABLE-RECOVERY-MIB
# Source digest sha256:7e4730c8d0a548041fc36ceee175fb5e4a7424f10d997479bbdc030086f7f63f
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
rlErrdisableRecovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128))
rlErrdisableRecovery.setRevisions(('2007-11-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlErrdisableRecovery.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: rlErrdisableRecovery.setLastUpdated('2007-11-07 00:00')
if mibBuilder.loadTexts: rlErrdisableRecovery.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlErrdisableRecovery.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlErrdisableRecovery.setDescription('The private MIB module definition for Errdisable Recovery MIB.')
class RlErrdisableRecoveryCauseType(TextualConvention, Integer32):
    description = 'Errdisable Recovery Cause Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("loopback-detection", 1), ("port-security", 2), ("dot1x-src-address", 3), ("acl-deny", 4), ("stp-bpdu-guard", 5), ("stp-loopback-guard", 6), ("pcb-overheat", 7), ("udld", 8))

rlErrdisableRecoveryInterval = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 86400))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryInterval.setDescription('Timeout interval in seconds for automatic activation of an interface after shutdown.')
rlErrdisableRecoveryCauseTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseTable.setDescription('The table is used to enable or disable auto-recovery for specific\n       application causes port suspend. The table includes entries for all applications.')
rlErrdisableRecoveryCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "LINKSYS-ERRDISABLE-RECOVERY-MIB", "rlErrdisableRecoveryCause"))
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCauseEntry.setDescription('An entry (conceptual row) in the rlErrdisableRecoveryCauseEntry.')
rlErrdisableRecoveryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryCause.setDescription('Type of recovery cause.')
rlErrdisableRecoveryEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryEnable.setDescription('Enable/Disable automatic recovery.')
rlErrdisableRecoveryIfTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfTable.setDescription('The table is used for show the reason of shutdown the port in errdisable state.\n       The table includes only suspended interfaces.')
rlErrdisableRecoveryIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEntry.setDescription('An entry (conceptual row) in the rlErrdisableRecoveryIfEntry.')
rlErrdisableRecoveryIfReason = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3, 1, 1), RlErrdisableRecoveryCauseType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfReason.setDescription(' The reason of shutdown the port in errdisable state.')
rlErrdisableRecoveryIfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 128, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setStatus('current')
if mibBuilder.loadTexts: rlErrdisableRecoveryIfEnable.setDescription('Enable/Disable automatic recovery status.')
mibBuilder.exportSymbols("LINKSYS-ERRDISABLE-RECOVERY-MIB", PYSNMP_MODULE_ID=rlErrdisableRecovery, RlErrdisableRecoveryCauseType=RlErrdisableRecoveryCauseType, rlErrdisableRecovery=rlErrdisableRecovery, rlErrdisableRecoveryCause=rlErrdisableRecoveryCause, rlErrdisableRecoveryCauseEntry=rlErrdisableRecoveryCauseEntry, rlErrdisableRecoveryCauseTable=rlErrdisableRecoveryCauseTable, rlErrdisableRecoveryEnable=rlErrdisableRecoveryEnable, rlErrdisableRecoveryIfEnable=rlErrdisableRecoveryIfEnable, rlErrdisableRecoveryIfEntry=rlErrdisableRecoveryIfEntry, rlErrdisableRecoveryIfReason=rlErrdisableRecoveryIfReason, rlErrdisableRecoveryIfTable=rlErrdisableRecoveryIfTable, rlErrdisableRecoveryInterval=rlErrdisableRecoveryInterval)
