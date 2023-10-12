#
# PySNMP MIB module RADLAN-MNGINF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-MNGINF-MIB
# Produced by pysmi-1.1.8 at Thu Oct 12 08:27:00 2023
# On host fv-az585-225 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, ModuleIdentity, Counter32, TimeTicks, NotificationType, iso, Unsigned32, Bits, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "ModuleIdentity", "Counter32", "TimeTicks", "NotificationType", "iso", "Unsigned32", "Bits", "Counter64", "Integer32")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlMngInf = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 89))
rlMngInf.setRevisions(('2003-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlMngInf.setRevisionsDescriptions(('Changed IMPORTS, added this MODULE-IDENTITY clause and editorial changes.',))
if mibBuilder.loadTexts: rlMngInf.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlMngInf.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlMngInf.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlMngInf.setDescription('The private MIB module definition for management access control.')
class RlMngInfServiceType(TextualConvention, Integer32):
    description = 'Management ACL Service type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("dontCare", 0), ("telnet", 1), ("snmp", 2), ("http", 3), ("https", 4), ("ssh", 5))

class RlMngInfActionType(TextualConvention, Integer32):
    description = 'Management ACL Action definition.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("permit", 0), ("deny", 1))

rlMngInfMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlMngInfMibVersion.setDescription("MIB's version, the current version is 1.")
rlMngInfEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfEnable.setStatus('current')
if mibBuilder.loadTexts: rlMngInfEnable.setDescription('The variable specifies if Management ACL functionality is enabled.')
rlMngInfActiveListName = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfActiveListName.setStatus('current')
if mibBuilder.loadTexts: rlMngInfActiveListName.setDescription('The currently activated Management ACL name')
rlMngInfListTable = MibTable((1, 3, 6, 1, 4, 1, 89, 89, 4), )
if mibBuilder.loadTexts: rlMngInfListTable.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListTable.setDescription('The table specifies all defined Access Lists definitions')
rlMngInfListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 89, 4, 1), ).setIndexNames((0, "RADLAN-MNGINF-MIB", "rlMngInfListName"), (0, "RADLAN-MNGINF-MIB", "rlMngInfListPriority"))
if mibBuilder.loadTexts: rlMngInfListEntry.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListEntry.setDescription('Row definition for this table.')
rlMngInfListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListName.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListName.setDescription('The Name of the Access List.')
rlMngInfListPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMngInfListPriority.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListPriority.setDescription('The Priority value.')
rlMngInfListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListIfIndex.setDescription("The IfIndex value. The IfIndex can be configured to be 0, which means don't care value.")
rlMngInfListIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIpAddr.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListIpAddr.setDescription("The IP address. The IP address can be configured to be 0, which means don't care value.")
rlMngInfListIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListIpNetMask.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListIpNetMask.setDescription('The subnet mask associated with the IP address of this entry. The value of the mask is\n         an IP address with all the network bits set to 1 and all the hosts bits set to 0.')
rlMngInfListService = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 6), RlMngInfServiceType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListService.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListService.setDescription('Service type. The Service type address can be configured to be 0,\n         which means any of Telnet, SNMP, HTTP, HTTPS, SSH.')
rlMngInfListAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 7), RlMngInfActionType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListAction.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListAction.setDescription('Action type. Can be permit or deny.')
rlMngInfListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 89, 4, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfListRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlMngInfListRowStatus.setDescription('The row status variable, used according to\n         row installation and removal conventions.')
rlMngInfAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 89, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMngInfAuditingEnable.setStatus('current')
if mibBuilder.loadTexts: rlMngInfAuditingEnable.setDescription('Controls whether SysLog messages\n   should be issued on reject by rule')
mibBuilder.exportSymbols("RADLAN-MNGINF-MIB", RlMngInfServiceType=RlMngInfServiceType, rlMngInfListTable=rlMngInfListTable, rlMngInfListIpNetMask=rlMngInfListIpNetMask, rlMngInfListRowStatus=rlMngInfListRowStatus, rlMngInfEnable=rlMngInfEnable, rlMngInf=rlMngInf, rlMngInfListPriority=rlMngInfListPriority, rlMngInfActiveListName=rlMngInfActiveListName, rlMngInfListService=rlMngInfListService, rlMngInfListAction=rlMngInfListAction, rlMngInfMibVersion=rlMngInfMibVersion, rlMngInfAuditingEnable=rlMngInfAuditingEnable, PYSNMP_MODULE_ID=rlMngInf, RlMngInfActionType=RlMngInfActionType, rlMngInfListIpAddr=rlMngInfListIpAddr, rlMngInfListName=rlMngInfListName, rlMngInfListEntry=rlMngInfListEntry, rlMngInfListIfIndex=rlMngInfListIfIndex)
